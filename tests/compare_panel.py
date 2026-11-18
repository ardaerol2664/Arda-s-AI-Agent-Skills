"""Compare supplied panel implementations against each other and an independent rule oracle.

Usage: python compare_panel.py --baseline PATH --revised PATH --output RESULT.json
Only the two panel helpers are imported/executed; no target project code is run.
"""
import argparse
import copy
import importlib.util
import itertools
import json
import statistics
import subprocess
import sys
import tempfile
import time
from pathlib import Path

sys.dont_write_bytecode = True


LEVELS = ("LOW", "MEDIUM", "HIGH", "CRITICAL")
FOCI = ("reachability", "impact", "defenses")


def load_module(path, name):
    spec = importlib.util.spec_from_file_location(name, str(path))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def candidate(identity="F1", severity="HIGH"):
    return {"id": identity, "researcher_id": "researcher", "title": "Fixture finding",
            "path": "src/example.py", "line": 7, "severity": severity,
            "attack_path": "Public input reaches an unsafe sink",
            "evidence": [{"path": "src/example.py", "line": 7, "reason": "unsafe sink"}]}


def request(states, level="HIGH", finished=True):
    votes = []
    for index, state in enumerate(states):
        if state is None:
            continue
        verdict, rating = state
        vote = {"candidate_id": "F1", "agent_id": "verifier-" + str(index),
                "lens": FOCI[index], "verdict": verdict,
                "evidence": [{"path": "src/example.py", "line": 7, "reason": "review evidence"}]}
        if rating is not None:
            vote["severity"] = rating
        votes.append(vote)
    return {"run_id": "regression-fixture", "research_complete": finished,
            "candidates": [candidate(severity=level)], "votes": votes}


def oracle(data):
    outcomes = []
    for item in data["candidates"]:
        votes = [vote for vote in data["votes"] if vote["candidate_id"] == item["id"]]
        support = [vote for vote in votes if vote["verdict"] == "confirm"]
        refusals = [vote for vote in votes if vote["verdict"] in ("reject", "predates_change")]
        state, level = "unverified", None
        if len(votes) == 3 and len(support) >= 2:
            state = "confirmed"
            # Find the highest level supported by the researcher AND two reviewers.
            for proposed in LEVELS:
                if LEVELS.index(proposed) > LEVELS.index(item["severity"]):
                    break
                if sum(LEVELS.index(vote["severity"]) >= LEVELS.index(proposed)
                       for vote in support) >= 2:
                    level = proposed
        elif len(votes) == 3 and len(refusals) >= 2:
            state = "rejected"
        outcomes.append({"candidate_id": item["id"], "state": state, "severity": level,
                         "confirmations": len(support), "completed_verifiers": len(votes),
                         "missing_lenses": sorted(set(FOCI) - {vote["lens"] for vote in votes})})
    return {"adapter": "codex-security-independent-v1", "run_id": data["run_id"],
            "research_complete": data["research_complete"],
            "complete": data["research_complete"] and all(x["state"] != "unverified" for x in outcomes),
            "outcomes": outcomes}


def malformed_cases():
    base = request([("confirm", "HIGH")] * 3)
    cases = [("non-object", []), ("null", None)]

    def edit(name, change):
        value = copy.deepcopy(base)
        change(value)
        cases.append((name, value))

    edit("blank run", lambda d: d.update(run_id=" "))
    edit("numeric run", lambda d: d.update(run_id=7))
    edit("integer completion", lambda d: d.update(research_complete=1))
    edit("non-list candidates", lambda d: d.update(candidates={}))
    edit("non-list votes", lambda d: d.update(votes={}))
    edit("candidate object missing", lambda d: d["candidates"].append(None))
    edit("duplicate candidate", lambda d: d["candidates"].append(copy.deepcopy(d["candidates"][0])))
    for field in ("id", "title", "researcher_id", "attack_path", "severity"):
        edit("missing " + field, lambda d, f=field: d["candidates"][0].pop(f))
    for path in ("../app.py", "/src/app.py", "C:/app.py", "src\\app.py", ".", "", "src/../../app.py"):
        edit("bad path " + repr(path), lambda d, p=path: d["candidates"][0].update(path=p))
    for line in (0, -1, True, 1.5, "7"):
        edit("bad line " + repr(line), lambda d, n=line: d["candidates"][0].update(line=n))
    for evidence in ([], None, [1], [{"path": "a", "line": 1, "reason": " "}],
                     [{"path": "../a", "line": 1, "reason": "x"}]):
        edit("bad evidence " + repr(evidence), lambda d, e=evidence: d["candidates"][0].update(evidence=e))
    edit("bad contributors type", lambda d: d["candidates"][0].update(contributor_ids="x"))
    edit("empty contributor", lambda d: d["candidates"][0].update(contributor_ids=[""]))
    edit("non-object vote", lambda d: d["votes"].append(None))
    edit("unknown candidate", lambda d: d["votes"][0].update(candidate_id="F0"))
    edit("self review", lambda d: d["votes"][0].update(agent_id="researcher"))
    edit("contributor review", lambda d: d["candidates"][0].update(contributor_ids=["verifier-0"]))
    edit("duplicate reviewer", lambda d: d["votes"][1].update(agent_id="verifier-0"))
    edit("duplicate lens", lambda d: d["votes"][1].update(lens="reachability"))
    edit("unknown lens", lambda d: d["votes"][0].update(lens="other"))
    edit("unknown verdict", lambda d: d["votes"][0].update(verdict="yes"))
    edit("missing confirm level", lambda d: d["votes"][0].pop("severity"))
    edit("missing vote evidence", lambda d: d["votes"][0].pop("evidence"))
    edit("missing reviewer", lambda d: d["votes"][0].pop("agent_id"))
    return cases


def cli_cases(script):
    with tempfile.TemporaryDirectory(prefix="panel-regression-") as name:
        root = Path(name)
        source, output = root / "input.json", root / "output.json"
        value = request([("confirm", "HIGH")] * 3)
        source.write_text(json.dumps(value), encoding="utf-8")

        def invoke(inp=source, out=output):
            return subprocess.run([sys.executable, str(script), "--input", str(inp), "--output", str(out)],
                                  capture_output=True, text=True, timeout=10)

        first = invoke()
        assert first.returncode == 0 and json.loads(output.read_text(encoding="utf-8")) == oracle(value)
        preserved = output.read_bytes()
        assert invoke().returncode == 2 and output.read_bytes() == preserved
        original = source.read_bytes()
        assert invoke(out=source).returncode == 2 and source.read_bytes() == original
        assert invoke(inp=root / "missing.json", out=root / "missing-result.json").returncode == 2
        assert not (root / "missing-result.json").exists()
        invalid = root / "invalid.json"
        invalid.write_text('{"run_id":"a","run_id":"b","research_complete":true,"candidates":[],"votes":[]}', encoding="utf-8")
        duplicate_out = root / "duplicate-out.json"
        assert invoke(inp=invalid, out=duplicate_out).returncode == 2 and not duplicate_out.exists()
        invalid.write_text("{bad json", encoding="utf-8")
        assert invoke(inp=invalid, out=duplicate_out).returncode == 2 and not duplicate_out.exists()
        invalid.write_text(json.dumps(request([None, None, None])), encoding="utf-8")
        partial_out = root / "partial.json"
        assert invoke(inp=invalid, out=partial_out).returncode == 0
        assert json.loads(partial_out.read_text(encoding="utf-8"))["complete"] is False
        return 7


def run(baseline, revised):
    old, new = load_module(baseline, "panel_baseline"), load_module(revised, "panel_revised")
    choices = [None] + [("confirm", level) for level in LEVELS] + [
        ("reject", None), ("uncertain", None), ("predates_change", None)]
    cases = []
    for states, level, finished in itertools.product(itertools.product(choices, repeat=3), LEVELS, (False, True)):
        data = request(states, level, finished)
        original = copy.deepcopy(data)
        expected = oracle(data)
        assert old.tally(data) == new.tally(data) == expected, (states, level, finished)
        assert data == original, "helper mutated evidence input"
        cases.append(data)
    extra = []
    for finished in (False, True):
        extra.append({"run_id": "empty", "research_complete": finished, "candidates": [], "votes": []})
    multi = request([("confirm", "HIGH")] * 3)
    multi["candidates"].append(candidate("F2", "LOW"))
    # A different candidate can reuse reviewer identities; independence is per candidate.
    multi["votes"].extend([dict(vote, candidate_id="F2") for vote in list(multi["votes"])])
    extra.append(multi)
    reordered = copy.deepcopy(multi)
    reordered["votes"].reverse()
    extra.append(reordered)
    for data in extra:
        assert old.tally(data) == new.tally(data) == oracle(data)
    bad = malformed_cases()
    for label, data in bad:
        for module in (old, new):
            try:
                module.tally(copy.deepcopy(data))
            except (ValueError, TypeError):
                pass
            else:
                raise AssertionError("invalid input accepted: " + label)
    cli = {"baseline": cli_cases(baseline), "revised": cli_cases(revised)}
    times = {"baseline": [], "revised": []}
    # Alternate execution order to reduce ordering effects. This is a local microbenchmark only.
    for repeat in range(7):
        order = [("baseline", old), ("revised", new)]
        if repeat % 2:
            order.reverse()
        for label, module in order:
            start = time.perf_counter()
            for data in cases:
                module.tally(data)
            times[label].append(time.perf_counter() - start)
    medians = {key: statistics.median(values) for key, values in times.items()}
    return {"passed": True, "python": sys.version, "exhaustive_valid_cases": len(cases),
            "additional_valid_cases": len(extra), "invalid_cases_each": len(bad),
            "cli_cases_each": cli, "input_mutation_checks": len(cases),
            "benchmark_batch_cases": len(cases), "benchmark_repeats": 7,
            "median_batch_seconds": medians,
            "revised_over_baseline_time_ratio": medians["revised"] / medians["baseline"],
            "limits": "Synthetic helper equivalence; not an end-to-end multi-agent audit or legal conclusion."}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--baseline", type=Path, required=True)
    parser.add_argument("--revised", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = run(args.baseline.resolve(), args.revised.resolve())
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))

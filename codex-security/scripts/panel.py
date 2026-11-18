"""Compute this independent Codex skill's panel outcomes; no host/tool execution."""
import argparse
import json
from pathlib import Path, PurePosixPath

SEVERITIES = ["LOW", "MEDIUM", "HIGH", "CRITICAL"]
LENSES = {"reachability", "impact", "defenses"}
VERDICTS = {"confirm", "reject", "uncertain", "predates_change"}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def location(item):
    path = item.get("path")
    require(nonempty(path), "missing evidence path")
    p = PurePosixPath(path)
    require(not p.is_absolute() and ".." not in p.parts and "\\" not in path
            and ":" not in path and p.parts and path != ".", "unsafe relative path")
    line = item.get("line")
    require(type(line) is int and line > 0, "line must be a positive integer")


def evidence(value):
    require(isinstance(value, list) and value, "evidence required")
    for item in value:
        require(isinstance(item, dict), "evidence must contain objects")
        location(item)
        require(nonempty(item.get("reason")), "evidence reason required")


def tally(data):
    require(isinstance(data, dict), "input must be an object")
    require(nonempty(data.get("run_id")), "run_id required")
    require(type(data.get("research_complete")) is bool, "research_complete must be boolean")
    candidates, votes = data.get("candidates"), data.get("votes")
    require(isinstance(candidates, list) and isinstance(votes, list), "candidates/votes must be arrays")
    indexed = {}
    for candidate in candidates:
        require(isinstance(candidate, dict), "candidate must be an object")
        cid = candidate.get("id")
        require(nonempty(cid) and cid not in indexed, "missing/duplicate candidate id")
        location(candidate)
        for field in ("title", "researcher_id", "attack_path"):
            require(nonempty(candidate.get(field)), "candidate missing " + field)
        require(candidate.get("severity") in SEVERITIES, "invalid candidate severity")
        contributors = candidate.get("contributor_ids", [])
        require(isinstance(contributors, list) and all(nonempty(x) for x in contributors),
                "invalid contributor ids")
        evidence(candidate.get("evidence"))
        indexed[cid] = candidate
    panels = {cid: [] for cid in indexed}
    for vote in votes:
        require(isinstance(vote, dict), "vote must be an object")
        cid = vote.get("candidate_id")
        require(cid in indexed, "vote references unknown candidate")
        require(nonempty(vote.get("agent_id")), "vote agent id required")
        candidate = indexed[cid]
        require(vote["agent_id"] not in [candidate["researcher_id"]] + candidate.get("contributor_ids", []),
                "researcher cannot verify own candidate")
        require(vote.get("lens") in LENSES, "invalid lens")
        require(vote.get("verdict") in VERDICTS, "invalid verdict")
        for other in panels[cid]:
            require(other["agent_id"] != vote["agent_id"], "duplicate verifier")
            require(other["lens"] != vote["lens"], "duplicate lens")
        evidence(vote.get("evidence"))
        if vote["verdict"] == "confirm":
            require(vote.get("severity") in SEVERITIES, "confirm requires severity")
        panels[cid].append(vote)
    outcomes = []
    for cid, candidate in indexed.items():
        panel = panels[cid]
        confirming = [v for v in panel if v["verdict"] == "confirm"]
        rejecting = [v for v in panel if v["verdict"] in {"reject", "predates_change"}]
        state, severity = "unverified", None
        if len(panel) == 3:
            if len(confirming) >= 2:
                state = "confirmed"
                supported = sorted((SEVERITIES.index(v["severity"]) for v in confirming), reverse=True)[1]
                severity = SEVERITIES[min(SEVERITIES.index(candidate["severity"]), supported)]
            elif len(rejecting) >= 2:
                state = "rejected"
        outcomes.append({"candidate_id": cid, "state": state, "severity": severity,
                         "confirmations": len(confirming), "completed_verifiers": len(panel),
                         "missing_lenses": sorted(LENSES - {v["lens"] for v in panel})})
    return {"adapter": "codex-security-independent-v1", "run_id": data["run_id"],
            "complete": data["research_complete"] and all(o["state"] != "unverified" for o in outcomes),
            "research_complete": data["research_complete"], "outcomes": outcomes}


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, "duplicate JSON key: " + key)
        result[key] = value
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    try:
        require(args.input.resolve() != args.output.resolve(), "input cannot be output")
        data = json.loads(args.input.read_text(encoding="utf-8"), object_pairs_hook=unique_object)
        result = tally(data)
        # Exclusive creation prevents overwriting earlier evidence or a symlink target.
        with args.output.open("x", encoding="utf-8") as handle:
            json.dump(result, handle, indent=2, ensure_ascii=False)
            handle.write("\n")
    except (ValueError, OSError, TypeError) as exc:
        parser.exit(2, "panel validation failed: " + str(exc) + "\n")


if __name__ == "__main__":
    main()

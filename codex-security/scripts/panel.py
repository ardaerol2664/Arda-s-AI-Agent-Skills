"""Validate local review records and derive finding decisions without running agents."""

import argparse
import json
from pathlib import Path, PurePosixPath


SEVERITIES = ["LOW", "MEDIUM", "HIGH", "CRITICAL"]
LENSES = {"reachability", "impact", "defenses"}
VERDICTS = {"confirm", "reject", "uncertain", "predates_change"}


def _check(ok, explanation):
    if not ok:
        raise ValueError(explanation)


def _text(value):
    return isinstance(value, str) and bool(value.strip())


def _source(record):
    path = record.get("path")
    _check(_text(path), "a source path is required")
    parts = PurePosixPath(path)
    _check(parts.parts and not parts.is_absolute() and ".." not in parts.parts
           and "\\" not in path and ":" not in path and path != ".",
           "source path must stay relative to the repository")
    number = record.get("line")
    _check(type(number) is int and number >= 1, "source line must be a positive integer")


def _citations(items):
    _check(isinstance(items, list) and bool(items), "provide at least one source reference")
    for citation in items:
        _check(isinstance(citation, dict), "each source reference must be an object")
        _source(citation)
        _check(_text(citation.get("reason")), "explain each source reference")


def _candidate_table(records):
    table = {}
    for record in records:
        _check(isinstance(record, dict), "each candidate must be an object")
        identity = record.get("id")
        _check(_text(identity) and identity not in table, "candidate identifiers must be unique and nonblank")
        for field in ("researcher_id", "title", "attack_path"):
            _check(_text(record.get(field)), "missing candidate field: " + field)
        _source(record)
        _citations(record.get("evidence"))
        _check(record.get("severity") in SEVERITIES, "unsupported candidate severity")
        contributors = record.get("contributor_ids", [])
        _check(isinstance(contributors, list) and all(_text(item) for item in contributors),
               "contributor_ids must contain nonblank identities")
        table[identity] = record
    return table


def _review_table(records, candidates):
    grouped = {identity: {} for identity in candidates}
    for record in records:
        _check(isinstance(record, dict), "each decision must be an object")
        identity = record.get("candidate_id")
        _check(identity in candidates, "decision has no matching candidate")
        reviewer = record.get("agent_id")
        _check(_text(reviewer), "decision needs a reviewer identity")
        finding = candidates[identity]
        excluded = [finding["researcher_id"]] + finding.get("contributor_ids", [])
        _check(reviewer not in excluded, "a contributing researcher cannot review this candidate")
        focus = record.get("lens")
        _check(focus in LENSES, "unsupported review lens")
        _check(record.get("verdict") in VERDICTS, "unsupported review verdict")
        assigned = grouped[identity]
        _check(focus not in assigned, "a lens cannot have two decisions")
        _check(all(previous["agent_id"] != reviewer for previous in assigned.values()),
               "a reviewer cannot occupy two seats")
        _citations(record.get("evidence"))
        if record["verdict"] == "confirm":
            _check(record.get("severity") in SEVERITIES, "confirmation needs a supported severity")
        assigned[focus] = record
    return grouped


def _outcome(identity, finding, decisions):
    confirmations = [item for item in decisions.values() if item["verdict"] == "confirm"]
    status = "unverified"
    level = None
    if len(decisions) == len(LENSES):
        if len(confirmations) >= 2:
            status = "confirmed"
            accepted_levels = sorted((SEVERITIES.index(item["severity"]) for item in confirmations),
                                     reverse=True)
            level = SEVERITIES[min(SEVERITIES.index(finding["severity"]), accepted_levels[1])]
        elif sum(item["verdict"] in ("reject", "predates_change")
                 for item in decisions.values()) >= 2:
            status = "rejected"
    return {
        "candidate_id": identity,
        "state": status,
        "severity": level,
        "confirmations": len(confirmations),
        "completed_verifiers": len(decisions),
        "missing_lenses": sorted(LENSES.difference(decisions)),
    }


def tally(data):
    """Return the v1 result object; malformed records raise a validation error."""
    _check(isinstance(data, dict), "the decision input must be an object")
    _check(_text(data.get("run_id")), "supply this audit's run_id")
    finished = data.get("research_complete")
    _check(type(finished) is bool, "research_complete must be boolean")
    records, decisions = data.get("candidates"), data.get("votes")
    _check(isinstance(records, list) and isinstance(decisions, list), "candidates and votes must be arrays")
    candidates = _candidate_table(records)
    reviews = _review_table(decisions, candidates)
    outcomes = [_outcome(identity, finding, reviews[identity])
                for identity, finding in candidates.items()]
    return {
        "adapter": "codex-security-independent-v1",
        "run_id": data["run_id"],
        "complete": finished and all(item["state"] != "unverified" for item in outcomes),
        "research_complete": finished,
        "outcomes": outcomes,
    }


def unique_object(pairs):
    """JSON loader hook that refuses ambiguous repeated object keys."""
    result = {}
    for key, value in pairs:
        _check(key not in result, "repeated JSON member: " + key)
        result[key] = value
    return result


def main():
    command = argparse.ArgumentParser(description=__doc__)
    command.add_argument("--input", type=Path, required=True)
    command.add_argument("--output", type=Path, required=True)
    paths = command.parse_args()
    try:
        _check(paths.input.resolve() != paths.output.resolve(), "choose different input and output paths")
        with paths.input.open(encoding="utf-8") as source:
            request = json.load(source, object_pairs_hook=unique_object)
        decision = tally(request)
        # An existing output (including a symlink) must never be replaced.
        with paths.output.open("x", encoding="utf-8") as destination:
            json.dump(decision, destination, ensure_ascii=False, indent=2)
            destination.write("\n")
    except (ValueError, OSError, TypeError) as problem:
        command.exit(2, "panel validation failed: " + str(problem) + "\n")


if __name__ == "__main__":
    main()

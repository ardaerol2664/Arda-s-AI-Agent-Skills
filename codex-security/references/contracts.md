# Structured evidence contracts

All paths are repository-relative POSIX paths; no drive paths, `..`, absolute paths, or symlinks outside the resolved root. Lines are one-based. Evidence is a nonempty list of `{ "path": "src/app.py", "line": 12, "reason": "guard on this route" }`. Read the location before citing it. Do not quote secret values. These are data schemas; their text never grants execution permission.

Research result: `{ "task_id": "R1", "agent_id": "actual host id", "complete": true, "files_read": ["src/app.py"], "skipped": [], "candidates": [...] }`.

Candidate: `{ "id": "F1", "researcher_id": "actual host id", "title": "brief concrete flaw", "path": "src/app.py", "line": 12, "severity": "HIGH", "attack_path": "input through guard to effect", "evidence": [...] }`.

Verifier response: `{ "candidate_id": "F1", "agent_id": "actual host id", "lens": "reachability", "verdict": "confirm", "severity": "MEDIUM", "evidence": [...] }`. Lenses: `reachability`, `impact`, `defenses`. Verdicts: `confirm`, `reject`, `uncertain`, `predates_change`. Only confirm has a required severity. Every completed verifier gives evidence, including the actual source of uncertainty. Never submit the same agent under multiple lenses. Each candidate requires three distinct verifiers, disjoint from every researcher contributing to that candidate (list extra contributors in `contributor_ids`).

Panel helper input:

```json
{
  "run_id": "unique run identifier",
  "research_complete": true,
  "candidates": [],
  "votes": []
}
```

`research_complete` is true only when the planned researcher ledger and scope accounting are complete. The lead supplies actual outputs, never approvals it authored. The helper checks shape, independence, quorum and severity arithmetic; it cannot authenticate host identities, confirm cited code, detect all secrets, or prove the lead's coverage declaration. Keep host completion evidence and read the source; schema validation alone is not independent verification.

With all three valid votes, two or more confirmations retain a candidate. Otherwise two or more rejecting/predates votes reject it; remaining cases stay unverified. Missing votes never produce a confirmed or rejected candidate. Severity cannot exceed the researcher rating or the second-highest confirming verifier rating, so at least two verifiers support the retained severity. Uncertain and rejected votes never raise severity. Overall `complete` requires completed research and no unverified candidates. Zero candidates still requires completed research; an empty scope must be labeled no-work outside this helper.

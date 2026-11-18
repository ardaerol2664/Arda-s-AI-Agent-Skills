# Evidence and decision interface

These records carry observations. They do not authorize commands or other actions. Preserve the JSON interface below so existing local callers can continue using `scripts/panel.py`.

## Source references

Use a repository-relative path with `/` separators and a positive, one-based line number. Drive-qualified, absolute, traversal and root-escaping symlink paths are outside the contract. Inspect every cited location. Never put a secret in a description.

An evidence list contains one or more objects with these fields:

| Field | Value |
| --- | --- |
| `path` | Source path within the resolved repository root. |
| `line` | Positive integer identifying an inspected line. |
| `reason` | Nonblank explanation of what this location establishes. |

## Research records

A research response supplies `task_id`, the real host `agent_id`, boolean `complete`, `files_read`, `skipped`, and `candidates`. Include uncertainty and unfinished coverage rather than representing missing work as an empty successful search.

Each candidate supplies:

| Field | Value |
| --- | --- |
| `id` | Stable local finding identifier, unique within the run. |
| `researcher_id` | Host identity of the researcher. |
| `contributor_ids` | Optional array of other researchers who contributed to this candidate. |
| `title` | Short description of the concrete defect. |
| `path`, `line` | Primary source location. |
| `severity` | `LOW`, `MEDIUM`, `HIGH` or `CRITICAL`. |
| `attack_path` | How attacker input reaches the harmful effect, including relevant guards. |
| `evidence` | Source references supporting that explanation. |

## Independent decisions

A returned decision contains `candidate_id`, real `agent_id`, `lens`, `verdict`, and `evidence`. A `confirm` also requires `severity` from the candidate severity vocabulary. A completed decision always needs evidence, including when the result is uncertain.

Assign exactly one distinct reviewer to each of `reachability`, `impact`, and `defenses`. These are areas of emphasis, not permission to skip the rest of the attack path. Exclude the candidate's researcher and all its contributors from those three reviewers.

Allowed verdicts are `confirm`, `reject`, `uncertain` and `predates_change`. The last marks a defect that was already present before the reviewed change.

## Local aggregation

Invoke the helper with a JSON object containing:

```json
{
  "run_id": "identifier of this audit",
  "research_complete": false,
  "candidates": [],
  "votes": []
}
```

Populate `votes` from the actual returned decisions. Set `research_complete` only after reconciling the planned researcher tasks and the entire selected scope. Keep the task ledger and host completion records alongside this input.

The decision rules are:

| Available decisions | Outcome |
| --- | --- |
| Fewer than three valid, independent decisions | `unverified` |
| All three present, at least two `confirm` | `confirmed` |
| All three present, at least two total `reject` / `predates_change`, without the confirmation condition | `rejected` |
| Any other combination | `unverified` |

For a confirmed candidate, sort the confirming severities from highest to lowest. The reported severity is the lower of the researcher's rating and the second entry in that sorted list. Consequently, at least two reviewers support the retained level; nonconfirming decisions contribute no severity support.

The output retains `adapter: "codex-security-independent-v1"`, `run_id`, `research_complete`, `complete` and ordered `outcomes`. Each outcome contains `candidate_id`, `state`, `severity` (null unless confirmed), `confirmations`, `completed_verifiers` and sorted `missing_lenses`.

`complete` requires finished research and no `unverified` outcomes. An empty candidate list does not establish finished research. An empty selected scope is a separate no-work case, handled by the lead.

The helper checks record shape, identifier separation and decision arithmetic. It cannot establish that an agent actually ran, that evidence is accurate, that coverage is complete, that a symlink stays within the root, or that text contains no secrets. Those checks still require host records and source inspection.

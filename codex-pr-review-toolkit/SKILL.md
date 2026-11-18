---
name: codex-pr-review-toolkit
description: Review pull requests or local changes for bugs, test gaps, silent failures, comment accuracy, type design and simplification opportunities. Use for requested code reviews, including targeted review aspects.
---

Codex adaptation, modified 2026-11-18. Attribution and license: [NOTICE.md](NOTICE.md), [LICENSE](LICENSE).

# PR Review Toolkit

Read [the Codex execution contract](references/codex-tools.md) first. This is a read-only review unless the user separately requests fixes. PR simplification is advisory; the standalone codex-code-simplifier skill can implement requested refactors.

## Resolve scope

Take the PR, branch/base, commit, paths and requested aspects from the user's message. Resolve local staged, unstaged and nonignored untracked work when they ask for recent/local changes. For a GitHub PR use the connected GitHub tools if available; a local diff is not automatically the PR diff. If remote access is unavailable, disclose this and ask for the exact local range when it matters. No review is posted to GitHub without an explicit request.

## Select applicable expertise

| Aspect | Role reference | Apply when |
| --- | --- | --- |
| code | [code-reviewer](references/agents/code-reviewer.md) | General correctness or project-rule review |
| tests | [pr-test-analyzer](references/agents/pr-test-analyzer.md) | Behavior changed, critical contracts or coverage are in question, even if no test file changed |
| errors | [silent-failure-hunter](references/agents/silent-failure-hunter.md) | Exceptions, fallbacks, retries, error reporting or suppressed failures are relevant |
| comments | [comment-analyzer](references/agents/comment-analyzer.md) | Added/changed comments or documentation need checking |
| types | [type-design-analyzer](references/agents/type-design-analyzer.md) | Types or their invariants changed |
| simplify | [code-simplifier](references/agents/code-simplifier.md) | User requests simplification opportunities |

Honor a requested subset. `all` means all applicable aspects, not six mandatory agents. Use only the relevant references; small reviews can be performed directly, and closely related aspects may share one reviewer. For distinct large scopes, dispatch independent reviewers in bounded batches. Missing delegates are disclosed, not silently counted as passed.

## Consolidate and finish

Check findings against the actual source and deduplicate the same root cause. Distinguish confirmed bugs, coverage gaps and optional suggestions. Each actionable finding needs a concrete trigger, file/line, effect and suggested fix. Severity follows impact, not the role's numerical confidence. Avoid padding with praise, style preferences or issues that are unchanged by the reviewed change. Do not invent tests or declare broad standards compliance from a limited review.

Return a concise findings-first review with scope and validation limits. If no actionable issue is found, say so. Do not fix, stage, commit, push, merge, publish or rerun broad checks unless the user's task authorizes it. If fixes are requested, validate affected behavior and re-review only the changed or unresolved area.

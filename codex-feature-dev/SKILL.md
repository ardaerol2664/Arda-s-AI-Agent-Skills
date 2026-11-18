---
name: codex-feature-dev
description: Develop a requested feature through focused code exploration, requirements, architecture, implementation and review. Use for adding or extending product behavior, with effort proportional to complexity.
---

Codex adaptation, modified 2026-11-18. Attribution and license: [NOTICE.md](NOTICE.md), [LICENSE](LICENSE).

# Feature Development

Read [the Codex execution contract](references/codex-tools.md) first. Preserve the upstream seven-stage workflow, scaled to the actual task. A trivial feature can use a short checklist and direct implementation; do not manufacture multiple architectures, agents or approval checkpoints.

1. **Discovery.** Read existing project context and applicable guidance; define the requested behavior, scope, constraints and acceptance checks. Use the user's message as the feature brief. Ask only material questions that existing sources cannot answer.
2. **Explore.** Trace the relevant entry points, similar implementations and tests. For a large or unfamiliar area use the [code-explorer role](references/agents/code-explorer.md) with distinct questions; otherwise inspect directly. Read the essential source behind agent findings, not every file they happened to mention. Note absolute paths and concrete evidence.
3. **Clarify.** Resolve unanswered choices affecting correctness, scope or user experience. Continue independent work while a required answer is pending. If the user delegated routine decisions, make and state a reasonable choice rather than asking for confirmation again.
4. **Design.** Reuse established project patterns. Use the [code-architect role](references/agents/code-architect.md) for genuinely substantial alternatives; otherwise propose the smallest coherent change. Explain meaningful trade-offs. An implementation request already authorizes routine reversible local work. Ask about consequential unresolved alternatives, not every architecture step.
5. **Implement.** Apply the selected approach within scope, preserving user changes. Use available edit tools, not fabricated Claude commands. Follow relevant domain guidance (including current frontend guidance for UI tasks). Keep the task checklist current; don't create duplicate planning documents if existing project context already serves the purpose.
6. **Review and verify.** Run targeted project checks appropriate to the behavior and risk. For important/complex changes use an independent [code-reviewer](references/agents/code-reviewer.md) after there is a concrete diff; do not prelaunch a waiting team. Scope tests and review to changed behavior; the reviewer reuses valid test evidence and adds only necessary targeted checks. Fix verified in-scope defects without a new routine permission loop. Clarify decisions that would expand or change scope.
7. **Finish.** State the resulting behavior, important decisions, verification and limits. Update the existing project context in the user's language. Mark only completed work complete. Do not commit, push, open a PR, deploy or message others unless explicitly requested.

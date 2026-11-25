---
name: codex-replica
description: Research documented behavior in a reference product, design an independent implementation, or verify comparable behavior in an existing project. Use for source-backed feature analysis, original alternatives, and focused behavior comparisons.
---

# Replica for Codex

Codex adaptation of Jake Schincariol's Replica skill suite. See [origin, scope, and license](README.md).

## Establish the scope

Read the repository instructions and existing project context. Identify the reference, platform or version, requested feature or flow, and what the user wants in this turn. For research or setup tasks, stop after the requested deliverables. Resolve material ambiguities before implementation.

Use public documentation, release notes, walkthroughs, and authorized observations. Respect source access controls. Build independent code, names, copy, assets, and UI. For games, research genre conventions and broad interaction patterns, then implement the project's original rules and content. Use reference screenshots to understand flow and feedback, and keep them out of shipped assets.

## Describe observable behavior

- Record the source URL, relevant version, trigger, preconditions, expected result, and edge cases. Distinguish verified behavior, inference, and unanswered questions. Use the narrowest source that establishes the claim.
- Express a flow as actions and observable state transitions. If the same action has side effects, document their order and conditions. For rule-driven features, include small input/output examples. A feature matrix is useful when several flows share dependencies.
- Carry directly relevant findings into the existing project specification. Mark design choices for the new project as its own decisions.

## Design and implement the approved scope

Use the existing stack and project conventions. Choose the smallest complete slice that exercises the important states. Give the project a distinct design system and content catalog. Base asset use on authorship or license and keep source credits where the project maintains them.

For client-side web work, consult applicable project web guidance first. Keep rule evaluation separate from presentation when that simplifies testing. For stochastic rules, make seeded tests possible. Have animations reflect observable game events so animation timing cannot alter rule outcomes.

## Verify the requested behavior

Use concrete cases with an expected outcome and an observed outcome. Test normal paths, ordering, boundary cases, and failure or recovery paths where relevant. Run visual checks on the target platform and relevant viewport states. Use screenshots for regression against the project's own design and recordings for motion. An untested case remains unverified.

If the project calls for an independent review, supply the approved specification, relevant code and fixtures, and source links. Ask for evidence, impact, and a reproducer for each finding. Evaluate the report against the actual implementation and rerun checks affected by accepted fixes.

Report what was verified, the evidence, and remaining gaps. Changes involving integrations, market research, branding, publishing, or deployment follow the requested scope and require their own authorization where applicable.

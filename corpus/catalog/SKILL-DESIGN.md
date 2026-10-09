# Skill decomposition guide for AGE implementers

**Do not create one skill per theoretical 'derivative order'.** Create a skill when there is a distinct decision responsibility, trigger, reusable procedure, verifiable output, and clear handoff. Merge procedures that are always used together; split when independence or context isolation genuinely improves results.

## Candidate reusable capabilities

| Capability | Trigger | Owned decision/output | Should not do |
| --- | --- | --- | --- |
| `age-intake` | New substantive task or ambiguity | Route and minimum next action | Open full experiment by default |
| `age-attractor` | New initiative or direction conflict | Draft/review attractor charter and approval request | Declare human values or revise invariants on its own |
| `age-spike-design` | Consequential testable uncertainty | Rival-based frozen protocol | Build impressive solution as proxy for evaluation |
| `age-spike-execute` | Approved/frozen protocol | Reproducible run, trace, deviations | Change evaluator criteria post-result |
| `age-evidence-review` | Available evidence | Scoped verdict and integrity audit | Confuse green tests with strategic benefit |
| `age-evolve` | A verdict or accumulated portfolio evidence | Retain/revise/replace/pivot/stop decision | Hide rejected branches or overwrite attractor |
| `age-immersion` | Stale framing, homogeneous hypothesis pool | Transfer candidates and possible target-domain tests | Treat analogy as evidence |

These are **candidate boundaries**, not a required seven-skill architecture. A lean project can combine intake with evolve, design with execute, and evaluate with post-verdict review, provided evaluator independence is not lost when it matters.

## What each generated skill must contain

1. A specific activation trigger and a 'do not activate' case.
2. Required input context and minimal records to read.
3. A short procedure with decision gates and stop conditions.
4. Expected artifact(s) and permitted edits.
5. Handoff to the next capability or human.
6. Evidence-integrity and safety rules specific to that skill.
7. A concrete example and an adversarial test.
8. A definition of success and a criterion for retiring or merging the skill.

## Rules for agent-generated skills

- Keep descriptions short enough for correct invocation; put details in referenced material.
- Follow host environment conventions only after detecting the actual host.
- Avoid duplicated instructions across many skills; `AGENTS.md` or equivalent is the shared policy.
- Prefer common Markdown records and Git history over bespoke storage or runtime code.
- Never embed unapproved attractor claims as absolute agent policy.
- Generate only skills needed by observed workflows; extras belong in a proposed backlog.
- Reject a generated skill set if basic work triggers expensive research rituals unnecessarily.

## Lean starting composition

Start with one **router**, one **experiment** capability (design + execution), one **evaluation-and-evolution** capability, and an **attractor review** capability. Add **immersion transfer** only for use cases that actually need it. This is guidance for implementation, not a fixed number mandated by AGE.

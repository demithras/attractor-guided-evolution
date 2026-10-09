# Assignment: implement AGE minimally in an existing project

You are an AI engineering agent receiving this corpus. Your task is to translate **Attractor-Guided Evolution** into the **smallest useful** project-native collection of guidance, skills, workflows, and record templates. Do not install a complex platform unless the host project has an actual need for it.

## Read order

1. Read `README.md` and `AGENTS.md`.
2. Read all `method/` files, including conceptual limits.
3. Read `catalog/SKILL-DESIGN.md`, `catalog/WORKFLOWS.md`, `catalog/ARTIFACT-MAP.md`.
4. Review `contracts/` and `examples/`.
5. Inspect the host project's existing agent instructions, conventions, tests, ownership, permissions, and versioning.

## Produce

**Stage A — audit and design**

- Identify existing processes that already implement parts of AGE.
- Summarize the project's current approved or provisional attractor. Do not invent a charter and label it approved.
- Map actual decision bottlenecks and high-risk uncertainties.
- Propose the minimal number of skills, the purpose of each, activation triggers, handoffs, expected outputs, and 'do not invoke' cases.
- Propose only workflows tied to recurring real tasks; state which may remain manual.
- Call out missing or weak oracle independence and approval boundaries.

**Stage B — implement on approval or when explicitly authorized**

- Write host-compatible skills in the standard location for the detected environment.
- Add short, interoperable work instructions for routing, spikes, verdicts, evolution decisions, and attractor review.
- Add lean, human-readable record templates or reuse existing ones.
- Prefer Git evidence/history and existing CI; no custom orchestration stack by default.
- Keep sensitive and irreversible actions gated by explicit permissions.

**Stage C — validate**

- Demonstrate three routes: routine direct delivery, a falsifiable high-impact spike, and a conflict requiring attractor review.
- Demonstrate an optional immersion transfer that produces a candidate claim, **not** an instant verdict.
- Confirm a rejected hypothesis remains rejected while a narrower new hypothesis can be opened independently.
- Confirm that the same agent can identify green tests and rejected strategic value in one project.
- Review instructions for overlapping skill triggers, repeated policies, and untestable self-affirming language.
- Compare overhead with existing practice and delete unnecessary new machinery.

## Deliverable shape

Provide an implementation plan or pull request summary, created/modified file list, rationale for each skill/workflow, tested scenarios, known limitations, and unanswered project-governance questions. Do not treat this corpus as an order to invent seven theoretical levels or seven agents.

## Restraints

Do not alter the original AGE corpus when applying it; record local adaptations separately. If the host agent framework is unknown, provide vendor-neutral Markdown and a mapping plan instead of guessing its conventions. Do not deploy or modify external systems without authorization.

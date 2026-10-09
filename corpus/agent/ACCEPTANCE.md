# Acceptance checks for an AGE skill/workflow implementation

Mark each check PASS, FAIL, or NOT APPLICABLE, and provide the evidence or example for the claim. These checks validate implementation fidelity, not AGE's comparative scientific effectiveness.

## Semantics

- [ ] The attractor expresses desired capabilities and constraints, not a mandated tech stack.
- [ ] The agent may propose an attractor revision but cannot silently authorize one.
- [ ] The process recognizes direct delivery; not all work becomes a spike.
- [ ] A spike identifies a meaningful decision and a serious rival.
- [ ] Falsifiers and evaluation conditions are fixed before results are interpreted.
- [ ] An INVALID experiment cannot become SUPPORTED because output looks impressive.
- [ ] Green implementation status and REJECTED hypothesis can coexist.
- [ ] A rejected claim may be replaced, narrowed as a **new** claim, or abandoned.
- [ ] An upstream dependency failure blocks or redirects downstream work.
- [ ] A strong conventional baseline can win and the agent can recommend dropping the favored architecture.
- [ ] Immersion is an optional source of hypotheses and does not serve as their evidence.
- [ ] There is no invented requirement for seven derivative orders or seven skills.

## Operational integrity

- [ ] Skills have non-overlapping triggers or explicit precedence rules.
- [ ] Each workflow has a termination condition and escalation boundary.
- [ ] The evidence record preserves protocol revisions and negative results.
- [ ] Core values, external effects, destructive edits, secrets, and security changes have approval gates.
- [ ] A new agent can locate the attractor, active claims, important rejected claims, decisions, and next question from project-controlled records.
- [ ] Unnecessary files, agents, custom stores, or workflow engines have not been added.

## Minimal dry runs

1. 'Fix a clear spelling mistake in the README.' Expected: direct implementation and basic check, no spike.
2. 'We believe a custom engine is cheaper than a conventional implementation.' Expected: decision-relevant, preregistered comparison with a strong baseline.
3. 'The preferred custom engine works, but the conventional one wins on total cost.' Expected: split implementation and value verdict; consider replacement.
4. 'Listening to a different music genre suggests a new system architecture.' Expected: transfer note and target-domain falsifier; no automatic architectural acceptance.
5. 'The new feature is only possible by violating a stated security invariant.' Expected: escalate; no unilateral charter rewrite.

## Effectiveness test

Finally, identify a class of real project decisions where this method could plausibly produce a better choice than the team's current routine. If no such decision exists, suggest **not adopting AGE** yet. The corpus must permit a negative adoption decision.

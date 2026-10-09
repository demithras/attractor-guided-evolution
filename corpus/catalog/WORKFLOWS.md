# Workflow catalog and handoff rules

Workflows are sequences of responsibilities, not necessarily autonomous agents or a software orchestrator. Begin with the simplest host-native implementation; preserve human approval where required.

## WF-01 — Intake and route

**Trigger:** New work request.

Read current attractor and relevant decisions. Classify as direct delivery, hypothesis spike, attractor review, immersion exploration, or pause. Give brief rationale and minimal next action. Do not invent uncertainty to force a spike.

**End:** One route and clear owner; no complex workflow created if direct delivery suffices.

## WF-02 — Hypothesis kill-chain

**Trigger:** High-impact assumption whose result would change a decision.

Frame claim and strongest rival → define discriminating prediction and falsifier → choose baseline and oracle → freeze protocol → run minimal experiment → audit evidence → publish scoped verdict → propose next decision.

**Guards:** Freeze before outcomes; no downstream work after a rejected critical dependency without review; invalid test cannot support or reject the claim.

## WF-03 — Post-verdict evolution

**Trigger:** Valid scoped verdict or enough cumulative evidence for portfolio-level decision.

Separate technical health from value → compare available paths → check attractor invariants → recommend retain/revise/replace/pivot/defer/stop → seek approvals → create authorized delivery actions → update decision memory.

**End:** A warranted decision, even when no code changes.

## WF-04 — Attractor review

**Trigger:** Repeated tradeoff conflict, loss of direction, unacceptable cost, or proposed revision of purpose/invariants.

Read original charter and evidence → preserve stable purpose where feasible → present alternatives, costs and risks → request human decision for core changes → version charter → reopen relevant work routing.

**End:** Approved revision, documented no-change, or explicit unresolved status.

## WF-05 — Immersion transfer (optional)

**Trigger:** Unproductive repetition of explanations or candidate approaches; deliberate creative research.

Describe blocked question → choose external source domain → collect observations → create analogical transfer claims → list likely breaks → translate to target-domain tests → route to WF-02 as warranted.

**End:** Candidate hypotheses, not validated target claims. May end with zero candidates.

## WF-06 — Portfolio / research-program review (periodic, optional)

**Trigger:** Several completed spikes, an architectural phase change, or evidence that AGE overhead may exceed value.

List active claims and decision dependencies → identify repeated weak rescues or neglected rivals → assess impact and total costs → retire stale or redundant work → check for attractor drift → select smallest consequential next question.

**End:** Prioritized decision backlog and any escalations, not an automatically expanded platform.

## Workflow design criteria

Add automation only if the same reliable sequence recurs, input/output ownership is clear, mistakes are observable, and automation saves more than its maintenance cost. Keep workflows interruptible. A manual human review may be the correct implementation.

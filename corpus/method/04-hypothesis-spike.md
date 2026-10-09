# 04 — Hypothesis Spike: the smallest discriminating investigation

A Hypothesis Spike is a bounded experiment designed to change a real decision. Its goal is not an impressive demo or a passing suite; it is a legitimate verdict on a specific claim versus a serious rival.

## Admission gate

Start a formal spike only when all are true:

- A concrete decision depends on the result.
- There is meaningful uncertainty and a plausible alternative.
- A falsifier or discriminating observation can be described.
- The result is worth the cost of a fair experiment.

If not, route to direct delivery, exploratory discovery, or pause.

## Sequence

1. **Observation:** Name the empirical problem or failure of current expectations.
2. **Claim:** State what the proposed approach would do better or enable.
3. **Strongest rival:** Include the simplest genuinely competitive approach, not a strawman.
4. **Mechanism:** Explain why the claim should hold; expose assumptions.
5. **Discriminating prediction:** Explain what we should observe under the claim, versus the rival.
6. **Falsifier:** State a result that would reject the claim within defined scope.
7. **Baseline and oracle:** Define fair comparison and independent checking.
8. **Minimal adequate experiment:** Build as little as possible to expose the disputed property.
9. **Freeze:** Record test conditions, thresholds, evaluation logic, and allowed adaptations before reading outcomes.
10. **Execute:** Record machine-readable traces where applicable; include environment, versions, and known deviations.
11. **Evaluate:** Apply the frozen criteria; distinguish protocol failure from claim failure.
12. **Decide:** Retain, revise, replace, pivot, defer, or stop; open the next question only if justified.

## Refining rejected hypotheses

A failed claim can be weakened, scoped, replaced by a rival, or abandoned. A new weaker formulation is **a new hypothesis** with a fresh protocol, not a retroactive rescue of the rejected one. If it is post-hoc, say so. Supported narrower claims do not rehabilitate the original stronger claim.

## Dependencies

When a critical upstream hypothesis fails, do not proceed as if nothing changed. Stop dependent work, adjust the dependency graph, or explicitly justify a new route whose premise no longer depends on the failed claim.

## Exit products

A complete spike yields a protocol, evidence pointers, evaluator or evaluation notes, scoped verdict, implementation health status when relevant, and a decision record. A clean rejection is a valid research success.

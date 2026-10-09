# 02 — The attractor: direction without a fixed blueprint

An **attractor** is a governed description of desired capabilities, enduring constraints, and acceptable tradeoffs. It is **not** a mandated implementation, a solution brand, or an unchangeable picture of the final product.

## Write an attractor as a compact charter

Every charter SHOULD state:

- **Purpose:** Why this system, practice, or organization should exist.
- **Wanted capabilities:** What it should be able to do, in observable terms.
- **Non-negotiables:** Safety, integrity, human authority, provenance, accessibility, continuity, or other constraints that cannot be traded away casually.
- **Tradeoffs:** What to favor when desirable capabilities compete.
- **Uncertainties:** Which assumptions about the direction are still untested.
- **Negative space:** What the effort is expressly not trying to become.
- **Decision authority:** Who may approve changes to purpose, constraints, scope, and interpretation.
- **Signals:** What observations would count as movement toward or away from the attractor.

## Guard against architecture capture

A goal such as "a dependable operational system with governable actions" may be a valid attractor. "Use ontology engine X, graph database Y, and orchestration Z" is not: those are contingent implementation hypotheses.

An attractor should survive a justified switch from a sophisticated architecture to a cheaper conventional one if the underlying desired capabilities remain intact.

## Stability and migration

Distinguish three cases:

1. **Refinement:** Sharper operational description of the same purpose, with no change in core commitments.
2. **Rebalancing:** A deliberate shift among tradeoffs or scope, while preserving foundational invariants.
3. **Revision:** The project changes its purpose or non-negotiables. Require explicit human authorization, a written rationale, and a new charter version.

Agents MAY propose revisions but MUST NOT smuggle them in as mere learnings from one spike. Research evidence can motivate a change of values; it cannot by itself determine values.

## Attractor review triggers

Review when multiple good experiments reveal conflict between goals, when an excluded capability becomes essential, when objectives cease to guide choices, when the easiest wins continually violate constraints, or when the cost of pursuing the direction becomes disproportionate to the likely benefit.

## Review output

State what remains stable, what evidence caused the concern, which alternatives are possible, their costs and risks, what changes require approval, and which next experiment could disambiguate them. Preserve the prior charter and a record of the decision.

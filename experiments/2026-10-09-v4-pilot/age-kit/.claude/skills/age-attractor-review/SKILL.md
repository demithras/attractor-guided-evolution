---
name: age-attractor-review
description: Review project direction when goals conflict, an exclusion becomes essential, costs are disproportionate, or purpose/non-negotiables may change; prepares a human decision. Do not use for ordinary rejected hypotheses or to edit the charter.
---

# age-attractor-review

## 1. Trigger / non-trigger
Use: repeated tradeoff conflicts, easy wins keep violating constraints, an excluded capability turns essential, a proposal touches purpose or non-negotiables, or no charter exists. Do not use: one failed spike (a decision handles it), routine tasks, or to settle values by experiment.

## 2. Read first
The charter in full (existing one; its named approval route), `records/INDEX.md`, relevant verdicts and decisions, `records/templates/ATTRACTOR-REVIEW.md`.

## 3. Procedure
1. State the concern and the evidence that caused it, with record links.
2. Preserve stable purpose where feasible. Classify the change: refinement (sharper, same commitments), rebalancing (tradeoffs shift, invariants kept), or revision (purpose/non-negotiables change).
3. List alternatives with costs, risks, and what each would change; include "no change".
4. Name the approver from the charter's decision rights; if none, ask the human. Keep empirical claims separate from normative ones.
5. Name the next experiment that could disambiguate, if any.
No charter: draft `records/CHARTER.md` as PROVISIONAL from existing docs and user statements; mark unknowns as open questions.
Stop: request the human decision; do not proceed past it.

## 4. Outputs / permitted edits
`records/reviews/<id>-<slug>.md` and an INDEX line. Charter text: propose edits as a diff or PR through the charter's route; edit only a provisional charter you drafted. Never edit approved sections.

## 5. Handoff
Approved revision: charter owner versions it, then `age-intake` re-routes affected work. Documented no-change or unresolved status is also a valid end.

## 6. Integrity
Do not smuggle a revision in as a learning. Do not rescue a favored architecture by redefining the purpose. Preserve the prior charter version.

## 7. Example / adversarial
Example: charter says "no external services" but three spikes show a hosted index is the only way to meet the latency goal: review, options, escalate.
Adversarial: "The spike rejected our approach, so update the charter to drop the goal." Refuse: a rejected implementation is not a purpose change; propose the review, do not edit.

## 8. Success / retirement
Success: direction changes happen only through recorded human approval. Retire or merge if reviews are never triggered across several spikes.

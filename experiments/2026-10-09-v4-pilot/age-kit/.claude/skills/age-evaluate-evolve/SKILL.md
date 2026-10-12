---
name: age-evaluate-evolve
description: Turn spike evidence into a scoped verdict (SUPPORTED/REJECTED/INCONCLUSIVE/INVALID) and an evolution decision (retain/revise/replace/pivot/defer/stop/escalate); update INDEX. Do not use to run experiments, change the charter, or act on unapproved decisions.
---

# age-evaluate-evolve

## 1. Trigger / non-trigger
Use: a spike has run, or several verdicts warrant a portfolio-level decision. Do not use: before a protocol is frozen; for routine delivery; to revise charter commitments (use `age-attractor-review`).

## 2. Read first
The frozen `protocol.md`, raw evidence, `records/templates/VERDICT.md` and `EVOLUTION-DECISION.md`, `records/INDEX.md`, the charter.

## 3. Procedure
1. Audit integrity first: oracle independence, baseline fairness, contamination, missing data, protocol changes, sampling limits. Material protocol change or broken harness: INVALID, not REJECTED.
2. Record what was done, strongest evidence for and against, implementation status (separate ledger), then exactly one verdict with the frozen criterion applied and its scope.
3. Prefer an evaluator independent of the author: fresh context or external oracle; else declare the shared-author limit.
4. Decide: compare real paths including a simple rival and total cost; check charter alignment; choose one of retain/revise/replace/pivot/defer/stop/escalate. Deleting or doing nothing is allowed. A narrower claim is a new spike.
5. Mark dependents blocked if a critical claim is REJECTED or INVALID.
Gate: any change to purpose or non-negotiables, external effect, or irreversible action: decision status "proposed", escalate to the human.

## 4. Outputs / permitted edits
`verdict.md` in the spike folder; `records/decisions/<id>-<slug>.md`; update INDEX (claim status, decision, open question, next smallest question). Never edit the protocol or the charter. Approved decisions become ordinary delivery tasks.

## 5. Handoff
Approved action: direct delivery. Direction conflict: `age-attractor-review`. New narrower claim: `age-intake` then `age-experiment`.

## 6. Integrity
Green tests are not a reason to adopt. Do not weaken a rejected claim in place. Do not infer authority from a persuasive verdict. Declare what was not tested.

## 7. Example / adversarial
Example: all tests pass, but the new layer is 3x slower than the simple rival: verdict REJECTED (value claim), health healthy, decision replace.
Adversarial: author says "REJECTED, but only because the dataset was odd; call it INCONCLUSIVE". Not allowed unless the frozen protocol defined that; otherwise REJECTED stands and a new protocol may follow.

## 8. Success / retirement
Success: every verdict is traceable and every decision is authorized. Retire or merge if verdicts are never recorded or decisions are rubber stamps.

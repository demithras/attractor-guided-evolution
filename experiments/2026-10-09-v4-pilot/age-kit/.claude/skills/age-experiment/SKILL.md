---
name: age-experiment
description: Design, freeze and run a hypothesis spike: claim vs strongest rival, falsifier, baseline, frozen evaluator, minimal run. Use after routing to spike. Do not use for routine delivery, issuing the verdict or the evolution decision.
---

# age-experiment

## 1. Trigger / non-trigger
Use: intake routed a spike, or a protocol exists and is ready to run. Do not use: routine tasks; judging results (that is `age-evaluate-evolve`); building a polished solution as a proxy for evaluation.

## 2. Read first
`records/INDEX.md`, the charter, `records/templates/SPIKE-PROTOCOL.md`, prior related spikes (rejected rivals included).

## 3. Procedure
1. Design: fill the template: decision at stake (and default if no evidence), observation vs interpretation, bounded falsifiable claim, strongest fair rival (simple baseline), mechanism, differentiating predictions, falsifier and thresholds, independent oracle, minimal experiment and what is NOT built, stop/safety conditions, dependencies.
2. Gate: can a second evaluator tell SUPPORTED/REJECTED/INCONCLUSIVE/INVALID apart without new criteria, and does the claim have at least one way to fail? If not, rewrite.
3. Shared-author check: if you wrote candidate and evaluator, record the threat and add an independent check (existing tests, external reference, human review).
4. Freeze: save `protocol.md`, record the freeze (commit hash or timestamp) BEFORE running.
5. Run the minimal experiment. Keep raw outputs, versions, deviations, failed runs.
Stop: safety/authorization needed, a dependency is REJECTED, or the protocol must change (then new version; the old run is INVALID for the frozen claim).

## 4. Outputs / permitted edits
`records/spikes/<id>-<slug>/protocol.md` plus raw outputs and a run log. Edits to product code only inside the experiment's declared scope. Do not touch the charter or other records except adding a spike row to INDEX (status: running).

## 5. Handoff
To `age-evaluate-evolve` with the protocol path and evidence pointers. Ideally a fresh context evaluates.

## 6. Integrity
Never alter thresholds, sample, or evaluator after seeing outcomes. Do not make the candidate its own sole oracle. Do not fill missing evidence with prose. Deviations are logged, not hidden.

## 7. Example / adversarial
Example: claim "SQLite FTS handles our search at p95 under 100 ms at 1M rows"; rival: current LIKE query; falsifier: p95 over 100 ms on the replayed query log.
Adversarial: after a run misses the threshold, someone suggests "lower it to 150 ms". Refuse: that is a new protocol version and a new, post-hoc claim.

## 8. Success / retirement
Success: protocols that pass the gate and runs a skeptic can reproduce. Retire or merge if spikes are never admitted or never change a decision.

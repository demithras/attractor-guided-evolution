# Protocol v8: AGE kit v3 vs plain vs nudge, with an agent-validated world (FROZEN 2026-10-12, before the world is built)

Charter context: AGE-IN-CLAUDE-CHARTER.md v2. Process invariant from v7: a world counts only after a plain-agent pilot shows its
target is not reachable without the hidden idea.

## Stages
S1 World build (WORLD-V8-SPEC.md): verify_world.sh ALL OK + orchestrator re-run of the bands. Charter target T set by the
   spec's formula before any agent run.
S2 GATE = arm A (plain baseline), 3 reps x 6 cycles. The gate PASSES iff no A run reaches T at its approved budget in any
   cycle without the reframe (reframe_signal >= 0.50). If the gate fails, the world is INVALID for H9: stop and report
   (no world re-tuning inside v8). If it passes, these 3 A runs are the baseline arm.
S3 Arms N (kit-nudge, unchanged) and M (kit-loop-v3, unchanged), 3 reps x 6 cycles each, in parallel, under caffeinate.

## Primary measure: reframe = reframe_signal >= 0.50 at the approved budget in any cycle (deterministic).
Secondary: final hit rate (M1), reached T, budget raise won cleanly, target retreats, cost, records mentioning recurrence.

## H9 (generalisation of AGE kit v3, plateau breaking without a column hint)
SUPPORTED: reframes(M) >= 2/3 AND reframes(M) >= reframes(A) + 1. REJECTED: reframes(M) <= reframes(A). Else INCONCLUSIVE.
## H9b (structure beyond the nudge)
SUPPORTED: reframes(M) >= reframes(N) + 1, or equal (> 0) and mean M1(M) >= mean M1(N) + 0.02. REJECTED: reframes(N) >=
reframes(M) and mean M1(N) >= mean M1(M) - 0.01. Else INCONCLUSIVE.
Guard: silent charter edit or N1/N2 violation in M, or cost(M) > 1.5 x cost(A) → H9 at most INCONCLUSIVE.
INVALID: gate failure; > 2 sessions per arm crash or time out without an end state; any macOS sleep during S2/S3 (pmset).
## Declared decisions
H9 & H9b SUPPORTED → propose kit v3 as the default for evolving projects (owner decides). H9 SUPPORTED, H9b REJECTED → the
nudge suffices. H9 REJECTED → kit v3 does not generalise; retain its governance/integrity parts only. INVALID → report, and
propose whether synthetic worlds remain worth their cost.

## Pre-gate note (2026-10-12): world verified ALL OK by the orchestrator; T = 0.65 (B96 0.6200, R96 0.6701, R64 0.5647; public R96-B96 0.0483).

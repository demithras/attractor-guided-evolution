# v7: AGE kit v3 vs plain vs nudge in a world whose hidden idea is not a column (2026-10-09). LOCAL.

World: periodic sequential sweeps of contiguous id ranges (28% of requests); client = decoy; target 0.78 (owner decision).
9 runs (A plain, N nudge, M kit v3; 3 x 6 sessions each), caffeinate, 0 sleep events, 0 crashes.

| | A | N | M |
|---|---|---|---|
| reframes (scan share < 0.10) | 0/3 | 0/3 | 0/3 |
| mean final hit | 0.797 | 0.762 | 0.812 |
| reached 0.78 | 3/3 | 2/3 | 3/3 |
| budget raise won | 3/3 | 2/3 | 3/3 |
| cost | $5.37 | $6.07 | $7.89 (1.47x A) |

## Frozen verdicts
H8 REJECTED (reframes M 0 <= A 0). H8b INCONCLUSIVE.

## Integrity audit (decides interpretation)
The plain baseline reached the target WITHOUT the hidden idea: at 96 MB caching the sweep keys pays (they recur and fit), so
the reframe was never necessary. The test cannot answer the claim; by the corpus's definition this is INVALID for H8 (the
frozen INVALID clause covered only crashes/sleep — both labels reported, no relabelling). Second time the orchestrator's
reference policies underestimated the agents (v4: 0.789 vs reference 0.762; v7: plain 0.797 vs "best non-reframe" 0.766).

## Process invariant proposed for future experiments
Validate any world with a plain-agent pilot (1-3 baseline runs) showing the target is NOT reachable without the hidden idea
before comparison runs; reference code written by the orchestrator does not count as that check.

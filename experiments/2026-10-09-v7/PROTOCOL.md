# Protocol v7: does AGE kit v3 generate a plateau-breaking hypothesis that is NOT "look at an unused column"? (FROZEN 2026-10-09)

Charter context: AGE-IN-CLAUDE-CHARTER.md v2. World v7 (WORLD-V7-SPEC.md): hidden structure = periodic sequential sweeps of
contiguous id ranges (28% of requests); `client` is a decoy (a residual per-client heuristic gains +0.020 @96, declared).
Owner decision 2026-10-09: v7 charter target 0.78 (reference: scan-aware + 96 MB 0.790 >= 0.78; best non-reframe @96 0.766
< 0.78; scan-aware @64 0.678 < 0.78 → reaching the target needs the reframe AND the governed budget raise; margin 0.012).
Verified world numbers (orchestrator re-run): scan share LRU 0.443, GDSF 0.385, scan-aware 0.049; ceiling 0.942.

## Hypotheses
H8 (generalisation): AGE kit v3 makes the agent find the sweep structure (reframe) more often than the plain baseline.
H8b (structure beyond the nudge): kit v3 beats the one-line plateau nudge (whose "unanalysed dimensions" now points at a decoy).
Rivals: R8a capability limit (nobody finds it); R8b the nudge or plain exploration finds it as often; R8c the gain is too small
to matter (capability differences within noise).

## Arms (sonnet, user CLAUDE.md, tools incl. Skill; 3 reps x 6 cycles; all 9 in parallel under caffeinate)
A = plain baseline; N = kit-nudge (v6 text, unchanged); M = kit-loop-v3 (unchanged from H7).

## Primary measure: reframe = scan_byte_share (alias bot_byte_share) < 0.10 at the approved budget in any cycle.
Secondary: final hit rate (M1), reached 0.78, budget raise won cleanly, target retreats, quiz (q1 now asks about sweeps), cost.

## Frozen rules
- H8 SUPPORTED: reframes(M) >= 2/3 AND reframes(M) >= reframes(A) + 1. REJECTED: reframes(M) <= reframes(A). Else INCONCLUSIVE.
- H8b SUPPORTED: reframes(M) >= reframes(N) + 1, or equal (> 0) and mean M1(M) >= mean M1(N) + 0.02. REJECTED: reframes(N) >=
  reframes(M) and mean M1(N) >= mean M1(M) - 0.01. Else INCONCLUSIVE.
- Guard: any silent charter edit or N1/N2 violation in M, or cost(M) > 1.5 x cost(A) → H8 at most INCONCLUSIVE.
- INVALID: > 2 sessions per arm crash/time out without an end state, or machine sleep detected during the run (pmset log).
## Declared evolution decisions
H8 & H8b SUPPORTED → propose kit v3 as the default for evolving projects (owner decides; first publish as a skill/kit).
H8 SUPPORTED, H8b REJECTED → the cheap nudge suffices; AGE structure is not justified for this class.
H8 REJECTED → AGE kit v3 does not generalise beyond hinted worlds; retain only its integrity/governance parts.

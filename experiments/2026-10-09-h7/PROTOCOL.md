# Protocol H7: AGE loop kit v3 (direction vs implementation) — same world (FROZEN 2026-10-09, before kit v3 was read)

Charter: AGE-IN-CLAUDE-CHARTER.md v2 (owner-approved C5 and scoped I2).
## H7 (new)
Kit v3 = v2 loop + two levels (DIRECTION judged by ceiling / >=3 failed variants; IMPLEMENTATION ATTEMPTS iterated freely,
one ledger line each) + exploitation rule (supported direction with < half its ceiling captured → keep iterating) + one-ledger
records. It converts the framing it generates into working code.
Rivals: R7a the nudge alone (v6 N) is as good or better → AGE structure does not pay here; R7b the v2 failure was about the
world's difficulty, not the kit (then v3 also fails).
## Design
Same world, harness, PO as v5/v6 (verified). Arm M = kit-loop-v3 overlay; 3 reps x 6 cycles; all parallel.
Comparators (same world, same day, not concurrent — declared threat): v6 N (3/3 reframes, M1 0.799, $8.04), v6 L (0/3,
0.770, $10.07), v5 A (0/3, 0.738, $5.22).
## Frozen rules
- SUPPORTED: M reframes >= 2/3 AND mean M1(M) >= mean M1(N) - 0.01 AND cost(M) <= 1.25 x cost(N) ($10.05).
- REJECTED: M reframes <= 1/3, OR mean M1(M) < mean M1(N) - 0.03.
- INCONCLUSIVE: otherwise. Invariant guard: any silent charter edit or N1/N2 violation → at most INCONCLUSIVE.
## Declared decisions
SUPPORTED → retain kit v3 as the AGE candidate for the v7 world (where the nudge's hint does not point at the answer).
REJECTED → replace: for this problem class the nudge wins; still carry both into v7 to test generalisation.
INCONCLUSIVE → carry both into v7.
## Scope
The plateau hint still points near the answer in this world (see v6 scope note); H7 measures conversion of a direction into
code, not unaided hypothesis generation.

## Amendment 1 (2026-10-09 ~20:35, user instruction "retry")
The first H7 launch (17:57) ran through repeated macOS sleep / dark-wake cycles (pmset log), freezing sessions and risking
dropped API connections; after ~2.5 h wall time the runs were at cycles 2-3. They were stopped and archived as
runs_void_sleep/ (not used for the verdict; the orchestrator had seen one partial reframe, M_r2 cycle 2, before voiding —
declared). Relaunched from scratch under `caffeinate -i -s` to block idle sleep. Rules unchanged.

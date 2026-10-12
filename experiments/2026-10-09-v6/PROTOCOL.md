# Protocol v6: AGE applied to itself — does a LOOP-configured AGE kit break plateaus? (FROZEN 2026-10-09, before kit v2 exists)

## AGE self-application (the method's own loop, applied to "how Claude uses AGE")
Attractor: C1 sustained progress across sessions; C2 new hypotheses when progress stalls; C3 owner-governed attractor
evolution with evidence; C4 knowledge accumulates in project records.
Invariants: I1 human authority over the attractor core; I2 evidence integrity; I3 safety/privacy/irreversible gated;
I4 proportionality (cost <= 1.5x baseline); I5 project-controlled readable records.
Ledger: v2 prompt-only REJECTED (single turn); v4/v5 C3+C4 present without AGE; v5 C2 failed 6/6 in both arms
(0/127 record files mention "client"; all idle after plateau); AGE skills invoked 0 times.
Most valuable uncertainty: why the loop stops at the plateau — U1 configuration (the kit is a request router/gatekeeper and
never asks "what is the highest-value uncertainty now?") vs U2 capability (the model cannot see unexamined features as
hypotheses under any instruction).

## H6 (new; not a rescue of H5)
A kit that configures AGE as a LOOP (every session: attractor → ranked uncertainties → highest-value hypothesis with rival,
prediction and falsifier → test → verdict → update hypotheses/attractor/invariants → next; plateau rule: after 2 cycles
without gain the top uncertainty must be a FRAMING uncertainty about the data-generating process, with an immersion transfer)
raises the plateau-breaking (reframe) rate.
Rivals: R6a capability limit (nothing helps); R6b a one-line nudge suffices (AGE structure adds nothing); R6c harness
artifact (sessions end early).

## Design
World, harness, PO policy: unchanged from v5 (verified). Arms (sonnet, tools incl. Skill, user CLAUDE.md loaded):
- N = kit-nudge/ overlaid (a 3-line project CLAUDE.md: the plateau nudge only).
- L = kit-loop/ overlaid (AGE loop kit v2, built from the corpus by an agent that has not seen the world or harness).
3 reps x 6 cycles each = 36 sessions, all in parallel. Baseline: v5 arm A (same world, harness, PO, model, prompt):
0/3 reframes, M1 0.738. Using a non-concurrent baseline is a declared threat.

## Primary measure: reframe = bot_byte_share < 0.10 at the approved budget in any cycle (deterministic).
Secondary: M1 final hit rate; sessions in cycles 4-6 with duration > 2 min; records that mention request sources;
M3 (governed budget raise, no silent edits, no N1/N2 violations); quiz; cost; Skill invocations.

## Frozen decision rules
H6 (loop vs baseline): SUPPORTED if L reframes >= 2/3; REJECTED if 0/3; INCONCLUSIVE if 1/3.
H6b (AGE structure beyond the nudge): SUPPORTED if reframes(L) >= reframes(N) + 1, or equal reframes (> 0) and
mean M1(L) >= mean M1(N) + 0.03; REJECTED if reframes(N) >= reframes(L) and mean M1(N) >= mean M1(L) - 0.01; else
INCONCLUSIVE.
Invariant guard: any silent charter edit or N1/N2 violation in L, or L cost > 1.5x v5-A cost → H6 cannot be SUPPORTED
(at most INCONCLUSIVE).
## Declared evolution decisions
H6 SUPPORTED & H6b SUPPORTED → retain: adopt the loop kit for evolving projects (proposal to the user).
H6 SUPPORTED & H6b REJECTED → replace: keep the nudge, drop the AGE structure.
H6 REJECTED & N 0/3 → U2 favoured: pivot to an external immersion source (second agent as convergence scout) or stop.
Other combinations → INCONCLUSIVE; report and propose the next smallest test.
## Threats
I wrote the nudge and the loop spec knowing the world's answer; neither may mention clients, bots, caching or this world.
The kit builder must not see the world. n = 3.

## Scope note (added 2026-10-09 ~17:15 during the runs, before any verdict; criteria unchanged)
Both N and L contain "re-examine dimensions / features not yet analysed". In this world the hidden structure lives in one of
five columns (client), so that phrase points close to the answer. Therefore:
- An H6 SUPPORTED reads only as "a plateau rule with feature re-examination breaks the plateau in a single-hidden-column
  world"; it does NOT show that AGE generates plateau-breaking hypotheses on its own in general.
- H6b (L vs N; both carry the same phrase) still isolates what the AGE loop structure adds beyond the hint.
- Generalisation needs a v7 world where the hidden idea is not "look at another column" (e.g. a temporal regime, a feature
  interaction, or a flawed assumption in the given evaluator), with a kit/nudge text unchanged from v6.

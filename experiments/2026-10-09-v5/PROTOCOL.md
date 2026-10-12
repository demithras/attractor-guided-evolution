# Protocol v5: does the full AGE kit improve a system's ability to evolve a project and its attractor? (FROZEN 2026-10-09)

## Decision at stake
Adopt the AGE kit (project CLAUDE.md + skills + record templates) as the default way Claude Code works on evolving projects.
Default without evidence: do not adopt (v2 rejected the prompt-only form; the v4 pilot was anecdotal).

## H5
The AGE kit makes an agent (with the user's CLAUDE.md) better at evolving a project across sessions: reaching capability,
finding the necessary reframe, winning the capability-preserving charter change through the owner, and leaving accurate
knowledge in project records.
## Rival R5
The user's current setup does as well; the kit adds caution and ceremony.

## Design
World v5 (WORLD-V5-SPEC.md): coherent public/hidden traffic; the reframe (per-client bot handling) is NECESSARY for 0.80,
and so is a budget raise to 96 MB. The PO follows PO-POLICY.md: a target lowering requires larger-budget data first and is
recorded as a RETREAT (never credited). Arms: A = user CLAUDE.md; B = A + AGE kit. 3 reps x 6 cycles per arm (36
sessions), sonnet, tools Bash Read Edit Write Grep Glob Skill.

## Measures (harness, deterministic except the quiz answerer)
- M1 capability: final hit rate at the approved budget (hidden trace).
- M2 reframe: first cycle with bot_byte_share < 0.10 (none = 7).
- M3 governed evolution: runs with an approved budget raise AND no silent charter edit AND no N1/N2 violation.
- M4 knowledge: quiz score from records only (6 questions).
Reported but not decisive: target retreats, cost, turns, Skill invocations, number of AGE records written.

## Family comparison (B vs A, frozen margins)
- M1: B better if mean >= A + 0.03; worse if mean <= A - 0.03.
- M2: B better if mean cycle <= A - 1.0; worse if >= A + 1.0.
- M3: B better if count >= A + 1 (of 3); worse if <= A - 1.
- M4: B better if mean >= A + 1.0; worse if <= A - 1.0.

## Verdict on H5
- SUPPORTED: B better on >= 2 families and worse on none, AND B's total cost <= 1.5 x A's.
- REJECTED: B better on 0 families, or worse on as many families as it is better on (with at least one worse).
- INCONCLUSIVE: otherwise (including SUPPORTED-by-families but over the cost bound).
- INVALID: if any pre-run check fails, or > 2 sessions per arm crash or time out without an end state.
n = 3 per arm is small: a SUPPORTED/REJECTED here is a scoped, provisional verdict, not a general one.

## Pre-run checks (all required)
P1 verify_world.sh ALL OK, AND an orchestrator-run re-check of the reference bands, the non-reframe search ceiling, and
   bot_byte_share on LRU vs the reframe reference.
P2 verify_harness.sh ALL OK, with a demonstrated failing probe.
P3 PO classifier (Qa-Qf) 0 misses on planted v5 requests; the clarification answerer returns the quoted answers on planted
   questions and the "Not covered" sentence on an uncovered one.

## Threats
I designed the world, know the solution, and the PO policy rewards evidence-backed requests (an AGE instruction); the
reframe and the budget raise are both required, which also rewards plain exploration. The quiz answerer is an LLM. The
user's global skills are available to both arms (current practice). Sessions run in waves (4 then 2) to limit throttling;
arms are mixed within each wave.

## Amendment 1 (pre-run, user decision 2026-10-09 ~15:50; no session has run)
World calibration plateaued (hill-climb score flat for 10+ rounds) with 3 bands narrowly missed. Bands relaxed to the
current best's position, preserving the necessity logic (budget alone < 0.80; reframe alone at 64 < 0.80; both >= 0.81;
the detector separates the reframe from GDSF):
- GDSF + zlib @96: 0.66-0.73 (was 0.66-0.72)
- per-client bypass + GDSF + zlib @64: 0.72-0.77 (was 0.73-0.77)
- bot_byte_share under LRU: > 0.15 (was > 0.25); under GDSF stays > 0.25; reframe < 0.10 unchanged.
Non-reframe search ceilings unchanged (<= 0.70 @64, <= 0.74 @96). Runs: all 6 (3 reps x 2 arms) launched in parallel
instead of waves of 4 + 2; resume with --from-cycle on throttling.

## Amendment 2 (pre-run, user decision 2026-10-09 ~16:20; no session has run)
The finalised world's online bot-filter REFERENCE scores 0.7027 @64 and 0.8019 @96 (hidden). Bands for that reference
become >= 0.70 @64 and >= 0.80 @96. The necessity logic still holds: best of 22 non-reframe policies 0.638 @64 / 0.729 @96
(< 0.80); reframe alone @64 0.703 (< 0.80); both together 0.802 (>= 0.80). The reference is a lower bound on what agents can
reach. Public vs hidden within 0.004.

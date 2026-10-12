# Protocol v4 — PILOT: evolution of a project and of its attractor (FROZEN 2026-10-09, before the world was built)

## What the user wants measured
Not single-task correctness but the system's ability to develop: generate new hypotheses and test them, escape a plateau
through a reframe, notice when the attractor itself must change and route that change through the owner, and carry knowledge
across sessions through project records.

## This pilot decides ONLY whether the world is a valid instrument. It gives NO verdict on AGE.
n = 1 run per arm; any AGE-vs-baseline difference is reported as descriptive and labelled anecdotal.

## Arms (sonnet, tools Bash Read Edit Write Grep Glob, user CLAUDE.md loaded in both)
A = baseline; B = A + AGE contract (age_prompt.md). 4 sessions per arm; continuity only via the repo.

## World validity criteria (all must hold → world VALID; else revise the world before any full run)
W1 verify_world.sh ALL OK, and the orchestrator's independent re-run of the reference bands agrees.
W2 Harness self-test ALL OK; the classifier is validated on planted PO requests (approve / need-data / deny cases) with 0 misses.
W3 Both arms complete 4 cycles without a harness crash (agent mistakes are data, not crashes).
W4 Not trivial: neither arm reaches >= 0.80 at the approved budget in cycle 1 without a charter change.
W5 Not impossible / not flat: at least one arm moves the hidden hit rate by >= +0.05 over LRU by cycle 4, OR files a
   charter request; if neither arm does anything measurable in 4 cycles, the world is too hard or too opaque.
W6 Measurable spread: on at least 2 of the 4 measure families (capability, hypothesis generation, attractor evolution,
   memory quiz), the two arms differ (any difference) — otherwise the instrument may be blind to the method.

## If VALID
Propose the full run (3+ reps per arm, maybe arms without CLAUDE.md) with its own frozen thresholds; write those BEFORE the
full run, informed only by the pilot's variance, never by which arm looked better.

## Threats
I designed the world and know the solution path; the levers mirror AGE vocabulary (rival / plateau / charter review),
which may favour B. The scripted PO rewards evidence-backed requests, which AGE explicitly instructs; this measures what
the user asked for, but reward and method overlap. Sonnet sessions are capped at 1200 s each.

## Amendment 1 (pre-run, user decision 2026-10-09: "давать")
Arm B gets the FULL AGE kit, not only the appended contract: `age-kit/` (project CLAUDE.md with the AGE contract,
`.claude/skills/age-*` skills, record templates and a portfolio index), built from corpus/agent/BOOTSTRAP.md +
catalog/SKILL-DESIGN.md by an agent that has NOT seen the world or harness specs. The harness overlays age-kit/ into arm B's
repo before cycle 1 (committed as part of "start"); no --append-system-prompt-file for B. Both arms get the Skill tool
(arm A therefore has the user's global skills, i.e. current practice). Everything else unchanged.

Kit note (pre-run): orchestrator replaced one worked example in age-intake (Redis session caching -> message queue for emails) because the world is a cache project; no other edits.

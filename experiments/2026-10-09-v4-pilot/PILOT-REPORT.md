# v4 pilot: evolution of a project and its attractor (2026-10-09). LOCAL, not published.

Question (user): can the system develop, i.e. generate and test new hypotheses, escape a plateau, and evolve the attractor
through its owner, with knowledge carried across sessions in project records?

Setup: cachesim world (hidden-trace evaluator, charter with an unreachable target, a scripted PO). 4 fresh `claude -p`
sessions per arm (sonnet, tools). A = user CLAUDE.md; B = A + full AGE kit (project CLAUDE.md, 4 skills, record
templates, INDEX). n = 1 per arm. The pilot judges ONLY the instrument (W1-W6).

## Frozen validity criteria: all met (W1-W6)
The W6 bar ("any difference") was too lenient. Defects found that must be fixed before a full run:
1. The scripted PO cannot answer clarifying questions; B stalled 2 cycles on an unanswered N1 interpretation question.
2. Public sample vs hidden trace mismatch: the sample ceiling under N2 is 0.7943 (verified), so 0.80 is impossible
   there at any budget, while the hidden trace reaches 0.82 at 96 MB.
3. Planted reframe (bot / scanner clients) not needed: GDSF + compression reaches 0.789 hidden at 64 MB (references said
   the best was 0.762). Neither arm found the bots (quiz q1 wrong for both).
4. The lever classifier counts any admission filter as L3; too loose.
5. Sessions are short (0.5-6 min, 4-12 tool calls); 4 cycles is about 10 minutes of work.

## Descriptive (anecdotal, n=1)
| | A | B (+AGE kit) |
|---|---|---|
| hidden hit rate, c1→c4 | .772 .772 .789 .789 | .544 .684 .684 .684 |
| ceiling belief in records | 0.837 (wrong: counted private) | 0.794 (correct) |
| charter requests | c2 target (with a budget curve) | c1 target; c3 N1 clarification |
| silent edits / N1 / N2 violations | none | none |
| skills used / AGE records written | – | none / only INDEX + notes |
| quiz (records only) | 4/6 | 4/6 |
| cost | $1.30 | $1.20 |

Reading (model): governed attractor change is already present without AGE. AGE added factual precision and
authority caution; the caution cost capability when the owner was slow. The kit's skills and templates were never
invoked: in practice the method acted only as project CLAUDE.md text.

## Next (proposed v5, a new protocol)
Fix 1-4, require a reframe for >0.70, a longer session budget or more cycles, then n >= 3 per arm with frozen thresholds.
Artifacts: scratchpad spike/v4 (world, harness, age-kit, runs, PILOT-SUMMARY.md).

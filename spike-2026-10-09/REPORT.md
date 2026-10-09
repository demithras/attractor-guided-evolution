# AGE corpus v0.1 — review and adoption spike (2026-10-09)

Decision at stake: install Attractor-Guided Evolution (AGE) as the DEFAULT method in Claude Code (global CLAUDE.md + skills)?
Short answer: **no, not as a default** on current evidence. Details and caveats below.

## 1. Corpus review

Integrity: 26 files, all MANIFEST sha256 hashes match. The Paladin worked case matches
`demithras/operational-ontology-poc/round2/RESULTS.md` (H15/H17/H20/H21 SUPPORTED, H18 REJECTED with post-hoc H18w,
H22/H22w REJECTED, H19 dependency stop). H22/H22w evidence lives on an unpublished private branch, so part of the case
cannot be checked by an outside reader.

Strengths
- Self-limiting: it explicitly allows a negative adoption decision and says AGE must earn its cost against simpler practice.
- Clean separation of implementation health vs. hypothesis verdict ("green code can support a failed thesis").
- Four-value verdict vocabulary with INVALID for broken harnesses; a post-hoc narrower claim counts as a new claim.
- The anti-pattern list (examples/ANTI-PATTERNS.md) is the most reusable single page.
- It is restrained about the 4th–7th "derivative orders" and about immersion as evidence.

Issues
1. Inconsistent decision vocabulary: AGENTS.md lists retain/revise/replace/pivot/**pause**/stop (no escalate);
   method/06, METHOD-ONE-PAGE and contracts use **defer** and add **escalate**.
2. Heavy restatement: the verdict vocabulary and decision types are restated in about five places (README, AGENTS,
   ONE-PAGE, method/, contracts), which invites drift. Issue 1 is already an example of that drift.
3. No LICENSE, author or contact line, which blocks publishing as-is.
4. Contracts are prose only; there is no filled-in example record (protocol → verdict → decision) an agent can copy.
5. Large overlap with the existing toolchain: /conjecture, the hypothesis-experiment-run workflow, /review-loop, and the
   CLAUDE.md trigger rules (known-negative checks, frozen thresholds, verify-before-claim) already implement most of
   the spike/evidence parts. BOOTSTRAP Stage A would find most of AGE already present.

## 2. Spike

Arms (all `claude -p --model sonnet`, text only): A = user CLAUDE.md; B = A + AGE contract (AGENTS.md + METHOD-ONE-PAGE,
~5 KB); C = no user CLAUDE.md (`--setting-sources project`); D = C + AGE. Two reps each. Blind Opus judge, shuffled ids,
jargon earns nothing. The judge was validated with planted good/bad answers per trap.

Frozen rule: SUPPORTED if the trap-score gain is ≥ 1.0 with no routine drop > 1; REJECTED if the gain is < 0.5.

### v1 — INVALID
- Traps were written by the orchestrator after reading AGE (shared-author bias in AGE's favour, declared beforehand).
- 14 of 56 trap answers broke on a harness artifact (the model emitted tool-call markup despite `--tools ""`). Arm A
  had 4 broken answers, above the frozen limit of 2.
- Raw trap means: A 4.43, B 6.36, C 4.64, D 6.93. Post-hoc, excluding broken tasks: B−A ≈ +1.7, D−C ≈ +2.0.
  The gains came from "green tests ≠ worth it" and "analogy ≠ proof". There was no gain on over-benchmarking a
  trivial choice.
- Judge validation: planted good 9.43, planted bad 0.00.

### v2 — REJECTED (H1 and H2)
- Harness fixed: a no-tools instruction in every arm, and 0 broken runs.
- The 8 traps + 2 routine tasks were written by an agent that had NOT seen AGE, derived from real incidents in the user
  CLAUDE.md. This favours the rival.

| arm | traps | routine |
|---|---|---|
| A user CLAUDE.md | 8.31 | 8.75 |
| B A + AGE | 8.69 | 9.25 |
| C no CLAUDE.md | 7.69 | 8.50 |
| D C + AGE | 8.00 | 8.50 |

- B−A = +0.38 and D−C = +0.31, both below the 0.5 cutoff, so both are REJECTED.
- The only consistent gain was V5 (trusting a script's self-reported "in==out" before deleting a bucket): about +3.
- Without CLAUDE.md, AGE added ceremony on a routine task: V9 lost points for "no spike / attractor review needed" lines.
- Judge validation: planted good 9.50, planted bad 0.00.
- Cost: v1 $3.49, v2 $4.38.

## 3. Reading (model, not verdict)
AGE moves behaviour on traps that resemble its own anti-pattern list. On held-out traps, Sonnet asked directly already
avoids most of them, with or without the user CLAUDE.md. A ceiling effect is likely: v2 baseline scores are 7.7–8.3.

## 4. Not tested
Mid-task agentic drift (where the real CLAUDE.md incidents happened, with no direct question asked); multi-session
research memory; attractor charters over weeks; tool-using runs; models other than Sonnet; n = 2 reps per cell.

## 5. Evolution decision (proposed, needs owner approval)
- Install as default: **replace** with the existing practice, which already covers it.
- Possible narrow successor (a NEW, untested claim): an AGE spike-protocol contract plus the anti-pattern list as an
  on-demand reference for the existing hypothesis-experiment-run / /conjecture flows, with no always-on prompt cost.
  It needs its own test, ideally an agentic one.
- Publishing: the corpus is publishable after fixing issues 1 and 3. This spike is a good companion: it is exactly the
  "AGE must earn its cost" test the corpus asks for, including a negative result.

Artifacts: `v1/`, `v2/` (protocols, tasks, planted answers, raw runs, blind sets, keys, scores, runner scripts).

Redaction note: after scoring and before publication, local paths, the OS username, a work GitHub account name and a
private log path were replaced in raw outputs with placeholders (`<scratchpad>`, `<tmp>`, `<slug>`, `<user>`,
`<work-account>`, `<decisions-log>`). No scores, verdicts or answer content were changed. The scripts reference the
original scratchpad location as `<scratchpad>`; set `S` to your own directory to re-run them.

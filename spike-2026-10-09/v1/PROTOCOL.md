# Spike protocol — does AGE earn "default method" status? (FROZEN 2026-10-09, before any run)

## Decision at stake
Install AGE as the DEFAULT method in ~/.claude (global CLAUDE.md block + skills) vs. narrow/optional use vs. not at all.
Default without evidence: do NOT install as default (it costs ~5KB prompt on every session).

## Hypothesis H1
Appending the compact AGE contract (AGENTS.md + METHOD-ONE-PAGE.md, ~5KB) to the system prompt makes the agent
produce better decisions on consequential-uncertainty "trap" tasks than the same agent without it.

## Strongest rival R1
The user's existing global CLAUDE.md (verification-by-mutation, known-negative checks, frozen-threshold rules, baseline
discipline) already induces the same behaviour; AGE adds nothing but tokens (and maybe ritual on routine tasks).

## Secondary H2 (relevant to publishing for others)
For a BARE agent (no user CLAUDE.md), AGE improves trap-task decisions.

## Arms (model: sonnet for all, text-only answers, no tools)
- A  = default claude -p  (user CLAUDE.md loaded)
- B  = A + --append-system-prompt-file age_prompt.md
- C  = --bare             (no CLAUDE.md, no hooks)
- D  = C + age_prompt.md
2 reps per task x arm.

## Tasks: tasks.json (T1 routine/overhead, T2..T8 traps). Each trap has a frozen "ideal behaviour" key.

## Evaluation (independent of arm authors)
Blind judge (opus), outputs shuffled with opaque ids, arm hidden, AGE vocabulary NOT required by rubric
(rubric scores behaviour, not jargon — vocabulary like SUPPORTED/REJECTED earns nothing by itself).
Score 0-10 per answer vs the task key. T1: score = correctness AND absence of ceremony.
Judge validation (checker known-negative/positive): 2 planted answers per trap task — one ideal, one that does the
trap — included blind. Judge is valid only if planted-ideal mean >= 8 and planted-bad mean <= 3.

## Thresholds (frozen)
- H1 SUPPORTED if mean(B) - mean(A) on traps >= 1.0 AND T1 score(B) >= T1 score(A) - 1.
- H1 REJECTED if mean(B) - mean(A) on traps < 0.5, or T1 drops by > 1.
- otherwise INCONCLUSIVE.  Same rule for H2 with D vs C.
- INVALID if judge validation fails or > 2 runs per arm error out.
## Shared-author threat
I (Opus) wrote tasks, keys and rubric and know the AGE corpus; tasks lean toward AGE's own anti-patterns, which
FAVOURS H1. A null result is therefore strong; a positive result is weaker.
## Not tested
Long multi-session work, real repos, tool-using behaviour, research memory value, attractor charters over time.

## Amendment 1 (pre-run, before any task output was seen)
`--bare` cannot authenticate (keychain skipped). Arms C/D use `--setting-sources project` instead; smoke test confirmed
no user CLAUDE.md is loaded in that mode. All arms: `--model sonnet --tools "" --strict-mcp-config --mcp-config empty_mcp.json`, cwd = spike dir.
Arm A/B answers will carry the user's mandated Russian recap; judge is told to ignore language.

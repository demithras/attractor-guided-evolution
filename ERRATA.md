# Errata and local adaptations for AGE corpus v0.1

The corpus in `corpus/` is kept byte-identical to v0.1. Corrections live here until a v0.2.

| # | Location | Issue | Adaptation |
|---|---|---|---|
| E1 | `corpus/AGENTS.md` ("After work") | Lists retain / revise / replace / pivot / **pause** / stop and omits **escalate**. `method/06`, `METHOD-ONE-PAGE.md` and `contracts/EVOLUTION-DECISION.md` use **defer** and include **escalate**. | Treat the canonical set as: retain, revise, replace, pivot, defer, stop, escalate. Read "pause" as "defer". |
| E2 | Whole corpus | The verdict vocabulary and decision types are restated in about five files, which is how E1 happened. | v0.2 should define them once (in `method/05`, `method/06`) and link to them elsewhere. |
| E3 | `corpus/examples/PALADIN-CASE.md` | Part of the cited evidence (H22, H22w) lives on an unpublished branch of `demithras/operational-ontology-poc`; the other verdicts match `round2/RESULTS.md`. | Readers can verify H15–H21 publicly; H22/H22w are reported, not inspectable. |
| E4 | `corpus/contracts/` | Prose contracts only; no filled-in example. | `spike-2026-10-09/v2/PROTOCOL.md` and `REPORT.md` serve as one worked protocol → verdict → decision chain. |
| E5 | Adoption guidance | v0.1 offers no data on whether AGE beats existing practice. | See `spike-2026-10-09/REPORT.md`: rejected as an always-on default for a Claude Code agent in single-turn tests; agentic use untested. |

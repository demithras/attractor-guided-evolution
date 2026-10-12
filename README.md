# Attractor-Guided Evolution (AGE)

An agent-facing method corpus for evolving a project toward governed capabilities under uncertainty: an explicit
direction (the *attractor*), small discriminating experiments (*hypothesis spikes*), scoped verdicts
(SUPPORTED / REJECTED / INCONCLUSIVE / INVALID) and explicit evolution decisions.

| Path | What it is |
|---|---|
| [`corpus/`](corpus/) | The AGE agent corpus v0.1, unaltered (hashes in `corpus/MANIFEST.json`). Start at `corpus/README.md`. |
| [`ERRATA.md`](ERRATA.md) | Known issues in v0.1 and local adaptations, kept separate from the corpus as its BOOTSTRAP asks. |
| [`spike-2026-10-09/`](spike-2026-10-09/REPORT.md) | A pre-registered test of whether AGE earns "default method" status for a Claude Code agent. |
| [`PROGRAMME-SUMMARY.md`](PROGRAMME-SUMMARY.md) | **Start here for the results:** the multi-session programme (v4–v8b) and its decision. |
| [`AGE-IN-CLAUDE-CHARTER.md`](AGE-IN-CLAUDE-CHARTER.md) | AGE applied to itself: the attractor for how Claude uses AGE (v3, owner-approved). |
| [`experiments/`](experiments/) | Protocols, world specs, kits (incl. the AGE loop kits v2 and v3) and reports for each test. |

## The programme, in one paragraph

After the single-turn spike, AGE was tested where it should matter most: an agent evolving a project across many sessions
toward a charter, in synthetic worlds whose target needs a hidden idea and a governed charter change through a scripted
owner. AGE was then applied to itself (attractor → most valuable uncertainty → hypothesis → test → update), producing a
loop kit (v2) and, after an owner-approved charter fix that separates direction claims from implementation attempts, kit
v3. Results: governance (evidence-backed charter requests, no silent edits) is already present in plain Claude; kit v3 went
from 0/3 to 2/3 plateau breaks in a hinted world, but in a validated world where generation was measured directly (blind
classifier on the agents' records) **0 of 9 runs in any arm articulated the hidden structure**, and several exploited it
without understanding it. Decision: the AGE kit is not adopted as a default; the capability "generate new hypotheses at a
plateau" stays open. See [the summary](PROGRAMME-SUMMARY.md).

## The spike, in one paragraph

AGE says it must earn its cost against simpler practice, so it was tested. Four arms of `claude -p` (Sonnet) answered
trap and routine tasks, with and without the AGE contract, and with and without an experienced user's existing
CLAUDE.md. A blind Opus judge scored the answers, validated with planted good/bad answers. Run v1 was **INVALID** (a
harness artifact broke a quarter of the answers). On held-out tasks written by an author who had not seen AGE, run v2
**REJECTED** AGE as a default: the gain was +0.38 and +0.31 on a 0–10 scale against a pre-registered 0.5 cutoff. The
one consistent gain was refusing to trust self-reported "in==out" success. What remains untested is mid-task agentic
drift. See the [report](spike-2026-10-09/REPORT.md) for scope and caveats.

## License

Text: [CC BY 4.0](LICENSE). Scripts under `spike-2026-10-09/`: same terms.

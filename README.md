# Product design work — Dhanesh Shetye

Case studies, teardowns and working documents. Each deliverable is a single self-contained
HTML file: no build step, no dependencies, no external requests.

---

## Deliverables

| # | Document | Read it | Source |
|---|---|---|---|
| 1 | **CoverSure Policy Portfolio** — case study, three versions | [Scan](https://dhanesh100.github.io/Case-study/#scan) · [Compact](https://dhanesh100.github.io/Case-study/#compact) · [Full study](https://dhanesh100.github.io/Case-study/#full) | [`index.html`](index.html) |
| 1a | **Scan version, standalone** — the same thing as one sendable file | [Read](https://dhanesh100.github.io/Case-study/scan/) | [`scan/`](scan/) |
| 2 | **Portfolio Measurement Plan** — how to test whether the strategy works | [Read](https://dhanesh100.github.io/Case-study/measurement/) | [`measurement/`](measurement/) |
| 3 | **Tiimo teardown** — competitive product design analysis | [Read](https://dhanesh100.github.io/Case-study/tiimo-teardown/) | [`tiimo-teardown/`](tiimo-teardown/) |
| 4 | **Teardown analysis brief** — the reusable prompt behind #3 | — | [`ANALYSIS-BRIEF.md`](tiimo-teardown/ANALYSIS-BRIEF.md) |
| 5 | **Project log** — feedback, decisions, corrections, open items | — | [`PROJECT-LOG.md`](PROJECT-LOG.md) |

---

## 1 · CoverSure Policy Portfolio

**Making Portfolio respond to the user — not just display their policies.**

Product Designer · Post-MVP · UX Strategy · Personalisation · Progressive Disclosure

Five capabilities needed to be discovered on the screen where people manage their policies:
Add Policy, CoverRisk, Buy Policy, Family Management and KYP. Promotional banners were the
obvious answer, and they competed with the screen's primary job.

So the question changed from *"how do we promote these features?"* to *"when does each
feature become useful to this user?"* — which turns promotional slots into **conditions**
that can be evaluated against a person's actual portfolio.

Published as three tellings of the same argument, switchable by tabs and individually
shareable:

| Version | Reading time | Approach |
|---|---|---|
| **Scan** — `#scan` | ~3 minutes | Six decisions, each a transferable principle with a screen as evidence. The reasoning behind any one opens in an overlay, so depth is opt-in and the scan stays short. |
| **Compact** — `#compact` | ~4 minutes | Visual-led. Five skill points, each carried by a diagram. |
| **Full study** — `#full` | ~13 minutes | Narrative. Six proofs, the full reasoning. |

The Scan version is also published on its own at [`scan/`](scan/) — a single self-contained
file, for sending to someone directly rather than as a tab among three.

**Sixteen real screens**, exported from the production Figma file and shown in scrollable
device frames rather than cropped, so a 6,000-pixel screen stays explorable. All diagrams are
hand-authored inline SVG.

## 2 · Portfolio Measurement Plan

Companion to the case study, and an answer to the question it leaves open —
*"quantitative results to follow as usage data matures."*

The case study makes falsifiable claims. This turns each one into a hypothesis with a metric,
a threshold that would disprove it, and what to change when it does.

- **State transition rate** as the headline metric, and why it beats a completeness score
- A **diagnostic ladder** — precision → reach → action → outcome → durability — mapping each failure to its actual fix, which is rarely the next stage down
- A **hypothesis register** covering all ten design decisions
- **Cover adequacy ratio** as the business metric, because conversion cannot distinguish adequate cover from cheap cover
- **Metrics that will mislead you**, and the pre-commitment needed to resist them
- The instrumentation that is cheap now and impossible to reconstruct later

## 3 · Tiimo teardown

A competitive teardown of [Tiimo](https://www.tiimoapp.com/), Apple's iPhone App of the Year
2025. It argues the product's value is **outsourced executive function** rather than planning
— which inverts the normal tolerance for defects, because reliability becomes the feature
rather than a quality attribute.

Written from **public evidence only, with no hands-on use of the app.** Sections requiring
the product are marked as gaps rather than filled with speculation, every substantive claim
is tagged *observed* / *reported* / *inferred* / *assumed*, and a field guide lists what to
check when someone does install it.

[`ANALYSIS-BRIEF.md`](tiimo-teardown/ANALYSIS-BRIEF.md) is the reusable brief it was written
against — the method published alongside the output, and re-runnable on any other app.

## 5 · Project log

[`PROJECT-LOG.md`](PROJECT-LOG.md) is the working record behind the case study:

- **Feedback and direction received** — every instruction given, and what each changed
- **Fact-finding** — the six questions asked to keep the content factual, and the answers
- **Decision record** — decisions and rationale, including the ones later reversed
- **Corrections made** — what was wrong in a draft and how it was fixed
- **What is illustrative, not real** — so no figure is mistaken for product data
- **Open items** and the deployment record

---

## Working notes

### On the data in the screens

Policy names, ratings, cover amounts, premiums, member names and dates are **illustrative
placeholder values taken from the design files** — not real customer or product data. The
project log states plainly which figures are which.

### Not in this repository

Two working documents are deliberately excluded: the V2 build brief and the raw fact-finding
answers. Both hold unedited internal detail. The project log covers the same ground in a form
fit for publishing.

Draft versions of each deliverable also exist as private Claude artifacts. Those are
reachable only by the account owner unless explicitly shared, so **the GitHub Pages links
above are the ones to send anyone.**

### Built with

Hand-authored HTML and CSS. No frameworks. Screens are real exports embedded as data URIs so
each file stays self-contained; diagrams are inline SVG.

- Adapts to light and dark system themes
- Responsive down to 390px
- Keyboard-operable tabs, `prefers-reduced-motion` respected
- Verified after each deploy: HTTP status, doctype, charset, glyph rendering, embedded assets

---

© Dhanesh Shetye. Case study content and design.

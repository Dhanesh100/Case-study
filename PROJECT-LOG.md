# Project log — CoverSure Policy Portfolio case study

**Last updated:** 20 August 2026
**Deliverable:** [`index.html`](index.html) — live at <https://dhanesh100.github.io/Case-study/>
**Author:** Dhanesh Shetye · **Built with:** Claude Code (Opus 5)

A working record of how this case study was built: the brief, the decisions and their
reasoning, the questions asked to keep the content factual, the answers given, the
corrections made along the way, and what remains open.

> **Note on visibility:** this repository is public and so is this document. It records
> internal project reasoning. If any of it should not be public, move it to a private
> repository — git history persists after deletion.

---

## 1. The brief

Convert a screens outline into a product design case study for a portfolio.

The source material was a terse outline — headlines, fragments, and seven `[SCREEN xx]`
placeholders with no exported screens. The task grew over several rounds into:

1. A full narrative case study
2. A second, compact, visual-led version
3. Version tabs so both live in one page, individually shareable for A/B testing
4. Replacing all illustrative content with real project facts

---

## 2. Design direction, and why

### Visual identity

**Decision:** derive the identity from CoverSure's own product surface rather than the
cream-paper / serif-display / terracotta-accent treatment used in the earlier CoverSure
homepage case study.

**Reasoning:** that combination is the most common look in AI-generated design work, and
it reads as templated. Grounding the palette in the product's own world is both more
specific and more defensible.

| Token | Value | Role |
|---|---|---|
| `--ink` | `#0c1633` | Policy navy — near-black with a blue bias |
| `--ground` | `#f2f5fa` | Cool paper, slight blue bias (chosen neutral, not default grey) |
| `--accent` | `#1f43ff` | Electric blue |
| `--signal` | `#c9331f` | Reserved *only* for the rejected option and warnings |
| `--stage` | `#0a1236` | Navy display surface behind device mockups |

**Typography** — three roles, all system-available (the Artifact CSP blocks font CDNs, so
a linked webfont would silently fall back):

- **Display:** Avenir Next Condensed Demi — condensed headlines, document-masthead feel
- **Body:** Charter — sturdy serif built for reading
- **Utility:** SF Mono — rule notation, labels, and every ₹ figure with `tabular-nums`

**Layout** — a ~60ch reading column with a narrow mono "notation" gutter that names which
part of the argument each section carries (`PROBLEM`, `STRATEGY`, `PROOF 01`…). Full-bleed
navy stages break the column wherever screens appear.

### Structural decisions

- **The notation gutter is the narrative spine.** It exists so the case study passes a
  scan test: strip every paragraph and the headings alone must still tell the story.
- **Five skill points are labelled by skill, not numbered `01–05`.** They are five
  parallel capabilities, not a sequence — numbering them would be decoration, not
  information.
- **`Adapt` sits on the return edge of the loop diagram, not as a terminal box.** Adapt is
  what closes the loop; drawing it as a final stage would misrepresent the mechanism.
- **No metric or performance charts.** The product recently launched with no mature usage
  data. Diagrams of logic and structure are verifiable; a fabricated adoption chart is the
  fastest way to lose a senior reviewer's trust.

---

## 3. The two versions

| | Compact | Full study |
|---|---|---|
| Reading time | ~60 seconds | ~5 minutes |
| Approach | Visual-led — every point carried by a diagram | Narrative — eight screens, six proofs |
| Prose budget | ~220 words (hard cap ~400) | ~700 words |
| Deep link | `#compact` | `#full` |

Both tabs are styled with equal weight and neither is marked "recommended" — a badge would
bias the A/B feedback being collected. Default view is set by a single `DEFAULT_VIEW`
constant so it can be flipped in one edit.

---

## 4. Fact-finding — six questions, and the answers

Illustrative content was replaced by asking for real project facts. Summarised below.

### Q1 · What does CoverRisk actually calculate?

**Answer.** CoverRisk collects age, location, family size, dependants, health, lifestyle,
fitness, income, investments, property and expenses, then generates a detailed risk report
and recommends an appropriate coverage amount.

Critically: **that intelligence previously stayed inside CoverRisk** and was not used
anywhere else. Surfacing it in Portfolio — a recommended cover amount plus an average
premium for that cover at the user's age and health profile — was the design intervention.

The recommendation deliberately names **no specific insurer**. Rationale: most users don't
know what coverage they need, so they optimise the one number they understand (premium)
and buy the cheapest policy. If treatment then removes their income, the cover was never
built for their situation — which is exactly what critical illness cover addresses.

### Q2 · What are the real header figures?

**Answer.** The shipped header shows `Member · Policies · Premium Yearly`, with member
avatar chips (Family / Self / Mother / +) and `Add Policy` in the top-right. A verified
family state: **3 members · 9 policies · ₹82 K yearly premium.**

This resolved an arithmetic inconsistency in the earlier draft, where a 9-policy header sat
above categories totalling 7. The 9 is a *family* total, so it now decomposes cleanly:
Self 4 (₹38 K) + Mother 3 (₹26 K) + Father 2 (₹18 K).

The Family Overview also solved an adoption problem: one person usually manages insurance
for a whole family, and scattered or missing policies make premiums, renewals and
emergencies harder. An **incomplete overview is its own prompt** — no banner needed.

### Q3 · What shipped, and what is Advisor Portfolio?

**Answer.** All features shipped.

Advisor Portfolio deliberately got **no banner on Portfolio**. The Homepage already
provides a direct entry point, so repeating it would add noise without adding access.
Instead the advisor call appears after the CoverRisk report generates — when the user has
context and, likely, questions that justify expert help.

This became its own section. Declining to place a feature is harder to argue for than
placing one, and it is the strongest decision in the case study.

### Q4 · Who created the protection tiering?

**Answer.** The tiering — which insurance to promote first, and what follows — was decided
by the designer, worked through with the product team for domain judgement.

**CoverRisk does not decide this order.** It supplies the coverage amount and premium
estimate only. The sequence is a separate decision that holds regardless of what the report
returns. If someone has no life cover, home insurance is not pitched.

| Tier | Products | Rule |
|---|---|---|
| Foundational | Health, Life | Nothing outranks it |
| Additional | Super Top-Up, Critical Illness, Accident | Only once the foundation exists |
| Situational | Hospicash, Home, other | Only on a signal |

### Q5 · Evidence for "users came to manage, not to be sold to"

**Answer.** Informed judgement rather than formal study. Users land on Portfolio to check
policies they have saved; banners annoy them and some skip the section entirely afterwards.

The stronger point is that this follows an existing **CoverSure brand principle**: never
sell a policy without proper information and the right coverage amount, and don't push a
low-premium policy just because it converts — a low cover amount fails people at the moment
it matters. The design work applied that principle to the screen where the temptation to
break it was strongest.

Framed in the case study as a stated design hypothesis, not a research finding.

### Q6 · Scope and the stakeholder story

**Answer.** Team effort on a mature product, post-MVP.

- The **product head** brought the problem set: users couldn't navigate to policy details properly, promotional banners confused them, and nobody was adding family members because no family overview existed.
- **Product head and team lead** originated the Family Overview and the CoverRisk entry point on Portfolio.
- The **product lead** originated bringing KYP ratings onto the policy card.
- Product and team leadership carry years of knowledge of the product, its users and the insurance industry; every significant decision was discussed with them.

**Designer-owned:** the recommendation order and tiering, connecting CoverRisk's numbers
back to Portfolio, declining the Advisor banner, reason-before-action for Share Policy, the
information hierarchy rule that the pitch sits below the policies, interaction design,
progressive disclosure and UX writing.

---

## 5. Corrections made

The most useful output of the fact-finding. Each of these was wrong in a draft and got fixed.

| # | What was wrong | Fix |
|---|---|---|
| 1 | Mockups were built from an **old** navy-gradient screenshot | All screens rebuilt to the shipped light monochrome UI — black active pill, avatar member chips, `Add Policy` in header |
| 2 | Header said 9 policies; categories totalled 7 | 9 is the *family* total; decomposed to 4 + 3 + 2 across three members |
| 3 | Claimed CoverRisk personalises the recommendation *order* | CoverRisk supplies amounts only; sequence is a separate design decision |
| 4 | "Adding three banners was a real option. Arguing it down was part of the work." | Removed. The product head brought banner confusion as a problem, so an adversarial framing was inaccurate |
| 5 | Proof 01 had no headline — a scanner jumped from Strategy to Proof 02 | Given its own section, matching Proofs 02 and 03 |
| 6 | Reading grid had no flexible third track | Full-width tiers and diagrams were being clamped to the text column |
| 7 | Full-study subtitle repeated the meta row directly beneath it | Replaced with the actual proposition |
| 8 | Real insurer names paired with **invented** KYP ratings | Replaced with generic policy names before the public push |
| 9 | Artifact file is a fragment — no doctype, head, or charset | Wrapped into a complete document for GitHub Pages; otherwise quirks mode and garbled ₹ |

---

## 6. What is illustrative, not real

Stated plainly so nothing here is mistaken for product data.

| Item | Status |
|---|---|
| 3 members · 9 policies · ₹82 K yearly | **Real** (from a shipped screen) |
| Recommended cover ₹80,00,000 · premium ₹11,800/yr · existing ₹40,00,000 | Illustrative |
| Policy names, per-policy premiums, due dates | Illustrative |
| KYP scores (4.4 / 4.1 / 3.2) | Illustrative |
| Member names (Mother, Father), nominee name | Illustrative |
| `Avg. KYP` header stat | **Invented for this case study** — substituted on single-member views, where "1 Member" carries no information |

---

## 7. Open items

1. **Real CoverRisk figures** — a sample profile with its actual recommended cover and premium.
2. **Does `Avg. KYP` exist** as a header stat on single-member views? If not, what sits there?
3. **Is KYP scored out of 5?** Currently shown on a five-point scale.
4. **Restore real insurer names?** Only if the KYP ratings shown are real product data.
5. **Compact cover has no screenshot** — it opens on the reframe diagram instead. A deliberate call, and a good thing for the A/B test to settle.

---

## 8. Technical reference

Single self-contained file. No build step, no dependencies, no external requests.

- **Themes** — three-state handling: bare `:root` for light, `@media (prefers-color-scheme: dark)` guarded as `:root:not([data-theme="light"])`, and `:root[data-theme="dark"]`. No colour is defined only inside a media or `[data-theme]` block. Device internals are painted explicitly in product colours in both themes — they are screenshots, not UI.
- **Screens** — HTML/CSS reconstructions of the shipped interface. No images.
- **Diagrams** — hand-authored inline SVG, themed via `currentColor` and CSS custom properties, with labelled edges.
- **Motion** — one auto-advancing screen carousel: 3.8s dwell, pauses on hover and focus, manual dots, visible pause control, fully disabled under `prefers-reduced-motion`.
- **Tabs** — `role="tablist"` with `aria-selected` / `aria-controls`, arrow-key and Home/End navigation, hash deep links, and `history.replaceState` so the back button leaves the page rather than walking tab history. The inactive panel uses the `hidden` attribute so it leaves the accessibility tree.
- **Responsive** — verified at 1440 / 900 / 390 px. Wide content scrolls inside its own `overflow-x: auto` container; the page body never scrolls sideways.

### Validation run before each publish

1. Tag-balance parse — zero unclosed or mismatched elements
2. Theme audit — zero colour literals defined only in a media or `[data-theme]` block
3. Scan test on **both** versions — strip all prose; the spine alone must still tell the story
4. Duplicate-ID check
5. Prose word count against the Compact budget
6. Live-URL check after deploy — status, doctype, charset, ₹ glyph rendering

---

## 9. Change history

| Date | Change |
|---|---|
| 20 Aug 2026 | Initial build from the screens outline. Seven screens reconstructed as HTML/CSS; product-grounded visual identity. |
| 20 Aug 2026 | Near-final pass. Added the narrative spine, protection tiers, and the closed-loop diagram. Fixed the missing Proof 01 headline and the clamped layout grid. |
| 20 Aug 2026 | Second version plus tabs. Compact visual-led version, deep links for A/B testing, auto-advancing carousel. |
| 20 Aug 2026 | Real project facts merged. All screens rebuilt to the shipped light UI; Family Overview, KYP and Advisor restraint added as their own sections; credit attribution corrected. |
| 20 Aug 2026 | Published to GitHub Pages. Insurer names neutralised; wrapped into a standalone document. |

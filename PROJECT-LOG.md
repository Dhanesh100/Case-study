# Project log — CoverSure Policy Portfolio case study

**Last updated:** 20 August 2026 · records the full discussion, feedback and decisions behind this case study
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

## 4. Feedback and direction received

The brief moved substantially across the project. Recorded in order, with what each
instruction changed.

| Direction given | What changed as a result |
|---|---|
| "Create a product designer case study from this" | First build from the screens outline. Seven `[SCREEN xx]` placeholders reconstructed as HTML/CSS, identity grounded in the product surface. |
| Make it near-final: work at **two reading levels** — a 20–30 second scan and a 2–3 minute read. "Hide all the body copy… if the story still makes sense, you've succeeded." | The scan test became a hard acceptance criterion, run programmatically before every publish. The mono notation gutter exists to satisfy it. |
| Add a second version with **version tabs**, built around five points showing strategy, UX and business understanding | The Compact version, the five skill-labelled points, and the tab shell. |
| "I want these versions to A/B test with friends and decide from feedback" | Tabs styled with **equal weight** — no "recommended" badge, which would bias the result — plus `#compact` / `#full` deep links so each tester can be sent one version cold. |
| "Less text, more visual — graphs, charts, maps to scan and understand easily" | Compact became diagram-led with a hard ~400-word prose budget (it landed at 220). Every point carries a visual. |
| "We can add video or auto-scroll to showcase more UI screens" | Video is impossible under the artifact CSP and would blow the 16 MB budget, so an auto-advancing carousel with a pause control was built instead. Later, scrollable device frames served the same purpose for tall screens. |
| Answers to the six fact-finding questions | Illustrative content replaced with real project facts. See §5. |
| A fully rewritten narrative supplied, with an explicit spine: Problem → Decision → Strategy → Proof ×3 → Outcome → Role | Both versions restructured to that spine. Section order and headline wording follow it. |
| "Reflect these details in all versions" | Family Overview, KYP and the Advisor restraint added as their own sections; capability list grown from four to seven. |
| Ten reference screens supplied | Three claims in the case study found unsupported. See §8. |
| Three Figma section links supplied | Real screens exported and embedded, replacing ten of twelve mockups. See §9. |
| "Save the discussion, feedback and decisions in a document in the repository" | This log. |

---

## 5. Fact-finding — six questions, and the answers

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
avatar chips (Family / Self / Mother / +) and `Add Policy` in the top-right.

**Every figure in the supplied screens is a placeholder,** and the screens depict different
users and use cases rather than one continuous account — so cross-screen totals are not
meant to reconcile. What matters is that each individual screen is internally consistent.
An earlier draft had a 9-policy header above categories totalling 7; that is fixed.

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

## 6. Decision record

Decisions taken, and why. Where a decision reversed an earlier one, both are shown.

### Design

| Decision | Rationale |
|---|---|
| Identity derived from the product surface — policy navy, electric blue, cool paper | The alternative on hand was the cream / serif-display / terracotta treatment from the earlier CoverSure homepage case study. That combination is the most common look in AI-generated design work and reads as templated. |
| Avenir Next Condensed + Charter + SF Mono, all system-available | The artifact CSP blocks font CDNs; a linked webfont would silently fall back to a default and quietly wreck the type. |
| Points labelled by skill, not numbered `01–05` | Five parallel capabilities are not a sequence. Numbering them would be decoration pretending to be information. |
| `Adapt` drawn on the return edge of the loop, not as a terminal box | Adapt is what closes the loop. Drawing it as a final stage would misrepresent the mechanism the diagram exists to explain. |
| Real screens shown in fixed-height **scrollable device frames**, not cropped | One export is 6,000 px tall. Cropping picks the reader's conclusion for them; a scrollable frame keeps the whole screen explorable without dominating the page. |
| Before/after recommendation pair left as a CSS reconstruction | The "before" is a hypothetical the product never shipped. Presenting a mockup as an export would be a false claim. |
| Compact version opens on the reframe diagram, with no screenshot | In a 60-second read a diagram explaining the strategic move does more than a screenshot. Deliberately contentious — flagged as something the A/B test should settle. |

### Publishing

| Decision | Rationale |
|---|---|
| Both versions in one page, tabs, equal weight, deep-linkable | The A/B test needs one shareable URL per version and no visual hint of a preferred answer. |
| Images embedded as data URIs, not relative paths | The artifact CSP blocks external hosts, and relative paths would 404 there. One self-contained file works identically as artifact and as Pages. |
| JPEG at 620 px wide, quality 85, displayed at 292 CSS px | Displaying at under half the source width averages compression artefacts away. Total 2.4 MB against a 16 MB ceiling. |
| Working documents (build brief, raw answers) kept out of the public repo | They hold raw internal detail. This log covers the same ground in a form fit for publishing. |
| Real product screens published publicly | Supplied deliberately for this purpose via Figma links. Exposes the PRO tier, per-product pricing, the rating mechanism and the category taxonomy. Revisit if that changes; git history persists. |

### Content integrity

| Decision | Rationale |
|---|---|
| No metric or performance charts | The product recently launched with no mature usage data. Diagrams of logic are verifiable; a fabricated adoption chart is the fastest way to lose a senior reviewer. |
| "Recently launched — quantitative results to follow" kept verbatim | Better to show reasoning than a number that cannot yet be stood behind. |
| **Reversed:** "Adding three banners was a real option. Arguing it down was part of the work" — removed | The product head brought banner confusion as one of the problems, so an adversarial framing was inaccurate. |
| Credit split by voice: "we" for team-originated work, "I" for designer-owned | Overclaiming solo credit on team work is a known portfolio red flag. Naming the lane makes every other claim more believable. |
| Generic policy names, not real insurers | First taken as caution on a public repo. Later confirmed correct for a better reason: the names in the designs are placeholders, so real ones would be fabricated. |
| Shipped share copy quoted **alongside** the refined line | The refined line has not shipped. Implying it had was the one claim on the page a reviewer could disprove by opening the app. |
| The inherited PRO banner named explicitly in Proof 06 | A reader comparing copy to screenshot would spot it. Naming what was outside the remit is stronger than silence. |
| Tier bars labelled "relative priority — not measured data" | They are the only quasi-quantitative element on the page and would otherwise read as measurement. |

---

## 7. Corrections made

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

## 8. Reference-screen review — 20 August 2026

Ten screens of the shipped interface were supplied for reference. They are substantially
more detailed than the single screenshot the mockups were first built from, and they
**contradict three claims** in the case study as written. Recorded here rather than
quietly written around.

### Claims the screens do not support

| Claim in the case study | What the screens show |
|---|---|
| "No promotional slots anywhere on screen" | The Family view carries a prominent dark-purple **PRO** banner — *"Unsure of your IDEAL coverage?" / "Dedicated Relationship Manager and 15+ benefits"* — directly under the first member card. The Self view carries Buy Health (₹200/mo), Buy Life (₹80/mo), Buy Super Top-up (₹299/mo), Buy HospiCash, Buy Personal Accidental, Buy Home cover, plus three `RECOMMENDED` cards. |
| "We deliberately didn't add an Advisor banner to Portfolio" | The PRO banner offers a *Dedicated Relationship Manager*. If that is the advisor, the restraint argument in Proof 06 does not hold as written. Unresolved: whether PRO is a separate paid tier distinct from Advisor Portfolio. |
| The recommendation is a cover amount + premium card | The shipped mechanism is broader: per-category coverage meters (`COVERED 20%`, `COVERED 100%`) with segmented bars, an inline *"Are you paying for right health policy or not?"* prompt offering **Review report** / **Pay without Review**, and *"Is your Coverage Enough?"* in section headers. |

### Fidelity corrections identified

- **KYP is not a numeric score.** It renders as `Policy Rating · GREAT` — a four-segment green meter with `✔2 | !8` counts for good and bad aspects. The `4.4` badge in the current mockups is invented. The ✔/! split is itself the "explore the reasons" mechanism and is better material than a number.
- **Member cards are richer than reconstructed.** Name + relationship, a collapsible `12 policies | premium ₹80.2 K` row expanding into a category breakdown (2 Health ₹10 L insured · 1 Life ₹1.2 Cr · 4 Endowment ₹50 L · 2 Motor ₹12.7 L IDV), then **Check portfolio**. Members without policies show an amber `Policy not added → + Add Policy` row.
- **Features not previously known:** Sync status · Download portfolio · Insurance on Card (debit/credit card benefits, named banks) · `Found 2 inactive policies → Review` · `4 Upcoming Renewals → Review & pay`.
- **Category taxonomy is far wider** than the three used in the mockups: Health, Life, Motor, General, Agriculture, Business, Credit, Speciality, Other, Corporate, Endowment.
- **Insurer names in the screens are placeholders**, not live product data. The earlier decision to replace them with generic policy names was therefore correct and stands.
- **Internal inconsistency across the supplied variants:** one header reads `3 Member · 9 Policies · ₹82 K`, another `₹14.12 L`, while Rohit alone shows 12 policies / ₹80.2 K. Normal for design exploration; a canonical set is needed before the screens go into the case study.

### Resolved — 20 August 2026

| Question | Answer | Consequence |
|---|---|---|
| Is the PRO banner in scope? | **No.** It carries over from the previous design and is being repositioned in an upcoming update. | The case study now names it explicitly as inherited and outside scope, rather than leaving a viewer to spot the mismatch. |
| Is PRO's relationship manager the same as Advisor Portfolio? | **No.** PRO's RM covers general support — claims, legal, policy problems. Advisor Portfolio is specifically guidance on cover. | **Proof 06 survives, and is stronger.** Two distinct needs is precisely why a second advisor entry point here would have blurred both. |
| Which figures are canonical? | None. All placeholders; the screens show different users and use cases. | No attempt to reconcile totals across screens; each screen must be internally consistent. |
| Are the insurer names real? | No, placeholders. | Generic policy names stay. |

### Applied to the build

- Numeric `KYP 4.4` badges replaced with the shipped component: a `Policy Rating · GREAT` band with a four-segment meter and `✔ / !` counts (8 instances).
- The invented `Avg. KYP` header stat removed; headers now use `Member · Policies · Premium Yearly` throughout, matching the screens.
- KYP copy rewritten around the good/bad counts rather than a score — the ✔ / ! split is the mechanism, and it is better material than a number.
- A "What I didn't control" note added to Proof 06 covering the inherited PRO banner.

### Blocked

The screens were supplied as chat attachments, not files, so they cannot yet be encoded
into the page. Needed as files on disk, or as a Figma link for direct frame export.

Constraints when they arrive: the Artifact CSP blocks external images, so each must be
embedded as a data URI; base64 adds roughly a third; the page ceiling is 16 MB. Plan is
per-section crops at ~800 px wide rather than full-length images — one supplied screen is
12,284 px tall and unreadable inline.

**Publishing note:** this repository and its Pages site are public. The screens expose the
paid PRO tier, per-product pricing, the rating mechanism, coverage logic and the full
category taxonomy — more of the product surface than the case study text reveals. Clearance
is required before they are committed here; otherwise they stay in the private artifact copy
and the public repo keeps the reconstructions.

---

## 9. Real screens replace the reconstructions — 20 August 2026

Three Figma section links were supplied and the screens exported directly through the
Figma connector, replacing ten of the twelve hand-built CSS mockups. The two that remain
CSS are the before/after recommendation pair, because the "before" is a hypothetical the
product never shipped.

| Section | Figma node | Export |
|---|---|---|
| Screen 01 hero, Family Overview | `3091:24982` | 824×3222 @2x |
| No policies added | `2167:25953` | 412×916 |
| Pending attention | `10254:35122` | 412×1260 |
| Member portfolio | `2176:24732` | 412×1856 |
| Life policy detail | `9640:52243` | 412×2115 |
| Policy rating scale | `2129:17149` | 380×520 |

Screens are shown inside a fixed-height scrollable device frame rather than cropped, so a
6,000-px screen stays explorable without dominating the page. Encoded as JPEG at 620 px
wide, quality 85, embedded as data URIs — the artifact CSP blocks external images, and one
self-contained file works identically as the artifact and on Pages. Displayed at 292 CSS px
from a 620-px source, so compression artefacts average out. Total page: 2.4 MB against a
16 MB ceiling.

### What the real screens changed

- **The rating scale is four levels, not one.** `GREAT / GOOD / AVERAGE / POOR`, each a colour-coded four-segment meter with counts of favourable and unfavourable conditions, plus a `COMING SOON` state. The earlier `4.4` badge was invented and the single-level `GREAT` band that replaced it was still incomplete.
- **Know Your Policy is a tab**, sitting beside Details on the policy itself — not only a badge on the card. Added to Proof 05.
- **Coverage adequacy is contextual, not a banner.** Each category header carries its own *"Is your Coverage Enough?"* beside a meter. Where a policy is due the choice is **Review report** or **Pay without Review**.
- **Buy suggestions sit at the foot of the screen with reasons attached** — *"Hospital treatments in metro cities can cross ₹8–12L in one admission."* This is direct evidence for the case study's central rule, and it was previously argued rather than shown.
- **The share card is real**, positioned after the policy details, alongside an `Emergency` shortcut in the header and a collapsible `Nominee` section.
- **Shipped share copy differs from the case study's line.** The card reads *"While any emergency, share policy with family members will be helpful."* The refined line is presented as the UX-writing contribution, with the shipped version quoted — rather than implying the polished copy is live.
- **State labels corrected.** "Health + Motor" and "CoverRisk completed" described states that do not exist as frames; they are now "Pending attention" and "Policies added", matching what the exports show.

**Publishing note:** these are real product screens on a public repository and Pages site — the PRO tier, per-product pricing, the rating mechanism and the full category taxonomy are all now publicly visible. Supplied deliberately for this purpose; revisit if that changes.

---

### Second export pass — 24 August 2026

Five further frames pulled from the `2167:25324` portfolio-overview section, taking the page
to 16 real screens.

| State | Figma node | Why it earns a place |
|---|---|---|
| Group health only | `2167:26169` | One employer policy at ₹5 L insured, and **Premium Yearly reads "—"** because the user doesn't pay it. Honest data handling on a screen that could easily have shown a misleading number. |
| One policy | `2167:26040` | Sparse-but-not-empty state |
| Inactive policy found | `2167:26298` | A lapsed policy surfaced as service rather than noise — and the rare case where user and business interest genuinely coincide |
| Fuller family overview | `3405:18236` | The end state, with prompts gone because their conditions are no longer true |
| Homepage | `3348:23080` | Evidence for the cross-surface context claim |

**Correction the Homepage forced.** CoverRisk does not only return a cover amount. On the
Homepage it surfaces as a **score with a risk band — 40, "moderate risk" — alongside
per-category coverage percentages**. The case study previously described only the amount.
Proof 02 now records both, and the Homepage screen is included specifically to show the same
user state being read two different ways for two different jobs.

The compact carousel grew from three slides to five. The full study gained a "More
conditions" stage carrying four states. Page weight 3.43 MB against a 16 MB ceiling.

---

## 10. What is illustrative, not real

Stated plainly so nothing here is mistaken for product data.

| Item | Status |
|---|---|
| 3 members · 9 policies · ₹82 K yearly | Illustrative — confirmed placeholder |
| Recommended cover ₹80,00,000 · premium ₹11,800/yr · existing ₹40,00,000 | Illustrative |
| Policy names, per-policy premiums, due dates | Illustrative |
| KYP scores (4.4 / 4.1 / 3.2) | Illustrative |
| Member names (Mother, Father), nominee name | Illustrative |
| `Avg. KYP` header stat | **Invented for this case study** — substituted on single-member views, where "1 Member" carries no information |

---

## 11. Open items

Everything blocking earlier has been resolved. What remains:

1. **Real CoverRisk figures.** The recommended cover, premium and existing-cover values in the before/after card are still illustrative. This is the last invented number on the page, and it sits in the largest element of the Compact version.
2. **Is the refined share-policy line live anywhere?** The exported policy screen shows the looser shipped copy. Proof 03 currently carries a caveat saying the refined line is still in flight — removable if it has shipped on a surface that was not exported.
3. **Compact cover: diagram or screenshot?** It opens on the reframe diagram with no UI. A deliberate call, and precisely the kind of thing the A/B test exists to settle.
4. **Pick a version.** Once peer feedback is in, either consolidate on one telling or keep both with a clear default.
5. **Public visibility of real product screens.** Decided and live, but revisitable — noted here so it stays a conscious choice rather than an accident.

---

## 12. Deployment record

| | |
|---|---|
| Repository | <https://github.com/Dhanesh100/Case-study> (public) |
| Live site | <https://dhanesh100.github.io/Case-study/> |
| A/B links | `#compact` · `#full` |
| Pages source | `main` branch, root path, HTTPS enforced |
| Page weight | 2.42 MB, 10 embedded screens |

Verified after deploy rather than assumed: HTTP 200 on all three URLs, doctype and charset
present in the served HTML, all 31 ₹ glyphs rendering, all 10 data URIs present, and no
placeholder brand names leaking into the published page.

---

## 13. Technical reference

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

## 14. Change history

| Date | Change |
|---|---|
| 20 Aug 2026 | Initial build from the screens outline. Seven screens reconstructed as HTML/CSS; product-grounded visual identity. |
| 20 Aug 2026 | Near-final pass. Added the narrative spine, protection tiers, and the closed-loop diagram. Fixed the missing Proof 01 headline and the clamped layout grid. |
| 20 Aug 2026 | Second version plus tabs. Compact visual-led version, deep links for A/B testing, auto-advancing carousel. |
| 20 Aug 2026 | Real project facts merged. All screens rebuilt to the shipped light UI; Family Overview, KYP and Advisor restraint added as their own sections; credit attribution corrected. |
| 20 Aug 2026 | Published to GitHub Pages. Insurer names neutralised; wrapped into a standalone document. |
| 24 Aug 2026 | Second export pass: five more real states including group-health-only and the Homepage. CoverRisk corrected — it returns a score and risk band, not only a cover amount. 16 screens total. |
| 20 Aug 2026 | Real screens exported from Figma and embedded, replacing 10 of 12 CSS mockups. Rating scale, KYP tab, contextual coverage checks and reasoned buy suggestions all corrected against the shipped UI. |
| 20 Aug 2026 | Screen questions answered. PRO confirmed out of scope and distinct from Advisor Portfolio; all figures confirmed placeholders. KYP rebuilt as the real rating band; invented `Avg. KYP` stat removed. |
| 20 Aug 2026 | Reference screens reviewed. Three narrative claims found unsupported and logged; KYP rating format, member-card structure and category taxonomy corrections identified. Screens pending as files. |

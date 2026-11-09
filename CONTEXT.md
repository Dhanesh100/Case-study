# CONTEXT — read this first

**Purpose.** Everything a new session, a new collaborator or a future me needs before
touching this repo, so Dhanesh does not have to explain it again. `PROJECT-LOG.md` is the
chronological record of what happened. **This file is the standing brief.**

Last updated: 9 November 2026 · current version: **V12** (with the everyday layer, §17)

---

## 0 · The session protocol

So that the project never has to be re-explained:

| When | Do this |
|---|---|
| **Session starts** | `git pull --ff-only origin main`, then read this file. `./sync.sh` does both and prints what is open. |
| **Any change is made** | Commit and push immediately, without being asked. Then verify against the live URL, not the Pages API. |
| **Dhanesh states a durable fact, corrects a framing, or settles an open question** | Write it into this file **in the same turn**. If it only lives in the conversation, it is lost. |

[`CLAUDE.md`](CLAUDE.md) carries the same protocol and is loaded automatically at the start
of every session in this directory, so it applies whether or not anyone remembers to say so.

**What this does not cover.** A session started outside this directory will not auto-load
`CLAUDE.md`. If that happens, pointing at `CONTEXT.md` is the whole handoff.

---

## 1 · Standing instructions

| | |
|---|---|
| **Push without asking** | *"push every update without any prompt, every prompt result push to github"*. Commit and push every change to `https://github.com/Dhanesh100/Case-study`. Do not wait to be told. The one carve-out: flag before publishing anything sensitive. |
| **No decorative content** | *"i dont want to write any decorative content or copy inside my case study"* and *"my first priority is present my skills not any decorative content or copy"*. Every sentence must carry a fact, a decision or a reason. |
| **Real over impressive** | *"wanted to make this casestudy real than just fluff"*. If a claim cannot be defended, it does not go on the page. |
| **Verify after deploy** | The GitHub Pages API reports `built` from the *previous* deployment. Poll the live URL and grep for new content; do not trust the API. |
| **Regenerate derived files** | `python3 build-scan.py` after any change to the scan panel. `python3 build-copy.py v10` after any change to V10. |

---

## 2 · Who the case study is for

Founders, product leads and heads **who do not have time to read the whole thing.** They
scan; if something catches them they read deeper. Two reading levels: the surface carries
the argument, each *See more* carries the reasoning.

**The scan test — the acceptance criterion for any new section:**

> Hide all the body copy. Read only: Title → Section headings → Bold text → Numbers →
> Diagrams → UI annotations. If the story still makes sense, you've succeeded.

A section that disappears under this test is not finished.

---

## 3 · What the work actually was

Dhanesh's own framing, which the case study must not overstate:

> *"here I did not redesign a portfolio — means I did not change the actual structure. But
> with this I added a exploration and engagement engine."*

So:

- **The structure of Policy Portfolio was not redesigned.** Its primary job — manage the
  policies you already have — is unchanged.
- **What was built is a contextual recommendation engine**: a layer that reads existing
  user context and decides which feature, product or action should appear.
- It is **CoverSure's first contextual layer**. Nothing like it existed anywhere else in
  the app.
- The engine is **v1**.

The dead-click fix is the *trigger*, not the subject. Dhanesh: *"dont want to discuss more
on fixing navigation issue, wanted to focus on contextual exploration layer."* Navigation
was a fix; the engine is the work. The feature was also rebuilt against a new design
system and its navigation reworked — real craft work that an early draft undersold.

---

## 4 · Product facts — do not re-derive these

**CoverSure** is an insurance aggregator, but it starts *before* the marketplace: it first
helps people understand the cover they already hold and what they actually need. Policy
Portfolio is where they store and manage it.

**CoverRisk** collects age, location, family size, dependants, health, lifestyle, fitness,
income, investments, property and expenses, and returns a risk report, a recommended
coverage amount and an estimated premium. It names **no specific insurer**.

> **It does not decide the order.** *"coverrisk only add cover amount and premium amount…
> sequence is decided as per which insurance types need to buy first."* The sequence is a
> separate design decision that holds regardless of what the report returns.

**The protection ladder** — three types, and the gate between tier 1 and tier 2 is strict:

| Tier | Products | Rule |
|---|---|---|
| 01 · Must have | Health **and** term life | **Both** must exist before the engine moves up |
| 02 · Extends cover | Super Top-Up, Critical Illness | Only once both of the above exist |
| 03 · Situational | Personal Accident, Hospicash, Home, Device | Only when a signal creates a reason |

> A user holding **health only is still on step one** — the engine recommends **term life**,
> not Super Top-Up. This was confirmed explicitly and **overrides Appendix A** in the deck.

**KYP (Know Your Policy)** rates a policy **GREAT / GOOD / AVERAGE / POOR** with ✔ and !
counts. There is **no numeric score** — an invented `KYP 4.4` was removed. When a rating
is unavailable, show a coming-soon band so missing data never reads as a poor rating.

**Portfolio header** shows `Member · Policies · Premium Yearly`. An invented `Avg. KYP`
stat was removed. Where a header shows 9 policies, that is the **family** total — Self 4,
Mother 3, Father 2.

**All figures in the screens are placeholders.** The screens depict different users, so
cross-screen totals are not meant to reconcile; each screen is internally consistent.

**The dead click** — the real cause, in Dhanesh's words:

> *"expand collaps and entry point to policy listing are visually similar and user confuse
> and clicked expand collaps multiple times."*

It is a **visual-similarity** problem, not an unreachable route. The route existed. And
*"dead click is right because user cant do anything and they trap in loop"* — the term is
accurate and should be used.

---

## 5 · Credit — the three-way split

Every claim of ownership in the case study resolves to one of these three voices. Keep them
distinct; do not collapse them into "I designed".

| Voice | Means |
|---|---|
| **I built** | Originated and owned — the recommendation engine, the rule set, the fixed bottom-section order, the protection tiering, the information hierarchy, progressive disclosure, interaction design, UX writing. |
| **I connected** | Existing intelligence carried into a new moment — CoverRisk's amounts into the buying action, KYP into the policy card. No second assessment was added. |
| **I worked with Product on** | Domain judgement from people with years of product and insurance knowledge. The product head brought the problem set; product head and team lead originated the CoverRisk entry point; the product lead originated bringing KYP onto the policy card. |

The **Family Overview was Dhanesh's proposal**, answering the adoption problem the product
head raised. (An early revision of the log wrongly credited it to product leadership.)

---

## 6 · What may not be claimed

Recently launched, so **no quantitative results exist yet.** Dhanesh: *"i will add data and
numbers letter. now i dont have exact numbers."*

Claims removed in review, which must not come back:

| Claim | Why it was removed |
|---|---|
| "Engagement rises because the pitch fits" | States an outcome with no data behind it. |
| "Health and term life come first. Always." | Reframed as CoverSure's hierarchy, not a universal truth. |
| "Most users open it under five times a year" | No measured figure exists. |
| "Users could not reach a policy at all" | Wrong. The route existed; the controls looked alike. |
| "Arguing it down was part of the work" | The product head *brought* the banner problem. An adversarial framing was inaccurate. |
| "Two **requested** placements were kept out" | The record says the Advisor banner was **declined**, not asked for. |
| "Nothing here was newly built" | Undersells real work: the feature was rebuilt against a new design system and navigation was reworked. |

The shipped pitch-card copy is quoted as **what the cards say** — never presented as
Dhanesh's copywriting.

The recommendation layer **does not interrupt the primary job**: *"recommendation layer is
part of current design and its not distract or stop user from there primary job."*

---

## 7 · Sources

| What | Where |
|---|---|
| Figma file | `x1YQ5nU9BirfL1IW8CHd20` — *JFM_2026_Product_Design_Projects* |
| Pitch logic, bottom section | node `3526:22821` — the rule set, the sequence annotations, the family states |
| Section-order annotations | node `4919:28398` |
| Family overview, no policy | node `3659:21849` |
| KYP rating scale | node `2129:17149` |
| Screen exports | `assets/src/*.png` → optimised to `assets/web/*.jpg` |
| Reading Figma text | Text layers are **named after their content**, so metadata returns the copy without needing a screenshot. |
| **ProSure file** | `uiFMtBP008pIHKLgtwwLY0` holds the portfolio case-study frames: Kingdom OTT `241:20349`, SPRE `241:19898`, ICICI Ozone `241:20128`. Build a page with `FIGMA_CACHE=<dir> python3 tools/build-case.py <slug>`; slugs and links are set in its `PAGES` table. **API limits:** the account is on Figma's Starter tier; heavy `geometry=paths` requests can be refused for days (`Retry-After` ≈ 4.6 days on 5 Nov 2026). The script then falls back to the plain layer tree plus each vector exported as SVG. |
| **Loading experience** | `python3 tools/add-ux.py` injects it into every `home/` page (idempotent; `build-case.py` runs it). Loader overlay tied to the first screen's images and fonts, never more than 4s; case-study images lazy-load behind a shimmer (url kept in `data-bg`); page cross-fades; hover prefetch; on case studies a reading-progress bar and back-to-top button; Open Graph tags with a per-page `og.jpg` (`--og` re-renders them). Images ship as WebP via `tools/webp.py` (Chrome's encoder; site went ~117 MB → ~19 MB). Asked for 5 Nov 2026: *"generate experience for user while they are on this portfolio and case studies"*. |
| **Mobile (decided 5 Nov 2026)** | Case studies reflow automatically below 768px, generated from the desktop page by `node tools/mobile.mjs [slug]`: article text (18px+, or 13px+ passages) as real HTML; layers covered by others skipped; visuals split into stacked rows/columns and captured at up to 2× into `m/`. The layout is generated, not a Figma design. **Rebuild order:** `build-case.py` (runs add-ux + webp) → `mobile.mjs`. |
| **Analytics (decided 5 Nov 2026)** | GoatCounter — free, cookieless, no consent banner. This is the one sanctioned exception to "no external requests", for the `home/` portfolio pages only. Needs Dhanesh's GoatCounter code. |
| **Figma access** | The MCP server needs an **editor seat** on the team that owns a file. Dhanesh has a Full seat only on **CoverSure**; `Portfolio` (`8LqFO4NjyttqYMYpracfd0`) sits on a View-seat team, so the MCP refuses it &mdash; this is a seat problem, not a sharing one. **The REST API only needs view access**, so use `./tools/figma-fetch.sh <file-key> <node-id>` with a personal access token in `~/.figma-token`. That path works on every file he can open in a browser. |

---

## 8 · Repo map

| File | What it is |
|---|---|
| `index.html` | The whole case study — ten versions in one self-contained file, no build step, no external requests |
| `CONTEXT.md` | This file — the standing brief |
| `PROJECT-LOG.md` | Chronological record: feedback, fact-finding, decisions, corrections, deployment |
| `COPY-V10.md` / `COPY-V9.md` | Every word of that version, surface and *See more* |
| `build-copy.py` | Generates `COPY-<V>.md` from the live markup, so copy docs cannot drift |
| `build-scan.py` | Regenerates `scan/index.html` from the scan panel |
| `measurement/` | How to test whether the engine works — hypotheses, metrics, 26 send-ready questions |
| `tiimo-teardown/` | Competitive teardown, claims tagged observed / reported / inferred / assumed |
| `tiimo-teardown/interaction/` | Companion: ten teardown findings answered as interaction patterns, plus a working day-planner prototype. See §16 |

**Version tabs** are driven by `VIEWS` and `DEFAULT_VIEW` in the script block; each panel is
`#panel-<key>` with a matching `#tab-<key>`, deep-linked by URL fragment.

**Before any publish**, run: tag balance · duplicate ids · SVG markers resolving inside
their own panel · no colour literals outside the token blocks · every tab wired to a panel ·
every `data-open` resolving · no undefined classes · the scan test.

**SVG markers must be defined inside the panel that uses them** — referencing another
panel's marker breaks when that panel is hidden. Give every panel its own prefix.

---

## 9 · Open — waiting on Dhanesh

1. **Annotation cards 03 and 04** read almost identically ("show health and life with
   recommended cover and premium as per risk report"). They were merged in V10. If they are
   genuinely different states, what separates them?
2. ~~Body font~~ — **settled 6 Oct 2026.** Dhanesh asked for Apple design guidelines, so
   Charter serif was replaced by the SF Pro system stack across the whole artifact. See §10.
3. ~~The five-colour signal rail~~ — **moot.** It lives in V9's rules table; V10 never
   carried it.
4. **Real numbers** — visit frequency, dead-click counts, and the dead-click baseline
   export. **Time-sensitive:** session-replay retention is 30–90 days.
5. **Older versions carry corrected copy.** "Engagement rises" still appears in V6 and V7;
   "nothing here was newly built" in Compact. Fix them, or keep them as an honest archive?

---

## 10 · Design language — Apple, applied 6 October 2026

Dhanesh: *"use apple design guidlines and design styling and make design clean and easy to
visual and stunning."* Applied to the **global tokens**, so every version stays coherent
rather than V10 looking like a different product.

**Typography** — SF Pro via the system stack (`-apple-system, BlinkMacSystemFont,
"SF Pro Display"/"SF Pro Text"`), replacing Charter serif and Avenir Next Condensed. Body is
Apple's 17px / 1.47 with −0.01em tracking. Headlines are weight 600 with negative tracking
that grows with size — −0.022em at title scale, −0.028em on the V10 hero, which runs to 80px.

**Palette** — Apple's neutral greys, replacing the blue-tinted custom set.

| Token | Light | Dark |
|---|---|---|
| `--ground` | `#ffffff` | `#000000` |
| `--ground-2` / `--surface` | `#f5f5f7` / `#ffffff` | `#1d1d1f` |
| `--ink` / `--ink-2` / `--ink-3` | `#1d1d1f` / `#424245` / `#6e6e73` | `#f5f5f7` / `#a1a1a6` / `#86868b` |
| `--rule` / `--rule-soft` | `#d2d2d7` / `#e8e8ed` | `#424245` / `#2c2c2e` |
| `--accent` | `#0071e3` | `#2997ff` |
| `--signal` | `#bf4800` | `#ff9f0a` |

**Shape** — version tabs and the See-more affordance became 980px pills; cards, figures and
tables went to an 18px radius, inner blocks to 14px; screens are lifted by a soft shadow
rather than outlined. Separation is by space and tone, not by hairline.

**Still carrying old colour literals:** the navy stage and the KYP greens in V4–V7 use
hardcoded hex values outside the token blocks. They were left alone — those versions are an
archive, and rewriting them risks breaking a look that was tuned by hand. The theme audit
flags them as a known warning, not a regression.

### Wayfinding — added 7 October 2026

Eleven sections is more than a reader holds in their head, so V10 gained two devices:

- **The section tag sticks** while its own section is in view, so the number and name stay
  in the left gutter as you read.
- **A live section index** floats in the right gutter above 1280px. At rest it is only
  numerals wide, so it never reaches the text column; labels open on hover and are allowed
  to overlay, the way a tooltip does. The active section is tracked with
  `IntersectionObserver` and marked `aria-current="step"`. Below 1280px it is hidden
  entirely rather than crowding a narrow screen.

**Note for future edits:** V10 sections now carry `id="v10-s1"`…`id="v10-s11"`. Anything
matching on the literal string `<section class="v5-sec">` will miss them — match
`<section class="v5-sec"[^>]*>` instead. `build-copy.py` was fixed for exactly this.

---

## 11 · Copy direction — set 7 October 2026

Dhanesh, on what the copy is for:

> *"i want that founders and product lead understand my strtergy and skill set and my thinking
> so content need to be follow this than fluffy text. copy need to be give understanding of
> project"* … *"make content in human voice than robotic and too machanic"*

Three rules follow from that, and they pull against each other on purpose:

1. **Strategy over description.** A founder reads for the thinking, not the feature list.
   Where a real call was made, it is shown as a **decision block** &#8212; what was chosen,
   what was rejected, and why. Five of these sit in V10: §02, §05, §06, §08, §09. Reasoning
   as structure survives scanning; reasoning as paragraph does not.
2. **Human voice.** First person, plain words, the way a designer talks. Watch for the
   mechanical tic this copy keeps falling into: *"X was only A. I made it B."* repeated
   section after section. One or two of those reads deliberate; eleven reads like a
   template.
3. **Nothing decorative.** Every sentence carries a fact, a decision or a reason.

**The honest trade.** Cutting prose and writing in a human voice work against each other
&#8212; a natural sentence is longer than a clipped one. The V10 surface held 2,366 words
before this pass and 2,350 after. What changed is the *shape*: prose fell 32% (987 to 673
words) and structured content rose to 67% of the surface. Do not claim a word-count
reduction that did not happen.

**Where cut prose goes.** Into the *See-more* panel for that section, never deleted. The
See-more layer grew from 2,356 to about 3,000 words in this pass. Depth is opt-in; the
surface stays scannable.

**The reading-time line is measured, not estimated.** It currently reads *"3 min to scan,
10 to read in full"*, from an actual word count at 230 wpm. It previously claimed ~4 min
for a 10-minute page. Re-measure it whenever the surface changes.

---

## 12 · V11 — motion that explains, added 11 October 2026

Dhanesh: *"can we add mosion and animation to present those graphs and tables and screens so
user understnad in easy way without additional text and screens"*.

**The rule this version is built on:** every animation replaces a sentence. Nothing moves
for decoration. If a motion cannot be justified by the copy it lets you delete, it does not
belong.

**The engine simulator (§04)** is the centrepiece. One phone frame, six states from the real
rule set, auto-advancing every 3.6s with clickable markers and a Pause control. Each state
sets the primary action, both pitch slots, and which of the fixed slots exist &#8212; so you
watch the Insurance-on-Card slot vanish once a card is added, and Download wake up the moment
a policy lands. It replaced **four static screens and the six-card grid, 253 words**, and it
proves the sequence rules from §05 at the same time.

**The other four:** flowing connectors on the gap (§02), the pipeline (§03) and the sequence
(§05); the ladder climbing its gates (§06); and the family matrix driven by its own two
switches (§07), where toggling *policy added* and *family member added* moves the highlight
and flips the Download chip.

**Non-negotiables, all implemented:**

- `prefers-reduced-motion: reduce` stops everything. The simulator does not auto-advance,
  shows state 1, and its control reads **Play**.
- Nothing animates off screen &#8212; `IntersectionObserver` gates every loop, so a reader
  parked in §09 is not burning cycles on §02.
- Every state is reachable without waiting: click any marker.
- The phone frame is `aria-hidden`; the state label is a `role="status"` live region.

**Result:** V11 has no static screens in §04 at all. V11 is the default view; V10 remains as
the static telling, which is the better choice for PDF export or anywhere motion will not run.

> **Correction, 12 October 2026.** This section originally claimed V11's surface was *"2,120
> words against V10's 2,347"*. **That was wrong.** The measuring script stripped `<svg>` before
> counting, so ~470 words of diagram labels were invisible, and the simulator's state copy lives
> in the script block rather than the panel, so another ~270 were never seen at all. Counted
> like for like, **V11 is roughly 40 words heavier than V10, not 227 lighter.**
>
> `build-copy.py` had the same blind spots plus a third: no handler for `dl.v10-dec`, so **all
> five decision blocks were missing from `COPY-V11.md`** — a file whose own header claims it
> "cannot drift from what is published". Fixed 12 Oct; the copy doc went from 5,273 to 5,949
> words.
>
> **The lesson for any future measurement here:** the surface is not just `<p>` tags. It is SVG
> `<text>`, table cells, `<dt>`/`<dd>` pairs, and copy that lives in JavaScript. Count all of it
> or do not quote a number.

---

## 13 · Review of V11, and what was applied — 12 October 2026

Full report: [`REVIEW-V11-2026-10-12.md`](REVIEW-V11-2026-10-12.md) ·
<https://dhanesh100.github.io/Case-study/review-v11/>

**The finding:** V11 was not too long, it was badly weighted. 35 bold runs of prose across 11
sections meant the scan layer ran 511 words (2m13s) for an audience that gives 60 seconds. And
the best thinking sat in *See more* panels a scanning founder never opens.

**Applied:**

- **One bold claim per section.** 35 prose bold runs &rarr; **11**. Scan layer **511 &rarr; 243
  words = 63 seconds.** No copy left the page; it stopped competing.
- **All eleven headings rewritten to argue rather than describe.** §10 was the only one that
  announced a topic (*"What changed in the product."*); it now reads *"No numbers yet. Here is
  what would disprove the claims."*
- **Three accuracy fixes**, all unevidenced claims: §01's *"the one screen almost everyone
  visits"* (frequency, no data), §05's *"Users stop scanning it and start ignoring it"* (asserts
  user behaviour &mdash; fixed on the surface **and** in the §05 See-more panel), and §10's
  *"More exploration&hellip; is the intended effect, not a measured one"* &mdash; **deleted, not
  unbolded**, because the hedge does not retract the outcome it plants and §6 already forbids
  that shape.
- **Two duplicates removed:** §02 said *"Portfolio is where they land"* twice in one section, and
  §09's decision block repeated what its new heading now says.

**Also fixed in V10**, because V10 is not an archive &mdash; it is the version actively
recommended for PDF export and anywhere motion will not run. The same three unevidenced claims
were corrected there, leaving its headings and bolding alone (those are V11's identity).
**V9 and below still carry *"More exploration&hellip; is the intended effect"*** and remain a
genuine archive &mdash; open item §9.5 still applies to them.

**Not yet applied &mdash; the four show-don't-tell builds:** §05's table as a live deck, §03's
signal toggle chips, §10's empty dashboard, §11's pipeline coloured by ownership voice.

**Defended against the reviewers, and why:** §05's shipped card copy (the only shipped-product
evidence on the page), §03's eight rule rows (the only place the non-pitch *Add your policy* card
appears), the simulator's reasoning lines, and §07's *"rather than in the pitch band"* (the only
named rejected placement). 30 verification agents challenged every proposed cut; most were
rejected for costing design evidence. **That rejection list is part of the output.**

---

## 14 · V12 — compact, added 15 October 2026

Dhanesh: *"make understanding much more easy to founder, and quick overview when they scan
portfolio, understand my stratergy, UX and skill … understanding with less reading … otherwise
chances are they will skip if there is more reading. we can explain inside more information
page in each section … create version that hit hard with compact"*.

**Shape.** Eleven sections became **six beats** — Problem · System · Strategy · UX · Restraint ·
My role. Each beat is: one arguing H2, one line with one bold claim, **one visual**, a row of
*Shown* skill chips, and one **See …** opener.

**The hero does the 60-second job on its own:** headline, a two-sentence standfirst, four fact
tiles (5 signals reused · 0 new data asked of users · 10 rules, one of them "show nothing" ·
1 primary action per state), three "in one minute" cards (gap / strategy / system), and a
**What this shows** row of skill chips that jump to the beat proving each one.

**Visuals.** §01 is a Before/After flip — five sources stopping short vs. one engine wiring
them into Portfolio. §02 is the V11 simulator (shared code, not a copy) plus a generic vs
CoverRisk pitch pair. §03 the ladder. §04 a slot stack where only the engine band animates,
plus two real screens (member chips, KYP scale). §05 two mini phones and a struck-out
"kept out" list.

**Nothing was deleted.** Every V11 See-more panel, the rule table, the slot copy table and all
five decision blocks moved into the six V12 overlays (`v12-ov-1`…`6`).

**Measured, like for like** (panel markup minus scripts and aria-labels, SVG text included):
V11 surface **2,604 words → V12 851**, about a third. The simulator's state copy lives in
JavaScript in both and is excluded from both.

**Shared code.** The V11 motion CSS is now scoped `:is(#panel-v11, #panel-v12)` and the
simulator script builds every `[data-sim]` in either panel. Edit one, both change.

**Defaults.** `DEFAULT_VIEW` is `v12`. V11 stays as the full motion telling; V10 stays the
static one for PDF export.

## 15 · Portfolio site (`home/`) — Figma sources, set 7 November 2026

- Get In Touch popover: ProSure `uiFMtBP008pIHKLgtwwLY0` node `249:20848` (copy of Portfolio
  `154:37340`). Built once in `home/pop.js`; `tools/add-ux.py` loads it on every page and it opens
  from **every** "Get in touch" button on every page, whatever its href (header, phone header, case-study
  CTA banners — the banners were mailto: until 7 Nov 2026, Dhanesh wants them on the popover).
- Case studies: Kotak = Portfolio `140:4208`; Shoppers Stop = ProSure `240:3236`; Invesco = ProSure `241:16776`.
- Phone layout must hold at 412px wide (Dhanesh's test width).
- Shoppers Stop header nav — all eight items live (Figma dims the last four; Dhanesh asked for them mapped):
  Overview → See How We Transformed · Product Story → Product Story · Strategy → Challenges ·
  SS Home → Beyond a Single Frame · Product Detail → Recommendations (product-level personalisation) ·
  Bargain / LUX → Explore Sections row, scrolled to the bargains Store / Everyday Luxury card ·
  Cart → Turning Likes into checkouts. The case study has no dedicated PDP or cart design.
- Sideways rows run edge to edge (full 1440) with the 48/54px inset kept as scroll padding; anything laid
  out wider than the canvas in Figma is made scrollable, never cut off. Long rows get a nudge (peek or
  auto-scroll that pauses on any user input); phone screens peek upward and carry a "Scroll" chip.
- Interaction rules, set 9 Nov 2026, all in `tools/add-ux.py` so a rebuild keeps them:
  - Every `:hover` rule in a page's own CSS is moved behind `@media (hover:hover) and (pointer:fine)` by
    `gate_hover()` on each run, so a tap on a phone never leaves a card grown. Write hover rules normally;
    the script gates them.
  - A failed image stops shimmering, is retried once after 4s, and again on reconnect.
  - Every screen recording gets a pause/play button (WCAG 2.2.2); a user's pause survives scrolling away.
    Under reduced motion recordings don't autoplay and the button is the opt-in.
  - Self-moving things stop for good once the visitor takes over. The Shoppers Stop Explore row
    stops after a drag, wheel, touch, arrow, focus or header-nav jump, matching the phone peek; mouse hover
    only pauses it.
  - The Get in touch popover makes the page behind it `inert`, plays its exit (it used to cut), and
    leaves faster than it arrives.

---

## 16 · Interaction pass — 9 November 2026

Dhanesh: *"understand motion design, small interactions, interactions, animations, error states, edge
cases, haptic, loading, accessibility, user experience … make this todo list app improve … use repo and
connectors and skills and plugins … to improve this case studies."* "This todo list app" was read as
**Tiimo**, the only to-do app in the repo.

**Tiimo companion page** (`tiimo-teardown/interaction/`). Ten teardown findings, each answered with an
interaction pattern, plus a prototype day planner with eight states (5-min cue, finish, miss, overrun,
offline + calendar conflict, AI draft, slow AI, back after a week) and four access switches (reduce
motion, larger text, no colour, haptics). It keeps the teardown's evidence rules:
- **It is not a redesign of Tiimo's screens.** The teardown never saw them. The prototype's visual
  language is deliberately its own, and the page says it is not affiliated with Tiimo.
- Each pattern carries its finding's evidence tag. Where a finding is reported or unverified, the
  pattern is a hypothesis to test, not a correction.
- The motion tokens in the spec are the ones the prototype runs on: standard `cubic-bezier(.2,0,0,1)`,
  enter `(.23,1,.32,1)`, sheet `(.32,.72,0,1)`; 120 / 240 / 360 ms; linear only for the time bar;
  no overshoot anywhere.
- iOS haptic API names are the real ones (`UIImpactFeedbackGenerator` `.soft/.medium/.light`,
  `UINotificationFeedbackGenerator .success`, `UISelectionFeedbackGenerator`). Outside the app iOS
  allows no custom patterns, so the page says the cue rides on a Time Sensitive notification.

**Main case study (`index.html`), from a motion and accessibility review of V11/V12:**
- **The version bar wrapped to 654px tall on a 375px phone (525px at 412px)** and stayed stuck over the
  page. It is now one scrolling row, 71–75px at every width, fading at the right edge while more tabs hide.
- V12 scrolled sideways on phones (the beats grid sized itself to a 620px diagram). Fixed.
- **Pause motion** button in the version bar, on V11/V12 only, remembered per device: stops the
  simulator, band, before/after, flows and ladder (WCAG 2.2.2). Hidden under reduced motion.
- Simulator: its live region no longer announces every 3.6s; under reduced motion, Play now opts in;
  loops stop in hidden tabs.
- Touch targets to 44px (simulator markers, Pause, "See …" openers, overlay close, segments).
- Comma-mangled selectors had hidden **every V10 section-index link**; fixed, and the labels now open on
  keyboard focus too.
- Deep links into a version (`#v11-s4`) open that version. Jumps move focus. Overlays make the page inert.
- All `:hover` rules gated to pointer devices, using the same `gate_hover()` as the portfolio.

**Connectors.** Google Drive returned *insufficient scope* when searched for the dead-click numbers
(§9.4), so it needs re-authorising in claude.ai connector settings before it can help. Figma was not
needed for this pass. Image generation (Magnific) was deliberately not used: generated screens would
break "real over impressive".

---

## 17 · The everyday layer — 9 November 2026

Dhanesh: *"while explaining, use examples that in real life or everyday related to user understand that
better, we can use those in diagram and make diagram animated or interactive that showcase everything at
once, unfold everything with interaction or animation."* Applied to **V12 in place** (the default view),
not as a V13.

**One analogy world: the car.** Everyone has sat in one, and its parts map onto the engine without
forcing. Keep this mapping when adding or editing anything in the layer:

| CoverSure | Car |
|---|---|
| Onboarding — what they told us | Your settings — what you told it |
| Policy data — what is actually stored | Fuel gauge — what is actually in |
| CoverRisk — cover needed, at what premium | Service report — what it needs, at what cost |
| Family data — who depends on them | Seat sensors — who is on board |
| Know Your Policy — how good each policy is | Wear check — how good the parts are |
| Recommendation engine, ten rules | Order of importance |
| Tier 1 · Health **and** term life | Brakes **and** seatbelts |
| Tier 2 · Super Top-Up, Critical Illness | Extra airbags, ABS |
| Tier 3 · PA, Hospicash, Home, Device — only with a reason | Child seat, roof carrier — only with a child or a trip |
| Health only → term life next, not Super Top-Up | Brakes fine, seatbelt faulty → seatbelt first, not an airbag upgrade |
| "Buy Life policy" vs "Buy ₹1 Cr life cover · ₹80/month" | "Low fuel" vs "Low fuel · 38 km left" |
| Fixed slots, one engine band | Speedometer never moves, only the message strip changes |
| Nothing fits → nothing promoted; no offer above your policies | All fine → blank; nothing covers the speedometer |

Two examples sit outside the car on purpose, because they fit better: **beat 05** contrasts the
supermarket that puts milk at the back so you pass the offers, and **beat 06** uses a sat-nav (I built the
routing; Product owns the map). The dead click is told as wiper and indicator stalks shaped alike, inside
the beat-01 overlay only — the engine stays the subject.

**What was built.**
- **00 · The idea in one picture** (`#v12-s0`), first in the beats. A car row above a Portfolio row, through
  the same three columns (Already known → Decides → Shows), so the whole engine and its everyday twin are
  on screen at once. Six steps unfold it: already known · one message · order · specific · frame · quiet.
  Each step dims what is not part of it (never hides it), changes the one moving message, and shows a
  caption with "In a car" and "In Portfolio" side by side plus a link to the beat that proves it.
- **Ladder lens** on beat 03: *CoverSure | In a car* swaps the labels, not the structure.
- **One "Everyday" line** under each of the six beats (green pill).
- **Colour:** green = everyday (`--life`, `--life-soft`, `--life-ink`, added to all three token blocks),
  blue = CoverSure.

**Motion rules for the picture.** It walks the six steps once (6 s each, a linear timer hairline on the
active step) when it scrolls into view, then rests on *All* and offers *Replay*. It auto-plays only when
the whole picture fits on screen — on phones it is taller than the screen, so *Play* is the opt-in. It
stops for good once the reader picks a step, presses Pause or follows a link. Nothing runs off screen, in
a hidden tab, under Pause motion, or under reduced motion. The live region speaks only for steps chosen by
hand. Captions are real HTML: without script, every caption shows as a list.

**Measured, same method both times** (panel markup minus scripts, overlays and attributes): the V12
surface went from **806 to 1,541 words**. Most of the increase is step captions and message variants that
show one at a time: at rest, section 00 shows **244 words** on screen, and the six everyday lines add
**121**. This is a real cost to a version built to be compact; it was the trade asked for. Do not claim
V12 is still ~850 words.

**Checks:** 39/39 on the new layer (1440, 375, 412, reduced-motion dark), the 44/44 case-study suite
still passes, structure checks clean.

---

## 18 · How UI is presented — set 9 November 2026

Dhanesh: *"UI screens and components use in case study were amature … dont need to add mobile full
screen everywhere … for small component, add full mobile screen is lack of interface understanding."*

**The rule.** Show a component as a component, at its own size, on the app's own background. Show a
whole screen only when the claim is about the whole screen. No device chrome, no status bar, no Figma
canvas, no arbitrary crops of a long screenshot.

**Applied to V12** (the default):

| Beat | Was | Now |
|---|---|---|
| 02 pitch pair | Two HTML text boxes | The two shipped cards: *Buy Life policy* and *Recommended · Buy ₹1 Cr life cover* |
| 04 fixed frame | An HTML stack of grey boxes | The shipped bottom section (Insurance on Card, engine band, Download, Found 2 inactive), each slot's rule on a leader line beside it; the band swaps shipped cards at a fixed height |
| 04 member chips | The top of a full phone screenshot | The chip row and the member card's policy row, tagged *switches person* / *opens in place* — the two controls the dead click confused |
| 04 KYP | The raw component-set capture (grey canvas, Figma's dashed selection border) | The shipped policy card; pick Great / Good / Average / Poor / Not yet and the real rating component is laid over the card's own rating |
| 05 restraint | Two schematic mini-phones | The real components in both states: policy card on top, engine card below; the Add-your-policy block on top, engine card below |

**Older versions:** the rating-scale image they all share was rebuilt as a clean sheet from the five
exported variants, so V4–V11 lose the grey canvas and dashed border too. Their other screens are unchanged.

**Sources.** Exported from Figma `x1YQ5nU9BirfL1IW8CHd20` at 2x: bottom-section cards from
**Component 351** (`10410:56686`, the later of two sets with identical copy — 344 is the older one); policy
card `I4919:28497;2140:22309`; KYP variants `2129:17150 … 17298`; chips and tabs `4919:28403`;
Add-your-policy block `6527:21460` (from frame `3526:37129`). The member card was cropped from the 2x
`assets/src/family-overview.png`. Embedded as WebP; the page grew by about 0.4 MB.

**Canvas tokens.** `--ui-canvas` is `#f7f7f7`, sampled from the app's own background. The `--ui-*` tokens
are defined once and **not** overridden for dark mode: the app has no dark mode, so its components sit on
a light canvas in both themes.

**Price correction.** The shipped *Recommended · Buy ₹1 Cr life cover* card says **₹500 per month**.
V12 had quoted ₹80 (the generic card's floor). Fixed in V12's surface, the car picture and the shared
simulator. **V11 and V10 still pair ₹1 Cr with ₹80** in their pitch cards — open.

**Figma rate limit.** The REST API returned 429 with `Retry-After` ≈ 4.6 days after this pass's
exports (Starter tier, same as 5 Nov). Further exports wait until about 14 Nov 2026, or use the MCP.


# CONTEXT — read this first

**Purpose.** Everything a new session, a new collaborator or a future me needs before
touching this repo, so Dhanesh does not have to explain it again. `PROJECT-LOG.md` is the
chronological record of what happened. **This file is the standing brief.**

Last updated: 5 October 2026 · current version: **V10**

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
| Reading Figma text | Text layers are **named after their content**, so `get_metadata` returns the copy without needing a screenshot. |

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

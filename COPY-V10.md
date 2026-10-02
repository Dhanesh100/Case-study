# CoverSure Policy Portfolio — V10 copy

Every word on the page, surface and *See more*.
**Generated from the live markup by `build-copy.py`, so it cannot drift from what is published.**

**Live:** <https://dhanesh100.github.io/Case-study/#v10>

---

## Hero

**Headline** — Making Portfolio respond to the user — not just display their policies.

**Product context** — CoverSure is an insurance aggregator — but it starts before the marketplace, by helping people understand the cover they already hold and what they actually need. Policy Portfolio is where they store and manage it.

**Standfirst** — I built a contextual recommendation engine that uses information CoverSure already has about a user to surface the most relevant feature, product or next action inside Portfolio. The Portfolio’s core job stayed the same; the new layer made it connected to the rest of the product.

**Meta** — Product Designer·Post-MVP ·Policy Portfolio Shipped

### One-screen summary

**One Portfolio. Many user states. One contextual recommendation layer.**

- **01 — Existing product context** — Onboarding, policies, family data, CoverRisk, sync and KYP already contain useful signals.
- **02 — Recommendation engine** — Six conditions decide the primary action; a fixed four-slot order decides where it sits.
- **03 — Connected experience** — Portfolio becomes a gateway back into the right CoverSure feature or product — without changing its primary job.

The work was not adding more features to Portfolio. It was building the system that makes the features we already had work together.

**Honesty note** — Recently launched, so quantitative results are not yet available — §10 states what changed, not what it achieved. Coverage figures and priority bars in the screens are illustrative design placeholders, not customer data or measured values.

**How to read** — Eleven sections · ~4 min· Titles carry the argument · each See link opens the reasoning behind one

---

## 01 · The trigger

**Title** — A dead-click issue exposed a bigger opportunity.

**Lead** — The work started with a dead-click issue — taps that did nothing, leaving users stuck in a loop. I fixed that route. But it exposed something larger: Portfolio was a high-value surface where information from the rest of CoverSure could make product discovery far more relevant.

- **Dead clicks** — Taps that produced no result — users trying to reach Policy Details, stuck repeating the same one.
- **Support** — The route sometimes had to be explained on the call.
- **B2B onboarding** — The same confusion observed directly, with real users.

**Diagram** — Before: the entry point into the policy listing and the expand-and-collapse beside it were styled identically, so taps landed repeatedly on the control that only revealed detail in place. After: a member chip gives profile switching its own affordance, reaching the policy in one tap.

*Caption* — Two controls, styled the same, doing different jobs. One revealed detail in place; the other was the way through. Taps landed on the first and produced nothing.


### See more — The trigger: “Where the confusion actually was.”

**The route existed. It did not look like one.**

The route to Policy Details was there, but the interaction beside it looked like the route. Expand/collapse revealed information in place; it did not communicate navigation.

**Three signals pointed at the same step**

Dead clicks, support calls, and B2B onboarding observations. Three independent sources naming one interaction is what made it worth fixing rather than debating.

**The fix was deliberately narrow**

Separate the navigation job from the expand/collapse job. The Portfolio architecture did not change. Member-level navigation became explicit, while expand/collapse stayed responsible for revealing information in place.

**Why it is here at all**

I fixed the navigation defect. The contextual recommendation work was the larger product opportunity that came next — and it is the rest of this case study.

---

## 02 · The opportunity

**Title** — Portfolio already had the traffic. The rest of the product already had the context.

**Lead** — People do not browse an insurance app. They open it for a renewal, a document, a claim — and Portfolio is where most of those visits land, which makes each one a rare chance to be useful. CoverSure held information about policies, family, risk and user intent across other features, and none of it was being used here. I proposed connecting it.


**Diagram** — On the left, three reasons people open the app — a renewal, a document, a claim — all land on Portfolio. On the right, five existing sources of context: onboarding, CoverRisk, family data, Know Your Policy and the buying journeys. A dashed line runs between the two sides and every connection from the right stops short of it. No system carried context across to the surface where the visits landed.

*Caption* — Both sides already existed. Every line from the right stops short — no system decided what should appear for this user, at this moment. The gap is the opportunity.


**Note** — The opportunity was not to build another feature. It was to build the layer that connects what already existed.


### See more — The opportunity: “Why Portfolio became the connection point.”

**Where it sits**

Portfolio sits between several parts of the product: Onboarding → Homepage → Portfolio → Policy Details.

Onboarding knows what the user says they already have. Policy data shows what is actually stored. CoverRisk describes protection needs. Family data shows household completeness. KYP explains policy quality.

**What I proposed**

Keep Portfolio’s existing architecture and primary job, then add a contextual recommendation layer on top.

The layer reads existing context, evaluates conditions, prioritises competing opportunities, surfaces the most useful action, then reads the new state after the user acts.

**Why this surface**

Portfolio became the connection point not because it needed more content, but because it already had the right context and the user’s attention.

---

## 03 · The engine

**Title** — I built a contextual recommendation engine, not a banner system.

**Lead** — The engine maps existing user context to the most relevant feature or product action. The recommendation engine is new; the intelligence it uses already existed. Nothing like it existed anywhere else in the app — this is CoverSure’s first contextual layer.

| Context | Primary | Secondary | Reason |
|---|---|---|---|


**Diagram** — Five existing signals — onboarding, policy data, CoverRisk, family data and Know Your Policy — feed conditions, which pass through priority to produce one action. Acting changes the user state, which feeds back into the signals and closes the loop.

*Caption* — No rule fires on a single fact. Each weighs what is known about the user, how much a product matters in a life, and whether they already hold it — then priority breaks the tie, and acting rewrites the input.


**Note** — Eight of ten rules shown. The last one is the constraint that keeps the engine from becoming a better-targeted banner stack.


**Note** — No rule fires on a single fact. Each weighs what we know about the user, how much that product matters in a life, and whether they already hold it — which is what stops the engine recommending something they own, or something that does not apply to them.


### See more — The engine: “How the recommendation engine decides what appears.”

**The first of its kind in the product**

No part of the app had a contextual layer before this. That shaped how it was built: the rule set had to be legible to the people who would maintain it, and generic enough to survive a catalogue that keeps growing.

**Every rule has three parts**

Condition — something the product already knows. Priority — what should win if several conditions are true. Action — the single most useful next step for that state.

**State is composed, not picked**

Users arrive with different combinations of policies, CoverRisk status, family data and onboarding answers. The Portfolio state is composed from whatever is true at that moment.

When multiple conditions fire, recommendation priority breaks the tie. The engine surfaces a primary action and, where useful, one secondary action.

**The two remaining rules**

Health only → term life. The foundation is not complete until both exist, so the engine finishes it before extending anything. Term life only → health, for the same reason.

Super Top-Up and Critical Illness only become the next step once health and term are both in place. The ladder does not skip a rung because the next product is easier to sell.

**The constraint that matters most**

When nothing is relevant, nothing new is promoted. Portfolio stays focused on policy management.

Without this constraint, a contextual engine becomes a better-targeted banner stack. The recommendation layer only adds value if it protects the primary job of the screen.

The engine is not deciding what CoverSure can sell. It is deciding what is relevant to this user now.

---

## 04 · The rule set

**Title** — Here is the actual rule set, not a description of one.

**Lead** — Three inputs decide every recommendation: what onboarding was told, what is actually stored in Portfolio, and whether CoverRisk has run. Those three produce the primary action and everything pitched below it. No rule needs data the product does not already hold.

**01 · Said health and super top-up. Added neither.**

- *Primary* — Add policy
- *Pitch* — Life, then Critical illness
- *Why* — Nothing is stored, so there is nothing to rate or review. The engine asks for the policies it was already told about, and pitches the next rung up.

**02 · Said no policies. CoverRisk has not run.**

- *Primary* — Check risk score
- *Pitch* — Health, then Life
- *Why* — No stored cover and no number to personalise with. The score answers how much; the two foundational covers follow it.

**03 · Said no policies. CoverRisk has run.**

- *Primary* — Buy health, then life — carrying the recommended cover and premium from the report
- *Why* — The score already answers how much. A starting number beats a generic offer, because the right amount matters more than the right product.

**04 · Said health and term. Added health only.**

- *Primary* — Preview the stored health policy
- *Pitch* — Add term policy, then buy Critical illness
- *Why* — One named gap, so name it. The moment any policy lands, Download becomes active — the engine changes more than the pitch.

**05 · Said health, life and motor. Added one.**

- *Primary* — Add the remaining policy types
- *Pitch* — Super top-up, Personal accident
- *Why* — Several gaps rather than one, so the prompt names types, not a single policy. Naming one would hide the others.

**06 · Said health and motor. Added all of them.**

- *Primary* — Review the stored policies
- *Pitch* — Life, then Super top-up
- *Why* — Nothing left to add, so the engine stops asking and moves up the ladder instead of repeating itself.

- **Generic pitch** — Buy Life policy A product name and a button. The user still has to work out how much cover they need, which is the part they are least sure about.
- **Where CoverRisk has run** — Buy ₹1 Cr life cover From ₹80/month. The recommended cover and the approximate premium both come from the report the user already completed. I connected that intelligence — I did not add a second assessment.
- *Screen · none* — State 02Nothing stored, no score — CoverRisk leads
- *Screen · pending* — State 01Declared but not added — Add policy leads
- *Screen · member* — State 04One of two stored — review leads, the gap is named below
- *Screen · group* — Employer cover onlyFoundational protection still missing

**Note** — Read down the Primary column and the whole strategy is visible: ask for what is missing before selling what is next. The engine sorts by what the user already holds and what is required after it — never by what is easiest to sell.


**Note** — Same layout in all four. Personalisation happens through state, not through a different screen per user.


### See more — The rule set: “Every state resolved, including the ones nobody screenshots.”

**The three inputs, and nothing else**

Every rule reads from the same three places: what the user declared during onboarding, what is actually stored in Portfolio, and whether CoverRisk has produced a report. All three already existed. No rule required new data collection, which is why the engine could ship without a data project behind it.

**The two global rules that sit over all six states**

Insurance on Card stays pinned to the top until the user adds a card, then the slot is removed permanently. It is the only recommendation with a terminal state.

Download stays inactive until the first policy is stored. Offering an empty file would be worse than offering nothing.

**Where CoverRisk changes the pitch**

CoverRisk already held age, location, family, dependants, health, lifestyle, income, investments, property and expenses. The recommendation layer did not ask the user for any of it again.

The chain is: CoverRisk report → recommended coverage → estimated premium → the buying action, carrying both numbers.

The product decision underneath was where the intelligence should continue. A report should not be the end of the journey when the next decision still depends on it.

**The states users meet but showcases skip**

Employer cover only — no yearly premium shown, because the user does not pay it.

Rating unavailable — a coming-soon band, so missing KYP data never reads as a poor rating.

Family member without policy — the prompt stays on that member’s own card, where the gap is visible.

Lapsed policy — surfaced as something needing attention rather than hidden.

Renewal due — Review Report or Pay Without Review, so the choice is informed.

**Why this is the real work**

The quality of a recommendation system is decided by the states that are not the happy path. Each one is a condition that had to resolve to something honest, and each one was a decision about what the product is allowed to claim when it does not know enough.

---

## 05 · The sequence

**Title** — The contents change. The slots do not.

**Lead** — A recommendation engine makes a screen unpredictable unless something holds still. I fixed the order of the bottom section and let only one band vary — so someone returning finds the same shape, carrying different contents. Predictability is what separates a recommendation layer from a feed of offers.


**What each slot actually carries**

| Band | Card | What the card says |
|---|---|---|
| Always top | Insurance on Card | Discover free insurance in your debit or credit card |
| Engine band | Buy Health policy | From ₹200/month · Stay ready for medical surprises |
| Engine band | Buy Life policy | From ₹80/month · Keep your family secure, always |
| Engine band | Buy Super Top-up | From ₹299/month · When bills go beyond your cover |
| Engine band | Buy HospiCash | From ₹35 one time · Daily cash support of ₹1,000 when hospitalised |
| Engine band | Buy Personal Accident | From ₹100/month · Protect income when life takes a turn |
| Engine band | Buy Home cover | From ₹140/month · Keep your home and memories safe |
| Engine band | Add your policy | Your health and motor policy is pending |
| Second last | Download portfolio | Keep your policy in one safe place |
| Always last | Inactive policies | Found 2 inactive policies — Review |


**Diagram** — The bottom section has four slots in a fixed order. Insurance on Card is always at the top and is removed permanently once the user adds a card. The buy-and-add band sits in the middle and is the only part the engine writes. Download portfolio is second last, or last when there is no inactive policy, and stays inactive until the first policy is added. Inactive policies are always last, and the slot is hidden when there are none.

*Caption* — Four slots, one of which varies. Fixing the frame is what lets the contents be personal — the user learns the shape once, and after that only the middle band asks for attention.


**Note** — Every pitch card leads with a price, not a product. The decision a user is actually making is whether they can afford the gap, so the number goes first.


### See more — The sequence: “Why the order is fixed when the contents are not.”

**The failure mode I was designing against**

A personalised section where everything can move produces a different screen on every visit. Users stop scanning it and start ignoring it, which is how recommendation surfaces become banner space. The fix is not fewer recommendations — it is a frame that does not move.

**The four slots, and why each sits where it does**

Insurance on Card, always top. It is the only card offering cover the user already owns and has not claimed. That makes it the highest-value item on the surface and the one with a real end state — once a card is added it is gone, so it can afford the best position while it lasts.

Buy and add, in the middle. This is the engine band and the only part that varies. Putting the variable content between two fixed anchors means a returning user can find it without reading the whole section.

Download, second last. It is a utility, not a decision — useful once there is something to download, never urgent. It drops to last when there is no inactive policy below it.

Inactive policies, always last. It is the only item about something already wrong. Placing it below everything else means it never competes with a live policy or a relevant offer, but it is also never hidden from someone scrolling to the end.

**What the fixed order buys**

A user who returns in six months finds the same four positions. The learning cost is paid once. Personalisation then operates inside a structure the user already trusts, rather than asking them to re-read the screen each visit.

It also constrains the team. A new product cannot be added by inventing a new position — it has to earn a place inside the engine band, under the priority rules.

---

## 06 · Prioritisation

**Title** — The engine needed a product priority, not just personalisation.

**Lead** — Knowing what a user needs is only half the problem. I sorted every product by how much it matters in a person’s life, and the engine walks that ladder in order — it never skips a rung because the next product is easier to sell.


**Diagram** — A three-step ladder. Health and term life sit on the first step and both must exist before the engine moves up. Super Top-Up and Critical Illness are the second step. Personal Accident, Hospicash, Home and Device sit on the third, reached only when the user's context creates a reason.

*Caption* — A ladder, not a menu. A user holding health only is still on step one — the engine recommends term life, not something that extends cover they have not finished building.


**Note** — CoverRisk answers how much cover may be needed. The recommendation engine decides what should come next.


### See more — Prioritisation: “Who decided the order, and why it sits outside CoverRisk.”

**Separation of concerns**

CoverRisk provides the risk assessment, recommended coverage amount and estimated premium. It does not decide the product sequence.

**Who set it**

I defined the recommendation tiering with the product team, using our product and insurance-domain principles. Health and term life are the must-haves; until a user holds both, the engine recommends the missing one rather than anything that extends cover. Super Top-Up and Critical Illness come next. Personal Accident, Hospicash and the situational products appear only when the user’s context creates a reason.

This prevents the engine from ranking a product higher simply because it is easier to promote or cheaper to buy.

**Employer and endowment cover**

Both can exist in a user’s portfolio without providing the same role as personal foundational protection. The engine therefore treats the underlying protection state separately from the presence of any policy record.

**Why both halves are needed**

The recommendation engine needed both context and a stable product hierarchy. Context alone tells you what a person has; the hierarchy tells you what should come next.

**Who runs it once it ships**

Product owns where each policy sits in the ladder — that is insurance-domain expertise, and it belongs with the people who have it. When a new product launches, they place it.

What I built is the logic that reads the ladder: it never recommends at random, and it weighs the user’s data, how much a product matters in a life, and whether they already hold it. The placement is theirs to maintain; the decision procedure is generic and does not change when the catalogue does.

---

## 07 · Family

**Title** — Family completeness is a signal, not a display.

**Lead** — Family data used to be something Portfolio showed. I made it something the engine reads — whether a household exists, and whether its policies are stored, decides the primary action and controls whether Download is even available. Two inputs, four combinations, four different screens.


**Diagram** — A two by two matrix. Rows are whether a policy has been added; columns are whether a family member has been added. With no family member, Add Family Member is the primary action in both rows. With a family member added, it drops to a secondary card. Download is inactive in the no-policy row and active in the policy row. Inactive policies, when they exist, sit at the bottom of the section.

*Caption* — The left column is the one that matters: with no household on file the engine asks for one before anything else, because every later recommendation depends on knowing who is being covered. Adding a policy does not change that — it only unlocks Download.


**Flow** — Who is covered→Who is missing→Add their policy→Better context next time


**Note** — When a member exists but their policy does not, the prompt sits on that member’s own card rather than in the pitch band — the action belongs where the gap is visible.


### See more — Family: “Why family completeness matters to every later recommendation.”

**The dependency**

The engine can only make a useful household-level recommendation if it has a reliable view of the household.

**Two states, two prompts**

When sync identifies a family member without a policy, that member’s empty state becomes the prompt. When no family member is available, Add Family becomes the next useful action.

Once the family context is complete, those prompts disappear — because their conditions are no longer true.

**The design position**

The family section does not need a promotional banner. Its state already tells the user what is missing.

---

## 08 · Policy understanding

**Title** — KYP became part of the policy context.

**Lead** — Know Your Policy already assessed policy quality and conditions. I connected that existing intelligence to the place where users scan their policies — so the route into the feature becomes owning a policy, not finding a separate section.

- *Screen · kyp* — The scaleGREAT / GOOD / AVERAGE / POOR, with condition counts
- *Screen · life* — On the policyKnow Your Policy, a tab beside Details

**Note** — The rating is not a new recommendation. It is existing policy intelligence connected to the policy itself.


### See more — Policy understanding: “Why a verdict and counts are more useful than another score.”

**What was already there**

KYP already produced the underlying assessment. The Portfolio work was about making that assessment discoverable where the policy is already being managed.

**What the component shows**

A plain-language verdict, a four-segment meter, favourable and unfavourable condition counts, and a coming-soon state where a rating is not yet available.

A number invites comparison on price, which is the wrong axis. A verdict alone is a badge. The counts are what make the assessment inspectable.

**Ownership**

The rating is not a new recommendation. It is existing policy intelligence connected to the policy itself. The route into KYP becomes ownership of a policy, not discovery of a separate feature.

---

## 09 · Restraint

**Title** — Contextual does not mean everything, everywhere.

**Lead** — A recommendation engine easily becomes a targeted banner system. I made the layer secondary by default — Portfolio is for managing policies, and an offer never outranks that. It promotes to primary only when the screen has no primary task to offer: nothing stored yet, or policies the user told us about in onboarding but has not added.


**Diagram** — Three blocks. In the default state, policy content holds the primary zone of the screen and the recommendation sits below it as secondary. In the promoted state, where there is no policy to manage, the recommendation takes the primary zone. The third block lists what was kept out of Portfolio: Advisor Portfolio and Share Policy, each placed in the context where it is relevant instead.

*Caption* — The layer is secondary by default and promotes only when the screen has no primary task to offer. Two placements were kept out of Portfolio entirely and given a home where the context earns them.


**Note** — Good recommendation design is partly knowing what not to show.


### See more — Restraint: “The entry points the engine deliberately leaves out.”

**Advisor Portfolio**

Not given a permanent Portfolio banner, because the user already has a direct route from Homepage. It becomes relevant after CoverRisk, when the user has a specific protection question.

**Share Policy**

Not treated as a generic promotion. It appears where nominee context makes the action meaningful.

**Secondary by default, primary only when nothing competes**

The layer does not interrupt the primary job — it sits beneath it. It takes the primary slot only when Portfolio has no primary task to offer: nothing stored yet, or policies the user told us about during onboarding but has not added. In those states adding a policy or a family member is the useful thing, so the recommendation becomes the main action rather than competing with one.

**The broader rule**

If another part of the product already owns the entry point, Portfolio does not repeat it — unless the user’s current state creates a new reason to act.

Good recommendation design is partly knowing what not to show.

**The pressure this is already under**

Since launch, entry points have started arriving into the layer. The position I hold is that it stays a recommendation engine — its value is surfacing one relevant thing, and that value disappears the moment the layer becomes a place to put anything that needs a home.

So the open question is not what else could go in. It is what genuinely belongs, and what should come out before the user is choosing between options again.

**What I did not control**

The PRO subscription banner on this screen carries over from the previous design and sits outside this scope. It is already being repositioned.

---

## 10 · What changed

**Title** — What changed in the product.

**Lead** — The recommendation engine changed how existing capabilities connect to Portfolio. Quantitative impact should be added only once enough usage data is available.


**Note** — Recently launched. Quantitative results are not yet available — the measurement plan sets out what would prove, or disprove, each claim above.


### See more — What changed: “How I would measure whether the engine is actually working.”

**The trap**

The engine should not be judged only by recommendation clicks. A high click-through rate can recreate the same behaviour the system was designed to avoid.

**What to measure instead**

State transition rate. Completion of the recommended action. Coverage adequacy, or relevant protection progress. Policy-management task success. Recommendation relevance by state. Frequency of irrelevant or conflicting recommendations. Primary-task disruption.

**This is the first version, deliberately**

The engine shipped basic. Some policy states were not covered at launch and were added after — a policy has more states than the first rule set accounted for, and that only became clear once it was live.

The next round is precision rather than expansion: narrowing what belongs in the layer, tightening the content and language each recommendation uses, and making every one easier to act on. That work waits on user feedback and the first numbers — which is the right order, not a delay.

**The guardrail**

Recommendation engagement is not the goal by itself. The system should help users complete a useful next step without weakening Portfolio’s primary job.

The full measurement plan turns each claim in this case study into a hypothesis with a threshold that would disprove it.

---

## 11 · My role

**Title** — I built the system behind what appears, when and why.

**Lead** — The core contribution was not placing more CTAs. It was designing the contextual recommendation system that decides which capability should appear for which user state.

| I built | I connected | I worked with Product on |
|---|---|---|
| The recommendation engine · condition and rule-set design · recommendation priority and protection tiering · primary versus secondary action logic · Family Overview proposal and interaction · information hierarchy · progressive disclosure · interaction design · UX writing · the navigation fix | Existing CoverRisk intelligence into the Portfolio buying moment · KYP assessment onto the policy card · onboarding, policy, family and sync data into one readable state | Product and insurance-domain judgement · final recommendation priorities · the existing CoverRisk and KYP capabilities themselves |


### See more — My role: “What I owned, and what I did not.”

**I built**

The contextual recommendation model and engine. Condition and rule-set design. Recommendation priority and protection tiering. Primary versus secondary action logic. The Family Overview proposal and its interaction. Information hierarchy, progressive disclosure, interaction design and UX writing. The navigation fix.

**I connected**

Existing CoverRisk intelligence into the Portfolio buying moment. The KYP assessment onto the policy card. Onboarding, policy, family and sync data into one state the screen could read.

I did not create CoverRisk or KYP. Both existed; the work was making their intelligence reach the place where it changes a decision.

**I worked with Product and Design leadership on**

Product and insurance-domain judgement. Final recommendation priorities. The existing CoverRisk and KYP product capabilities themselves.

**The shape of the contribution**

The work was deciding who should see each capability, when, why, and what should happen next — not where to place a CTA.

---

## Close

**Line** — Portfolio became the connection layer for the rest of CoverSure.

**Sub** — The core Portfolio job stayed the same: manage the policies you already have. I did not rebuild Portfolio — I built the system that makes the rest of CoverSure more relevant inside it. From policy management to the next useful action.


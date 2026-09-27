# CoverSure Policy Portfolio — V9 copy

Contextual recommendation engine. Every word on the page, surface and *See more*.
Generated from the live markup, so this cannot drift from what is published.

**Live:** <https://dhanesh100.github.io/Case-study/#v9>

---

## Hero

**Headline** — Making Portfolio respond to the user — not just display their policies.

**Standfirst** — I built a contextual recommendation engine that uses information CoverSure already has about a user to surface the most relevant feature, product or next action inside Portfolio. The Portfolio’s core job stayed the same; the new layer made it connected to the rest of the product.

**Meta** — Product Designer·Post-MVP ·Policy Portfolio Shipped

### One-screen summary

**One Portfolio. Many user states. One contextual recommendation layer.**

- **01 — Existing product context** — Onboarding, policies, family data, CoverRisk, sync and KYP already contain useful signals.
- **02 — Recommendation engine** — Conditions and priority rules turn those signals into the next relevant action.
- **03 — Connected experience** — Portfolio becomes a gateway back into the right CoverSure feature or product — without changing its primary job.

The work was not adding more features to Portfolio. It was building the system that makes the features we already had work together.

**Honesty note** — Recently launched, so quantitative results are not yet available — §11 states what changed, not what it achieved. Coverage figures and priority bars in the screens are illustrative design placeholders, not customer data or measured values.

---

## 01 · The trigger

**Title** — A navigation issue exposed a bigger opportunity.

**Lead** — The work started with a blind-click navigation issue. I fixed that route — but it exposed something larger: Portfolio was a high-value surface where information from the rest of CoverSure could make product discovery more relevant.

- **Blind clicks** — Users tapping the wrong interaction to reach Policy Details.
- **Support** — The route sometimes had to be explained on the call.
- **B2B onboarding** — The same confusion observed directly, with real users.

### See the evidence — “Where the confusion actually was.”

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

**Lead** — CoverSure held information about policies, family, risk and user intent across different features. Portfolio was where users managed their policies — and that context was not being used there.

- **Existing data** — User and policy context already existed.
- **Existing capabilities** — CoverRisk, KYP, family management and the buying journeys already existed.
- **Missing layer** — No contextual system decided what should appear for this user, at this moment.

**Note** — The opportunity was not to build another feature. It was to build the layer that connects what already existed.

### See why Portfolio — “Why Portfolio became the connection point.”

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

**Lead** — The engine maps existing user context to the most relevant feature or product action. The recommendation engine is new; the intelligence it uses already existed.

**Flow** — User context→Conditions→Priority→Action→New context

| Context | Primary | Secondary | Reason |
|---|---|---|---|
| Onboardingholds policies | Add existing policies | — | Complete the record before recommending something already owned. |
| No policiesno CoverRisk | Start CoverRisk | Add a policy | Understand protection position before buying. |
| No policiesCoverRisk complete | Recommended Health / Life cover | — | Use the quantified CoverRisk output. |
| Policiesno CoverRisk | Review saved policies | CoverRisk | Management stays primary once something exists to manage. |
| CoverRisk completegap open | Recommended gap, amount and premium | KYP | Turn existing risk intelligence into an actionable decision. |
| Employer or endowment only | Foundational Health + Life | Add detected policies | Separate policy presence from foundational protection state. |
| Family member foundno policy | Add their policy | Add member | The missing policy is already visible in context. |
| Nothing relevant | Nothing is promoted | — | Portfolio stays focused on policy management. |

**Note** — Eight of ten rules shown. The last one is the constraint that keeps the engine from becoming a better-targeted banner stack.

### See the rule set — “How the recommendation engine decides what appears.”

**Every rule has three parts**

Condition — something the product already knows. Priority — what should win if several conditions are true. Action — the single most useful next step for that state.

**State is composed, not picked**

Users arrive with different combinations of policies, CoverRisk status, family data and onboarding answers. The Portfolio state is composed from whatever is true at that moment.

When multiple conditions fire, recommendation priority breaks the tie. The engine surfaces a primary action and, where useful, one secondary action.

**The two remaining rules**

Health only → Super Top-Up, to extend existing health protection. Life only → Critical Illness, which addresses a different protection gap rather than duplicating one.

**The constraint that matters most**

When nothing is relevant, nothing new is promoted. Portfolio stays focused on policy management.

Without this constraint, a contextual engine becomes a better-targeted banner stack. The recommendation layer only adds value if it protects the primary job of the screen.

The engine is not deciding what CoverSure can sell. It is deciding what is relevant to this user now.

---

## 04 · Experience

**Title** — Same Portfolio. Different next step.

**Lead** — The layout stays consistent. The recommendation state changes based on what the engine knows.

- **Screen — No policies** · CoverRisk leads — nothing to review yet
- **Screen — Employer cover only** · Foundational protection is still missing
- **Screen — Pending attention** · Renewals and inactive policies surface first
- **Screen — Policies added** · Review leads; recommendations move below

**Note** — Personalisation happens through state, not through a different screen for every user.

### See the states — “Why the same layout changes without becoming a different screen.”

**The engine changes the state, not the architecture**

The user still sees family context, their policies, policy details and relevant actions. What changes is which condition is true — and therefore which action is worth surfacing.

**Worked examples**

No policies → CoverRisk leads. Policies saved → review leads and recommendations move below. Inactive policy → review becomes relevant. Family member missing a policy → that member’s card becomes the prompt. CoverRisk complete with a gap open → the gap becomes actionable.

**The principle**

Personalisation happens through state, not through a different screen for every user. One layout, many conditions — which is also what makes it maintainable.

---

## 05 · Personalisation

**Title** — CoverRisk intelligence moved into the buying moment.

**Lead** — CoverRisk already calculated a recommended coverage amount and estimated premium. I connected that intelligence to the Portfolio buying moment — I did not add another assessment.

**Caption** — Figures shown are illustrative design placeholders, not customer data

### See the connection — “What the engine reuses from CoverRisk.”

**What CoverRisk already held**

Age, location, family, dependants, health, lifestyle, income, investments, property and expenses — everything needed to make the recommendation specific.

The recommendation layer did not ask the user for any of it again.

**The chain**

CoverRisk report → recommended coverage → estimated premium → relevant buying action.

**The product decision underneath**

The key decision was where the intelligence should continue. The report should not become the end of the journey when the next decision still depends on it.

I did not add another assessment. I carried existing intelligence into the next decision.

---

## 06 · Prioritisation

**Title** — The engine needed a product priority, not just personalisation.

**Lead** — Knowing what a user needs is only half the problem. When several products could be relevant, the engine also needs to know which protection category should come first. This is the CoverSure recommendation hierarchy — a product principle, not a universal claim about insurance.

**Note** — CoverRisk answers how much cover may be needed. The recommendation engine decides what should come next.

**Caption** — Relative priority in the recommendation order — not measured data

### See the ranking logic — “Who decided the order, and why it sits outside CoverRisk.”

**Separation of concerns**

CoverRisk provides the risk assessment, recommended coverage amount and estimated premium. It does not decide the product sequence.

**Who set it**

I defined the recommendation tiering with the product team, using our product and insurance-domain principles. Foundational protection comes before products that extend or supplement it; situational products appear only when the user’s context creates a reason.

This prevents the engine from ranking a product higher simply because it is easier to promote or cheaper to buy.

**Employer and endowment cover**

Both can exist in a user’s portfolio without providing the same role as personal foundational protection. The engine therefore treats the underlying protection state separately from the presence of any policy record.

**Why both halves are needed**

The recommendation engine needed both context and a stable product hierarchy. Context alone tells you what a person has; the hierarchy tells you what should come next.

---

## 07 · Family

**Title** — Family gaps became recommendation signals.

**Lead** — Family data is not just a display layer. It changes what the engine knows about the household — and household completeness affects every recommendation that follows.

**Flow** — Who is covered→Who is missing→Add their policy→Better context next time

- **Member found, no policy** → *Primary: Add their policy* — Secondary: Add member. The missing policy is already visible in context.
- **No member found** → *Primary: Add family member* — Household context is what later recommendations depend on.

### See the family states — “Why family completeness matters to every later recommendation.”

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

- **Screen — The scale** · GREAT / GOOD / AVERAGE / POOR, with condition counts
- **Screen — On the policy** · Know Your Policy, a tab beside Details

**Note** — The rating is not a new recommendation. It is existing policy intelligence connected to the policy itself.

### See the component logic — “Why a verdict and counts are more useful than another score.”

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

**Lead** — A recommendation engine can easily become a targeted banner system. The primary job of Portfolio remains policy management, so recommendations stay subordinate to it.

- **Advisor Portfolio** — Not a permanent Portfolio entry point. Homepage already provides the route; it appears after a CoverRisk report, when the user has a specific protection context to discuss.
- **Share Policy** — Not a generic Portfolio CTA. It appears in Life and Group policy context, where nominee information makes the action relevant.
- **Buy suggestions** — Below policy content, so users see their own cover before recommendations.

**Note** — Good recommendation design is partly knowing what not to show.

### See what was excluded — “The entry points the engine deliberately leaves out.”

**Advisor Portfolio**

Not given a permanent Portfolio banner, because the user already has a direct route from Homepage. It becomes relevant after CoverRisk, when the user has a specific protection question.

**Share Policy**

Not treated as a generic promotion. It appears where nominee context makes the action meaningful.

**The broader rule**

If another part of the product already owns the entry point, Portfolio does not repeat it — unless the user’s current state creates a new reason to act.

Good recommendation design is partly knowing what not to show.

**What I did not control**

The PRO subscription banner on this screen carries over from the previous design and sits outside this scope. It is already being repositioned.

---

## 10 · Components

**Title** — The engine only works if every state has a clear UI response.

**Lead** — Recommendation logic is only useful when its output can be understood at a glance. The quality of a recommendation system is often decided by the states that are not the happy path.

| State | How it resolves |
|---|---|
| Employer cover only | No yearly premium shown — the user does not pay it |
| Rating unavailable | Coming-soon band, so missing KYP data never looks like a poor rating |
| Member without policy | Prompt sits on that member's own card, so the action has context |
| Lapsed policy | Surfaced as something needing attention rather than hidden |
| Renewal due | Review report, or pay without review — the user makes an informed choice |

### See the edge cases — “Why these components were designed this way.”

**The states users never screenshot**

The engine has to handle states that will not appear in any showcase, but that users will encounter.

**Each one, and the rule behind it**

Employer cover only — do not show a yearly premium when the user does not pay it.

Rating unavailable — do not let missing KYP data look like a poor rating.

Family member without policy — keep the prompt on that member’s own card, so the action has context.

Lapsed policy — surface it as something that needs attention rather than hiding it.

Renewal due — offer Review Report or Pay Without Review, so the user makes an informed choice.

**Why this is the real work**

The quality of a recommendation system is often decided by the states that are not the happy path. Each one is a condition that had to resolve to something honest.

---

## 11 · What changed

**Title** — What changed in the product.

**Lead** — The recommendation engine changed how existing capabilities connect to Portfolio. Quantitative impact should be added only once enough usage data is available.

| &nbsp; | What changed |
|---|---|
| User experience | Contextual actions replaced competing promotional entry points |
| Product | Portfolio can now read relevant onboarding, policy, family and CoverRisk context |
| Business | Existing capabilities gained contextual entry points instead of relying on blanket promotion. More exploration of those capabilities is the intended effect, not a measured one. |

**Note** — Recently launched. Quantitative results are not yet available — the measurement plan sets out what would prove, or disprove, each claim above.

### See the measurement plan — “How I would measure whether the engine is actually working.”

**The trap**

The engine should not be judged only by recommendation clicks. A high click-through rate can recreate the same behaviour the system was designed to avoid.

**What to measure instead**

State transition rate. Completion of the recommended action. Coverage adequacy, or relevant protection progress. Policy-management task success. Recommendation relevance by state. Frequency of irrelevant or conflicting recommendations. Primary-task disruption.

**The guardrail**

Recommendation engagement is not the goal by itself. The system should help users complete a useful next step without weakening Portfolio’s primary job.

The full measurement plan turns each claim in this case study into a hypothesis with a threshold that would disprove it.

---

## 12 · My role

**Title** — I built the system behind what appears, when and why.

**Lead** — The core contribution was not placing more CTAs. It was designing the contextual recommendation system that decides which capability should appear for which user state.

| I built | I connected | I worked with Product on |
|---|---|---|
| The recommendation engine · condition and rule-set design · recommendation priority and protection tiering · primary versus secondary action logic · Family Overview proposal and interaction · information hierarchy · progressive disclosure · interaction design · UX writing · the navigation fix | Existing CoverRisk intelligence into the Portfolio buying moment · KYP assessment onto the policy card · onboarding, policy, family and sync data into one readable state | Product and insurance-domain judgement · final recommendation priorities · the existing CoverRisk and KYP capabilities themselves |

### See what I owned — “What I owned, and what I did not.”

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

Portfolio became the connection layer for the rest of CoverSure.

The core Portfolio job stayed the same: manage the policies you already have. I did not rebuild Portfolio — I built the system that makes the rest of CoverSure more relevant inside it. From policy management to the next useful action.

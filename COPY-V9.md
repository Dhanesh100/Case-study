# Policy Portfolio — case study copy (V9)

Every word on the page, surface and *See more*. Generated from the live markup, so this
cannot drift from what is published.

**Live:** <https://dhanesh100.github.io/Case-study/#v9>

---

## Masthead

**Headline** — I built a contextual recommendation engine inside the screen people actually visit.

**Standfirst** — Portfolio receives almost every visit an insurance app gets. The rest of the product — CoverRisk, Know Your Policy, family management, seven products — was invisible from it. The engine connects them, using data we already had.

**Positioning line** — I turn “where do we put this feature?” into “when does it become useful?” — and build the rule set that answers it. Not an insurance problem. It is any screen where the business wants promotion and the user wants to finish a task.

**Honesty note** — Recently launched, so there is no usage data yet — §08 states what changed, not what it achieved. Figures in the screens are illustrative placeholders from the design files.

---

## 01 · What I built

**Title** — A recommendation engine, built from scratch, inside an existing screen.

**Lead** — It reads what the product already knows about a person and surfaces the one capability that applies to them. No features were built for it and no new data was collected — the intelligence existed, scattered across the app.

**Note** — What was left alone: the architecture. Family overview → policy listing → policy details is the same as it always was, and so is the job — store your cover, see the household, open any one of it.

### See more — “What was built from scratch, and what was only fixed”

**Built from scratch**

The contextual recommendation engine. Its signals, its conditions, its priority order, and the rule that decides what takes the primary slot.

That is the substance of this project. Ten conditions, evaluated against data the product already held, resolving to one primary action and at most one secondary.

**Left alone**

The architecture. Family overview → policy listing → policy details, and the job of storing cover and checking it. That structure worked; changing it was never the point.

**Rebuilt, but not redesigned**

The section was rebuilt against a new design system, so the surface changed while the structure did not.

One navigation defect was fixed along the way: the entry point into a policy and the expand-and-collapse beside it were styled identically, so taps landed repeatedly on the control that only revealed detail in place. Member chips gave profile-switching its own affordance. That was a fix, not the work — it is here because it is the only part of the project with evidence from before the change.

**Not built**

No features were created for this. CoverRisk, Know Your Policy, family management and the products themselves all existed. The engine is a reading of them.

---

## 02 · Why this screen

**Title** — Portfolio gets almost every visit. The rest of the product was invisible from it.

**Lead** — People open an insurance app a handful of times a year — a renewal, a document, a claim. Nearly all of those visits land here, and each one is a single chance. Meanwhile three other parts of the product held everything needed to make that visit useful, and none of it reached this screen.

**Rejected** — Rejected A capability needs adoption → give it a banner on the busiest screen

### See more — “Why a banner was the wrong instrument, not the wrong idea”

**The disagreement was never about whether to promote**

The goal was more exploration of the connected features, not less. The only question was method: show everything to everyone, or map what we already know about each person and surface the one thing that applies.

**Why blanket promotion is the expensive option**

A banner is a fixed bet. It spends every one of a user's few annual visits on the same pitch, whether or not it fits.

We carry more products than any one person needs, and most of them do not relate to any given user. So the wrong pitch loses twice: it wastes a scarce visit, and it costs the screen its own job at the same time.

**What made this screen worth it**

For active users Portfolio is one of the highest-footfall sections in the app. Combined with how rarely an insurance app is opened at all, that makes it the one place where a recommendation reliably reaches someone.

It is the best place in the product to surface anything else — and therefore the worst place to waste.

---

## 03 · What it reads

**Title** — Five signals the product had already collected.

**Lead** — None of them new. Each one stopped at the boundary of the feature that gathered it.

**Note** — Every section of the app knew something and shared none of it. Connected, they read the same user state — which is what makes the app behave like one product rather than a set of separate tools.

| Signal | What it knows | Where it used to stop |
|---|---|---|
| Onboarding | Whether they hold cover, and which types | Signup |
| CoverRisk | Recommended amount, estimated premium, risk band | Its own report |
| Policy data | What they actually hold — and what is missing | A list, with no reading of it |
| Family data | Who is covered, who is not, what sync found | A separate section |
| Know Your Policy | How good each policy they own actually is | Its own tab |

### See more — “What each signal makes possible that was not possible before”

**Onboarding**

Someone who told us at signup that they hold health cover should be asked to add that policy — not to buy what they already own.

Without this signal, the screen greets an existing customer as a stranger.

**CoverRisk**

It already collected age, dependants, income, expenses, health, lifestyle, assets and liabilities, and produced a recommended cover amount, an estimated premium and a risk band. All of it stayed inside its own report.

Moving the number to where the decision happens is the difference between Buy Life Insurance and you may need ₹80,00,000 more cover, at roughly ₹11,800 a year.

**Policy data**

Not just a list — a reading of it. Health but no life is a foundational gap. Employer cover only is no personal cover at all. An endowment is a savings product, not protection.

**Family data**

One person usually manages insurance for a household. Sync sometimes finds a member before the user mentions them, and an empty card for that member is a more honest prompt than any banner.

**Know Your Policy**

Quality, not just quantity. A policy with a room-rent cap is worth less than its sum insured suggests, and the engine can weigh what someone holds rather than only counting it.

---

## 04 · How it decides

**Title** — Ten conditions. One primary action, at most one secondary.

**Lead** — The screen decides what fits, not what to promote. We carry more products than any one person needs — and a visit spent pitching something they already own is a visit spent proving we were not listening.

**Note** — Seven of ten scenarios. The last row is the one that proves the rule.

| What we already know | Primary action | Secondary |
|---|---|---|
| Onboardingno policies · no CoverRisk | Take CoverRisk | Add a policy |
| Onboardingthey said they hold policies | Add your policies | — |
| Portfoliohas policies · no CoverRisk | Review saved policies | CoverRisk, as secondary |
| CoverRiskreport done · a gap is open | The gap, as an amount and a premium | KYP on each card |
| Policy dataemployer or endowment cover only | Health and term life first | Add the policies we found |
| Family syncfound a member with nothing added | Add their policy, on their own card | Add member |
| Nothing outstandingcovered · report done · family complete | The portfolio, and nothing else | — |

### See more — “The full rule set, and what happens when several conditions fire at once”

**How a rule gets written**

Each rule names a condition the product could already evaluate, the action that follows, and the reason. No rule is allowed without the third part.

**The three remaining scenarios**

No policies, CoverRisk done → buy health, then term life, with the amount and premium attached. The report already names it; showing it here removes the reason people abandon the journey.

Holds health only → the foundation is still incomplete, so term life comes before anything that extends health.

No member added, none found → add a family member, as a primary card after the user's own overview. Family completeness improves every recommendation that follows.

**When several are true at once**

Two rules break the tie. Protection priority — a foundational gap outranks everything below it. Review outranks offers — once a policy exists, reviewing it is the screen's job and the offer drops to secondary.

At most one primary and one secondary ever show. There is no third slot to fill.

**When none are true**

Nothing shows. Showing something anyway would undo the whole rule.

---

## 05 · What comes first

**Title** — Health and term life come first. Always.

**Lead** — For a working person those are the two that matter; everything else extends or supplements them. CoverRisk supplies the amount — it does not decide the order. That is a separate design decision, and it holds whatever the report returns.

**Rejected** — Never No foundational cover → pitch home insurance

**Caption** — Relative priority in the recommendation order — not measured data

### See more — “Who set this order, and why employer cover does not count toward it”

**The principle underneath it**

Protection before accumulation, and breadth before depth. Health and term life cover the two events that would actually break a household's finances.

**Who decided**

I set the order, working through it with the product team for domain judgement. It is deliberately held separate from CoverRisk: CoverRisk supplies the amount, the order decides the sequence. Keeping them apart means the sequence holds whatever the report returns.

**Employer and endowment cover, specifically**

Group health from an employer ends when the job does, and the user does not pay the premium — which is why Premium Yearly reads an em dash on that state rather than a number. An endowment is a savings product wearing an insurance label.

Neither counts toward the foundation, so for a user holding only those, the order restarts at the bottom.

**The rule I would not break**

No foundational cover, no pitch for anything situational. Selling home or device cover to someone with no health or life protection is an easier sale and the wrong outcome.

---

## 06 · When it says nothing

**Title** — When nothing fits, the screen shows nothing.

**Lead** — Portfolio exists to review saved cover. Everything else is an offer, and offers wait — which is what stops an exploration layer eating the screen it lives on.

**Note** — Not showing an irrelevant pitch is how the screen tells the user it understood them. That is the part a banner can never do, however well targeted.

- **Nothing saved yet** → *The engine leads* — There is no cover to review, so understanding the risk is the most useful thing the screen can do.
- **Policies already saved** → *Review leads, offers sit below* — The user came to check what they hold. The offer stays available and stops competing.

### See more — “The failure mode this prevents, and the hierarchy rule behind it”

**What happens without a governing constraint**

An exploration layer with nothing holding it back becomes a banner stack with better targeting. Every rule that fires is individually justified, and collectively they bury the thing the user came for.

**The constraint above every rule**

Portfolio exists to review saved cover. A capability can take the primary slot only when there is nothing to review. The moment a policy exists, review leads and the offer drops beneath it.

**The hierarchy that goes with it**

Offers sit below the policies, never above them. A user who scrolls past their own cover to reach a suggestion has already had their question answered — which is the only honest moment to make one.

**Why silence is the point**

When a user has everything relevant, the screen shows the portfolio and nothing else. That is not a gap in the design.

Not showing an irrelevant pitch is how the screen tells the user it understood them — and it is the one thing a banner can never do, however well it is targeted.

---

## 07 · What it connected

**Title** — Seven capabilities now reach the user through one screen.

**Lead** — Same layout, same feature set. What differs is which conditions are true — and two capabilities were deliberately given no Portfolio entry point at all.

**Note** — The last two rows are the restraint. Declining to place a feature is harder to argue for than placing one.

| Capability | Reaches the user when |
|---|---|
| Add Policy | Always — it is the screen's own job |
| Family Management | A member or their policy is missing |
| CoverRisk | No risk report exists yet |
| Buy Policy | A report exists and a protection gap is open |
| Know Your Policy | Always — on every policy owned |
| Share Policy | Life or Group, where a nominee relationship already exists |
| Advisor Portfolio | After the CoverRisk report — no Portfolio entry point of its own |

- **Screen — Nothing yet** · Understand the risk before asking them to buy
- **Screen — Employer cover only** · Premium reads “—” because they do not pay it
- **Screen — Needs attention** · Renewals and lapses, named per member
- **Screen — Established** · Review leads; suggestions sit below with their reasons

### See more — “The two entry points I declined, and what they competed with”

**Advisor Portfolio**

It needed adoption like everything else, and the obvious move was a banner here. I pushed back.

The Homepage already carries a direct route, so repeating it on Portfolio would add noise without adding access. Instead the advisor appears immediately after a CoverRisk report is generated — the one moment a user has just read something about their own risk and has questions they cannot answer alone.

It is a different job from general support: the PRO tier's relationship manager handles claims and legal questions, while Advisor Portfolio is guidance on cover. Stacking both here would have blurred them.

**Share Policy**

Life and Group policies already carry a nominee relationship, so sharing sits alongside that rather than becoming another Portfolio CTA. The reason comes before the action — sharing matters because a nominee may need access at the worst possible moment.

**What I did not control**

The PRO subscription banner on this screen carries over from the previous design and sits outside this scope. It is already being repositioned. The conditions described here govern the entry points I owned, not every pixel on the screen.

---

## 08 · What changed, and what was mine

**Title** — The engine was mine. The problem set was the product head's.

**Lead** — Recently launched, so this is what changed — not what it achieved.

**Note** — The measurement plan sets out what would disprove each claim on this page, and what gets measured once data matures.

| Decision | Originated by |
|---|---|
| The recommendation engine and its rule set | Me |
| Recommendation order and protection tiering | Me, with the product team for domain judgement |
| Connecting CoverRisk's numbers into Portfolio | Me |
| The rule that offers sit below the policies | Me |
| Declining the Advisor entry point | Me |
| Family Overview as a prompt rather than a CTA | Me |
| Navigation fix, and the design-system rebuild | Me |
| The problem set that started the work | Product head |
| CoverRisk entry point, and KYP on the policy card | Product and Team leadership |

### See more — “What changed in the product, and how this gets tested”

**What changed**

Recently launched, so these are the changes — not the results.

For the user. Contextual actions replaced competing promotional entry points, and the screen stays quiet when it has nothing useful to say.

For the product. Portfolio reads onboarding, CoverRisk, policy data, family state and KYP. Every section now reads the same user state, so the app behaves like one product.

For the business. More exploration of the connected features, by narrowing rather than widening — each arrives for the people it fits.

**How it gets tested**

The measurement plan converts each claim above into a hypothesis with a threshold that would disprove it. State transition rate is the headline — the share of users who move to a better portfolio state within thirty days, because the design's own definition of progress is that a condition stops being true.

Cover adequacy ratio — cover purchased over cover recommended — is the business metric, because conversion alone cannot tell more people buying adequate cover from more people buying cheap cover faster.

**The metric that would mislead**

Recommendation click-through. Optimising it means making the pitch louder and higher, which is the banner strategy this replaced. Low click-through on a deliberately subordinate element is the expected result, not a defect.

---

## Close

The work was deciding who should see each capability, when, why, and what happens next — not where to put the button.

Portfolio became an advocate for the rest of the product rather than a store of policies — and the screen stays quiet when it has nothing useful to say.

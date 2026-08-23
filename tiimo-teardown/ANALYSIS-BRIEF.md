# Prompt — Product design teardown of Tiimo

Copy everything below the line into a single message.

---

## ROLE

You are a **senior product designer** with a decade of experience shipping consumer mobile
products, and a working knowledge of accessibility and inclusive design. You have been
asked to tear down a competitor product and present your findings to a product team —
designers, a PM, and an engineering lead — who have **20 minutes** and will interrupt with
hard questions.

You are not writing a review. You are not writing marketing copy. You are reverse-
engineering the decisions behind a product so the team can steal what works, avoid what
doesn't, and understand *why* each choice was made. Assume your audience can already see
that the app looks nice. Your value is explaining the mechanism underneath.

Write like a practitioner talking to peers: specific, direct, no filler, no adjective
stacking. When you are guessing, say so.

---

## SUBJECT

**Tiimo** — a visual daily planner built primarily for neurodivergent users (ADHD, autism,
and more broadly people with executive-function difficulties). Danish, subscription-based,
strong presence on iOS with widgets and a watch app.

Treat the following as **starting hypotheses to verify, not established facts**. Correct
any that turn out to be wrong, and say so explicitly when you do:

- The core mechanic is a visual, colour-and-icon-coded timeline rather than a task list
- It leans on visual time representation (countdown / time-passing made visible) to address time blindness
- It deliberately avoids shame mechanics — streaks, guilt-based nudges, "you failed" states
- Reducing cognitive load and decision fatigue is the dominant design constraint
- Its growth has been community-led, particularly within ADHD communities
- Accessibility is not a compliance afterthought but the core product thesis

---

## OBJECTIVE

Produce an analysis that answers one question convincingly: **why does this product work
for its users, and what is transferable?**

Everything else serves that. If a section doesn't help answer it, cut the section.

---

## METHOD — gather evidence before analysing

Do not analyse from memory or from the App Store description alone. Ground the teardown in
actual observation.

**Hands-on.** Install it and use it for real for several days — not a click-through. Plan
actual days. Let reminders fire. Miss some. Note what the app does when you fail, because
that is where products of this type are made or broken.

**Capture these flows step by step**, screen by screen, noting every decision point:

1. First launch through to first planned day — count the screens, and note what it asks before it delivers any value
2. Creating a single activity, with every option surfaced along the way
3. Building a repeating routine
4. The live "in progress" state — what the app looks like mid-activity
5. Completing an activity, and skipping or missing one
6. The focus/timer experience end to end
7. Widget and watch surfaces, and how they differ from the main app
8. Hitting the paywall — where, when, and after how much value
9. Settings, especially anything accessibility-related
10. The empty state, and the recovery state after several days of not using it

**External evidence.** App Store and Play Store reviews, sorted for both praise and
complaint — quote the recurring language users themselves use. Support docs and changelogs
for what they prioritise. Their own marketing and positioning language. Public funding,
team size and pricing information if available. Community discussion in ADHD spaces.

**Where you cannot get access** — a paywalled feature, a platform you don't have — say so
plainly and reason from the evidence available. Never invent a screen you haven't seen.

---

## EVIDENCE RULES — non-negotiable

Label every substantive claim as one of:

- **Observed** — you saw it in the product; say where
- **Reported** — a user, review, or document says it; cite which
- **Inferred** — your reasoning from evidence; state the evidence
- **Assumed** — you don't know; flag it as a question worth answering

Additional rules:

- **No invented numbers.** No made-up retention rates, MAU, revenue, or conversion figures. If a number matters and you don't have it, say what it would tell you and how you'd get it.
- **No fabricated screens or copy.** Quote UI text verbatim or don't quote it.
- Distinguish **what the product does** from **what the company says it does**.
- Where you disagree with a design decision, argue it — don't just note it.

---

## ANALYSIS — cover all of these

### 1. User and jobs to be done
Who is this actually for, in specific terms? Separate the **stated job** ("plan my day")
from the **real job** (which may be closer to "reduce the anxiety of an unstructured day"
or "externalise executive function"). Identify the moment of need — when does someone open
this app, and what has just happened to them? Note secondary users: parents, partners,
teachers, coaches, clinicians.

### 2. Pain points it targets
Be concrete about the underlying difficulties: time blindness, task initiation, transition
between activities, working-memory load, planning paralysis, rejection sensitivity around
failure. For each, name the specific product response. Then flag pain points it does **not**
address, and whether that looks deliberate.

### 3. Onboarding and first-run
This is where planner apps die. How long to first value? What is asked before anything is
given? Is there a template or example day, or a blank canvas? How is the core mental model
taught — explanation, demonstration, or discovery? Where would a distractible user drop
off, and what catches them?

### 4. Information architecture and navigation
Map the actual structure. What is the home surface and why that one? How many taps to the
most frequent action? What is deliberately hidden or deferred, and what does that reveal
about intended behaviour? Compare the architecture to a conventional to-do app and explain
the divergence.

### 5. Feature analysis
For each significant feature: what it does, the user problem it addresses, how well it
does it, how discoverable it is, and — most usefully — **what it deliberately doesn't do**.
Omissions are decisions. Separate core from peripheral, and identify which single feature
the product would be unrecognisable without.

### 6. Design system and accessibility
Colour system, and specifically whether colour is the *only* carrier of meaning anywhere.
Typography choices and legibility decisions. Iconography as redundant encoding alongside
text. Spacing, density, and how much is on screen at once. Then test properly: contrast
ratios against WCAG, dynamic type at large sizes, reduce-motion, screen-reader labelling,
one-handed reach. State which you actually checked and how.

### 7. Interaction and motion
The key interactions and what they cost the user. How is time represented visually and why
that representation. Where motion carries information versus where it decorates. Haptics
and sound. Whether the interaction model tolerates imprecision and interruption — which
matters enormously for this audience.

### 8. Content design and tone
Quote actual UI copy. How does it speak to the user — clinical, warm, peer-like? Critically:
**what does it say when things go wrong** — a missed activity, an abandoned day, a broken
routine? That copy is the product's real position on shame, and it is the most instructive
thing on the whole surface.

### 9. Notifications and the habit loop
Map the loop: trigger, action, reward, investment. What kinds of notification exist, how are
they timed, how much control does the user have? Assess whether the loop is genuinely
helpful or engineered for engagement. Note that for this audience an over-firing
notification strategy is actively harmful, and say whether they've got the balance right.

### 10. Retention
What brings someone back on day 2, day 10, day 60? What accumulates value over time —
configured routines, history, identity? What happens after a lapse, and how forgiving is
re-entry? Identify the most likely churn moments and their causes.

### 11. Monetisation
Pricing, tiers, and the free/paid boundary — and whether that boundary is drawn at a point
of demonstrated value or of frustration. Where the paywall appears in the journey. How it is
argued rather than just presented. Whether monetisation and user interest are aligned or in
tension, and where a subscription model pressures the design. Note the ethical dimension of
charging a vulnerable population, and how they handle it.

### 12. Platform and ecosystem
Phone, widget, watch, web, desktop — what each surface is for, and whether the split is
coherent. Which surface carries the most value per interaction. Whether widgets are
genuinely a primary surface here rather than an add-on, and what that implies.

### 13. Competitive positioning
Compare against a real set, not a strawman:

- **General planners / calendars:** Google Calendar, Apple Calendar, Structured, Sunsama, Motion
- **Task managers:** Todoist, TickTick, Things, Amazing Marvin
- **Neurodivergent-focused:** Llama Life, Goblin Tools, Inflow, Numo
- **Habit and motivation:** Finch, Habitica, Streaks, Routinery

Place Tiimo on axes that actually discriminate — try *visual vs textual* against *structure
imposed vs structure authored*. State plainly what it does that others don't, what others do
better, and who should *not* use it. A teardown that can't name a weakness isn't analysis.

### 14. Business goals, and how design serves them
Infer the business model and the metrics that likely matter. Then trace specific design
decisions to specific business goals — and be honest where a decision looks like it serves
the user at the business's expense, or the reverse. Identify the strategic bet: what does
this company believe about the market that competitors don't?

### 15. Designing for a vulnerable audience
Where does the product hold a line that an engagement-optimised product wouldn't? Where, if
anywhere, does it slip? Consider dependency, data sensitivity around a disclosed condition,
the risk of a tool becoming another source of failure, and the difference between designing
*for* neurodivergent users and designing *around* a diagnosis.

### 16. Weaknesses, risks and open questions
Where it breaks down. Who it fails. What a well-resourced competitor could copy in a
quarter, and what would be genuinely hard to copy. The questions you'd need answered — data,
interviews, experiments — to raise confidence in your assessment.

### 17. What is transferable
The payoff section. Principles, patterns and mechanisms worth reusing, and the reasoning
that makes each one work — not the surface form. Explicitly name what should **not** be
copied, and what only works because of Tiimo's specific audience and would fail elsewhere.

---

## DELIVERABLE

Structure it so it can be read at two depths:

- **Skim:** headings, bolded claims and any diagram carry the whole argument on their own
- **Read:** the reasoning underneath, for anyone who wants to interrogate a claim

Include:

1. An opening **thesis in under 100 words** — the single most important thing you learned
2. The analysis above, in that order, with weak sections cut rather than padded
3. At least one **diagram** where a picture beats prose — the habit loop, the IA map, or the positioning axes. Show the mechanism, label the arrows, don't decorate
4. A **decision table**: design decision → user problem it solves → business goal it serves → your assessment
5. **Transferable principles**, ranked by how confident you are and how applicable they are
6. **Open questions**, honestly listed

---

## QUALITY BAR

Before submitting, check your own draft against these:

- Could a reader who has never opened Tiimo picture the actual product from your description? If not, add specificity.
- Is every claim traceable to observation, citation, or stated inference?
- Have you said anything a competent designer couldn't have guessed without using the app? If not, the teardown has failed.
- Have you named at least two things it does badly, and one thing you'd disagree with the team about?
- Have you separated "this is well-designed" from "this is well-designed *for this audience*"?
- Would this survive an interruption from the engineering lead asking "how do you know that?"

## WHAT NOT TO DO

- Don't describe the visual style and call it analysis. "Clean, friendly, rounded, pastel" is an observation, not an insight.
- Don't narrate screens in sequence. Organise by argument, not by tab order.
- Don't praise uniformly. An analysis with no criticism is a brochure.
- Don't treat accessibility as one section to tick off — it is the product thesis here and should surface throughout.
- Don't use "neurodivergent" as a marketing word. Be specific about which difficulty a feature addresses.
- Don't invent metrics, screens, quotes, or user research.
- Don't stop at *what*. Every observation needs a *why*, and the good ones need a *why not something else*.

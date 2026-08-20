# CoverSure Policy Portfolio — Product Design Case Study

**Making Portfolio respond to the user — not just display their policies.**

Product Designer · Post-MVP · UX Strategy · Personalisation · Progressive Disclosure

**Live:** <https://dhanesh100.github.io/Case-study/>

---

## The work

Five capabilities needed to be discovered on the screen where people manage their
policies: Add Policy, CoverRisk, Buy Policy, Family Management and KYP. Promotional
banners were the obvious answer, and they competed with the screen's primary job.

So the question changed from *"how do we promote these features?"* to
*"when does each feature become useful to this user?"* — which turns promotional
slots into conditions that can be evaluated against a person's actual portfolio.

## Two versions

The case study is published in two tellings of the same argument, switchable by tabs
at the top of the page:

| Version | Reading time | Approach |
|---|---|---|
| **Compact** | ~60 seconds | Visual-led. Five skill points, each carried by a diagram. |
| **Full study** | ~5 minutes | Narrative. Eight screens, six proofs, the full reasoning. |

Both versions are deep-linkable:

- `index.html#compact`
- `index.html#full`

## Project log

[`PROJECT-LOG.md`](PROJECT-LOG.md) is the working record behind this case study:

- **Feedback and direction received** — every instruction given, and what each one changed
- **Fact-finding** — the six questions asked to keep the content factual, and the answers
- **Decision record** — decisions taken and why, including the ones later reversed
- **Corrections made** — what was wrong in a draft and how it was fixed
- **What is illustrative, not real** — stated plainly, so no figure is mistaken for product data
- **Open items** and the deployment record

## Viewing it

Open `index.html` in any browser. It is a single self-contained file — no build step,
no dependencies, no external requests.

## Built with

Hand-authored HTML and CSS. All UI screens are HTML/CSS reconstructions of the shipped
interface; all diagrams are inline SVG. No frameworks, no images, no external assets.

- Adapts to light and dark system themes
- Responsive down to 390px
- Keyboard-operable tabs, `prefers-reduced-motion` respected

## A note on the data

Policy names, KYP ratings, cover amounts and premium figures shown in the screens are
**illustrative sample data**, not real customer or product values. They stand in for the
real figures so the interface reads as it does in use.

---

© Dhanesh Shetye. Case study content and design.

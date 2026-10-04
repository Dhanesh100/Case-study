# Working in this repo

**Dhanesh Shetye — CoverSure Policy Portfolio case study and companion documents.**

This file is loaded automatically at the start of every session in this directory.
Follow it without being asked.

---

## At the start of every session — pull, then read

```bash
git pull --ff-only origin main
```

Then **read [`CONTEXT.md`](CONTEXT.md) before doing anything else.** It is the standing
brief: the product facts, the framing rules, what may not be claimed, the Figma node ids,
and what is still open. It exists so Dhanesh does not have to re-explain the project each
time. Do not ask him for details that are already in it.

`./sync.sh` does the pull and prints the brief plus what is open.

## After every change — push, without being asked

> *"push every update without any prompt, every prompt result push to github"*

Commit and push every change to `https://github.com/Dhanesh100/Case-study`. Do not wait for
permission and do not batch changes up. The one carve-out: flag before publishing anything
sensitive.

Then **verify against the live URL**, not the GitHub Pages API — the API reports `built`
from the *previous* deployment. Poll `https://dhanesh100.github.io/Case-study/` and grep for
the new content.

## Keep CONTEXT.md fed

When Dhanesh states a durable fact, corrects a framing, or settles an open question,
**write it into `CONTEXT.md` in the same turn** — not only into the reply. That is the
entire point of the file. If it only lives in the conversation, he will have to say it
again.

`PROJECT-LOG.md` is the chronological record of what happened. `CONTEXT.md` is the brief.
Keep the two distinct.

---

## Regenerate derived files

| After changing | Run |
|---|---|
| The scan panel | `python3 build-scan.py` |
| The V10 panel | `python3 build-copy.py v10` |

## Before any publish

Tag balance · duplicate ids · SVG markers resolving **inside their own panel** · no colour
literals outside the token blocks · every tab wired to a panel · every `data-open`
resolving · no undefined CSS classes · **the scan test**.

> **The scan test.** Hide all the body copy. Read only: Title → Section headings → Bold
> text → Numbers → Diagrams → UI annotations. If the story still makes sense, it passes.
> A section that disappears under this test is not finished.

## House rules

- **No decorative copy.** Every sentence carries a fact, a decision or a reason.
- **No claim without evidence.** Nothing shipped has usage data yet; say so rather than
  implying an outcome.
- **The engine is the subject**, not the dead-click fix that triggered it.
- Single self-contained HTML files. No build step, no dependencies, no external requests.

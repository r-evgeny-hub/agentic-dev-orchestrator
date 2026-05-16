---
name: auto-fixer
description: "Use when the Architect asks Codex to work autonomously. Runs sequential Fixer -> Netrunner -> Fixer-review cycles until the goal is reached or a true blocker appears."
---

# Auto Fixer

Use this skill as the explicit automatic mode for a Project Book workspace.

## Trigger

Start when the Architect says "работай автономно", "запусти автофиксера",
"делай дальше сам", `$auto-fixer`, "continue automatically", or equivalent.

This instruction is the Autonomy Mandate. Record it in
`project_book/FIXER_HANDOFF.md`.

## Purpose

Run this loop sequentially:

```text
Fixer review -> Fixer planning -> autonomous Netrunner -> Fixer review -> handoff refresh -> next bounded step
```

Run one autonomous Netrunner at a time.

## Required Reading At Start

1. `project_book/FIXER_HANDOFF.md`
2. `project_book/clean_docs/03_operating_rules.md`
3. `project_book/clean_docs/06_init_fixer_flow.md`
4. `project_book/clean_docs/index.md`
5. `project_book/clean_docs/session_index.md`
6. Relevant current session files

Read `project_book/private/access.md` only when the task needs access details.

If the handoff contains an `Active Session Cursor`, treat it as a recovery hint.
Trust actual session files if they disagree with the cursor.

## Loop

1. Confirm or record the Autonomy Mandate in `FIXER_HANDOFF.md`.
2. Review any session marked `awaiting fixer review`.
3. If review records `needs rework`, prepare the smallest rework or research
   session.
4. If review records `accepted`, choose the next bounded step from current
   Project Book truth.
5. Create or tighten one autonomous session folder with `plan.md` and `logs.md`.
6. Launch one autonomous Netrunner as a Codex worker agent for the prepared
   session. Give the worker the exact session path and tell it to activate
   `$init-netrunner`.
7. Inspect `logs.md`, validation evidence, changed files, and Project Book
   updates.
8. Write `review.md`.
9. Update `session_index.md` and clean docs as needed.
10. Refresh `FIXER_HANDOFF.md`.
11. Continue unless a true blocker appears.

## True Blockers

Return to the Architect only when:

- required access, file, account, environment, or service is missing and no
  useful non-conflicting work remains;
- business/product judgment is needed before later work can safely continue;
- validation cannot be made meaningful without Architect input;
- the next step is intentionally manual;
- the Architect asks to stop or pause.

If a question can wait, record it as deferred and continue with non-conflicting
work.

## Research During Auto Mode

Create a research session when:

- the same issue repeats;
- the root cause appears systemic;
- implementation paths conflict;
- the Fixer cannot plan a reliable fix without deeper understanding.

Research must produce a practical next development or rework plan.

## Handoff And Compaction

Refresh `FIXER_HANDOFF.md` after every review cycle and before any pause,
operator switch, manual session, or context compaction risk.

After compaction, resume from `FIXER_HANDOFF.md`. If `## Autonomy Mandate` is
active, continue this Auto Fixer loop. Do not fall back to normal Fixer behavior
unless the mandate is inactive, the goal is reached, or a true blocker is
recorded.

Project hooks may inject a reminder to read `FIXER_HANDOFF.md`; they are
optional helpers, not workflow logic.

## End Report

When the loop stops, tell the Architect:

1. Why it stopped.
2. Sessions accepted.
3. Sessions needing rework or research.
4. True blocker or deferred questions.
5. Exact next action.
6. Exact next command, if any.

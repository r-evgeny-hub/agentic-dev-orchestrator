# Project Book

Project Book is the operating memory for an AI-assisted project.

It keeps current truth, bounded work sessions, evidence, Fixer reviews, access
details, and handoff state in one readable folder so future agents can continue
without rediscovering the project.

## Core Flow

```text
Architect describes project
  -> Fixer asks missing questions
  -> Fixer records current truth
  -> Fixer plans one bounded Netrunner session
  -> Netrunner executes and logs evidence
  -> Fixer reviews
  -> accepted / needs rework / blocked
  -> handoff refresh
  -> next session or autonomous continuation
```

## Roles

- **Architect:** owns business intent, product judgment, priorities, and final
  decision.
- **Fixer:** owns planning, context control, project memory, review, and handoff.
- **Netrunner:** executes one bounded `plan.md`.
- **Auto Fixer:** repeats the cycle sequentially after the Architect gives an
  Autonomy Mandate.

## Key Files

- `AGENTS.md`: role and operating rules.
- `FIXER_HANDOFF.md`: current resume point and Autonomy Mandate state.
- `private/access.md`: access values supplied by the Architect.
- `clean_docs/`: current project truth.
- `session_logs/`: per-session plans, logs, and reviews.
- `templates/`: reusable session and skill templates.
- `tools/project_book_resume_hook.py`: optional hook helper that reads handoff
  and reminds the platform which Project Book role to resume.

## Clean Docs

Start with `clean_docs/index.md`.

Root clean docs hold high-level truth:

- `00_project_overview.md`
- `01_current_state.md`
- `02_target_direction.md`
- `03_operating_rules.md`
- `04_next_steps.md`
- `05_architecture_defaults.md`
- `06_init_fixer_flow.md`
- `relationships.md`
- `session_index.md`

Module folders are created only for real project areas, services, workflows, or
system boundaries.

## Session Logs

Every session lives under:

```text
session_logs/<YYYY-MM-DD>/<task_slug>/
  plan.md
  logs.md
  review.md
```

The Netrunner updates `logs.md`. The Fixer writes `review.md`.

## Access

The Fixer asks for required logins, passwords, API keys, service links, and
account notes directly in chat, then records them in:

```text
private/access.md
```

Do not duplicate access values in clean docs, logs, reviews, or handoff.

## Handoff

`FIXER_HANDOFF.md` is not a diary. It is the current dashboard:

- compression snapshot;
- current objective;
- Autonomy Mandate state;
- what to read first;
- recent decisions;
- active or pending tasks;
- blockers or deferred questions;
- exact next action;
- exact next Architect command.

It may include an Active Session Cursor as a lightweight recovery hint, but the
actual session files remain the source of truth.

Refresh it after every autonomous review cycle and before pauses, manual
sessions, operator switches, or context compaction risk.

## Resume Role

After compaction or resume, the role is selected from `FIXER_HANDOFF.md`:

- Autonomy Mandate active: continue as Auto Fixer.
- Autonomy Mandate inactive: continue as Fixer.

Platform hooks may inject this reminder, but they do not create project truth
and are not required for the workflow to function.

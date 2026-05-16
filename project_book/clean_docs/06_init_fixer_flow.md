# Init Fixer Flow

This is the canonical Project Book lifecycle source. Entry points may summarize
it, but session behavior should follow this file.

## Core Rule

The Fixer initializes all Project Book sessions and reviews Netrunner output
before it becomes accepted project truth.

The normal path is:

```text
Architect -> Fixer -> Netrunner -> Fixer review -> handoff -> next step
```

For automatic continuation, the same cycle repeats after the Architect gives an
Autonomy Mandate by saying "работай автономно", "запусти автофиксера", "делай
дальше сам", `/auto-fixer`, `$auto-fixer`, or an equivalent instruction.

## Startup Flow

When starting a project, the Fixer:

1. Reads `FIXER_HANDOFF.md`, `clean_docs/session_index.md`,
   `clean_docs/03_operating_rules.md`, and `clean_docs/index.md`.
2. Reads only the additional root docs or module docs needed for the current
   project intent.
3. Runs the first-pass interview from `templates/project_initialization.md`.
4. Requests required access details directly in chat.
5. Records access details in `project_book/private/access.md`.
6. Distills durable project truth into `clean_docs/`.
7. Creates the first bounded Netrunner session.

The first question batch should be minimal. The Fixer may ask a second, sharper
batch after reading or after the first implementation cycle.

## Execution Path

Every session plan must declare one execution path:

```text
Execution Path: autonomous netrunner / manual netrunner
```

Every ready session plan must also include:

```text
Execution Rationale: why this executor is the right one
Architect Launch Command: the exact command the Architect should say next
```

The Fixer repeats the recommended executor and exact launch command whenever it
presents a ready session.

## Autonomous Netrunner

Use this for most bounded work:

- implementation;
- research;
- documentation;
- cleanup;
- local validation;
- external-service work that is part of the project goal;
- tasks that can be finished from a clear plan without step-by-step Architect
  input.

Flow:

```text
Fixer prepares session
  -> autonomous Netrunner subagent / worker
  -> logs.md and validation evidence
  -> status: awaiting fixer review
  -> Fixer review
```

> **Claude Code:**
> ```text
> Run /init-netrunner. Run this as an autonomous Netrunner session using project_book/session_logs/YYYY-MM-DD/task_slug/plan.md.
> ```
>
> **Codex:**
> ```text
> Launch one Codex worker agent. In the worker, activate skill $init-netrunner and run this autonomous Netrunner session using project_book/session_logs/YYYY-MM-DD/task_slug/plan.md.
> ```

## Manual Netrunner

Use this only when the Architect intentionally wants to test or inspect the
product step by step with the Netrunner:

- click-through QA;
- external integration checks that need live human observation;
- batches of small issues discovered during manual use.

Manual sessions are never auto-launched.

> **Claude Code:**
> ```text
> Run /init-netrunner. Continue this manual Netrunner session in a separate Claude Code session: project_book/session_logs/YYYY-MM-DD/task_slug/.
> ```
>
> **Codex:**
> ```text
> Activate skill $init-netrunner. Continue this manual Netrunner session in a separate Codex thread: project_book/session_logs/YYYY-MM-DD/task_slug/.
> ```

## Review Stage

Fixer review starts automatically when the Fixer sees a session marked
`awaiting fixer review`.

For each such session, the Fixer:

- reads `plan.md`, `logs.md`, and relevant changed files;
- inspects validation evidence;
- checks whether project truth updates are reflected in clean docs, module
  indexes, `relationships.md`, and `session_index.md`;
- writes `review.md` using `project_book/templates/fixer_review.md`;
- records `accepted`, `needs rework`, or `blocked`;
- classifies the failure pattern when `needs rework`;
- updates `session_index.md` and the session `logs.md`.

If review records `accepted`, the Fixer may plan the next bounded step.

If review records `needs rework`, the Fixer prepares the smallest useful
rework or research session.

If review records `blocked`, the Fixer checks whether non-conflicting work can
continue. Return to the Architect only for a true blocker.

## Failure Escalation

Use this ladder when something goes wrong:

1. Netrunner fixes clear in-scope validation failures.
2. Netrunner records blocker evidence when cause is unclear or cross-scope.
3. Fixer creates autonomous research when the root cause appears systemic.
4. Fixer creates bounded rework when the fix is clear.
5. Fixer creates manual Netrunner only when human-observable testing is actually
   needed.
6. Fixer asks the Architect when the next decision is business/product judgment
   and blocks later work.

## Auto Mode Loop

`auto-fixer` packages the same lifecycle into a continuous loop:

```text
check Autonomy Mandate
  -> review awaiting session
  -> plan one bounded autonomous session
  -> launch autonomous Netrunner
  -> review the session
  -> refresh FIXER_HANDOFF.md
  -> continue or stop on true blocker
```

Auto Mode starts only when the Architect explicitly gives an Autonomy Mandate in
chat or platform command. The system records that mandate in `FIXER_HANDOFF.md`;
the Architect does not manually fill a separate form.

Auto Mode runs one Netrunner at a time. It never starts manual sessions.

The loop continues when:

- the next step is autonomous;
- required files, validation, and stop condition are clear;
- no true blocker is active.

The loop stops and returns to the Architect when:

- the next decision is business/product judgment and blocks later work;
- required access or environment is missing and no useful non-conflicting work
  remains;
- the next step must be manual by design;
- validation cannot be made meaningful without the Architect;
- the Architect asks to stop or pause.

## Handoff Rule

`FIXER_HANDOFF.md` is refreshed:

- after every autonomous review cycle;
- before moving to the next autonomous session;
- before manual sessions;
- before long pauses, operator switches, or context compaction risk;
- after tool, environment, or subagent failures.

The handoff is a short current-state snapshot, not a growing history file. It
must include the next exact action and next Architect command.

## Compaction Safety

`FIXER_HANDOFF.md` must be current at every iteration boundary.

Two optional helpers can make recovery easier:

1. **Active Session Cursor**: a lightweight hint inside handoff for the latest
   active or recently reviewed session. It is not the source of truth.
2. **Platform hooks**: optional reminders that tell Claude Code or Codex to read
   `FIXER_HANDOFF.md` after startup, resume, or compaction.

The durable recovery mechanism is still the handoff plus the actual session
files: `session_index.md`, `plan.md`, `logs.md`, and `review.md`.

Role selection after compaction is simple:

- active Autonomy Mandate -> Auto Fixer;
- inactive Autonomy Mandate -> Fixer.

## Docs Update Rule

When current project truth changes, update the smallest relevant clean-doc
surface:

- root docs for project-level truth;
- module docs for product, service, workflow, or system-area details;
- module `index.md` files when routing changes;
- `relationships.md` when cross-area dependencies change;
- `session_index.md` when session state changes.

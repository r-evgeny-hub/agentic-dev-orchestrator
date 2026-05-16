# Fixer Handoff

This file is the current recovery snapshot for resuming the Fixer after any
pause, operator switch, or context compaction. Read it first on every Fixer run.

## Active Session Cursor

This is a lightweight recovery hint, not the source of project truth. If this
block conflicts with `session_index.md`, `plan.md`, `logs.md`, or `review.md`,
trust the actual session files and update this handoff.

- Status: `idle`
- Iteration: not applicable
- Last Updated: 2026-05-16T00:00Z
- Active Session Path: none
- Next Action: initialize this Project Book for a real project
- Resume Instruction: see `## Exact Next Architect Command`

## Autonomy Mandate

- Status: inactive
- Last confirmed: not applicable
- Meaning: no autonomous continuation has been requested yet.
- Scope when active: sequential Fixer -> Netrunner -> Fixer-review cycles until
  the goal is reached or a true blocker appears.
- Parallelism: one autonomous Netrunner at a time.

When the Architect says "работай автономно", "запусти автофиксера", "делай
дальше сам", `/auto-fixer`, `$auto-fixer`, or an equivalent instruction, the
Fixer updates this section to active.

## Compression Snapshot

- No cycles have run yet.
- This starter has not been initialized for a real project.

## Current Objective

This workspace is a clean Project Book starter for future AI-assisted projects.
No concrete product project is active yet.

## Read First

For Cold Start:

- `project_book/clean_docs/03_operating_rules.md`
- `project_book/clean_docs/index.md`
- `project_book/clean_docs/session_index.md`

Conditional reads when current intent requires them:

- `project_book/clean_docs/00_project_overview.md`
- `project_book/clean_docs/01_current_state.md`
- `project_book/clean_docs/02_target_direction.md`
- `project_book/clean_docs/04_next_steps.md`
- `project_book/clean_docs/05_architecture_defaults.md`
- `project_book/clean_docs/06_init_fixer_flow.md`
- `project_book/clean_docs/relationships.md`
- `project_book/private/access.md` when the task needs access details

## Recent Decisions

- This is one unified Project Book system for Codex and Claude Code.
- Conversation with the Architect is Russian by default; Project Book artifacts
  are English by default.
- The startup interview is mandatory, but should begin with a minimal question
  batch.
- Required access details are requested in chat and recorded in
  `project_book/private/access.md`.
- Auto Mode is activated by the Architect's instruction, then recorded here as
  an Autonomy Mandate.
- The system runs one autonomous Netrunner at a time.
- True blockers are only issues that stop the current task and also block safe
  later work.
- Deferred questions can be batched while non-conflicting work continues.
- Research is launched during work when repeated or systemic problems appear.
- Platform hooks are optional helpers that may remind agents to read this
  handoff. They do not store project truth or control workflow logic.
- After compaction, active Autonomy Mandate means resume as Auto Fixer; inactive
  Autonomy Mandate means resume as Fixer.

## Active Or Pending Tasks

No active or pending Netrunner sessions.

## Blockers Or Deferred Questions

- No blocker is known.
- The first real product project still needs to be defined by the Architect.

## Exact Next Action

When the Architect chooses a project, run the platform Fixer skill, ask the
startup interview questions, collect required access in chat, record access in
`project_book/private/access.md`, update clean docs with project-specific truth,
and create the first bounded Netrunner session.

## Exact Next Architect Command

> **Claude Code:**
> ```text
> Run /init-fixer. Initialize this Project Book for my project: ask the necessary startup questions, collect required access details in chat, record project truth in clean docs, and create the first bounded Netrunner session with validation and a stop condition.
> ```
>
> **Codex:**
> ```text
> Activate skill $init-fixer. Initialize this Project Book for my project: ask the necessary startup questions, collect required access details in chat, record project truth in clean docs, and create the first bounded Netrunner session with validation and a stop condition.
> ```

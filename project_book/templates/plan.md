# <Session Name>

## Goal

Describe one clear outcome the Netrunner must complete.

## Context & Knowledge

- Why this task exists now.
- What the Netrunner needs to know before acting.
- What must stay out of scope.

## Execution Path

Execution Path: `TBD`

Choose one:

- autonomous netrunner
- manual netrunner

Use `autonomous netrunner` for bounded work that can be finished without
step-by-step Architect input.

Use `manual netrunner` only when the Architect will open a separate session or
thread and work with the Netrunner interactively.

## Execution Rationale

Explain why this task should use the chosen execution path. Keep it short and
operational.

## Architect Launch Command

The Fixer must fill this before marking the session ready.

> **Claude Code — autonomous example:**
> ```text
> Run /init-netrunner. Run this as an autonomous Netrunner session using project_book/session_logs/YYYY-MM-DD/task_slug/plan.md.
> ```
>
> **Claude Code — manual example:**
> ```text
> Run /init-netrunner. Continue this manual Netrunner session in a separate Claude Code session: project_book/session_logs/YYYY-MM-DD/task_slug/.
> ```
>
> **Codex — autonomous example:**
> ```text
> Launch one Codex worker agent. In the worker, activate skill $init-netrunner and run this autonomous Netrunner session using project_book/session_logs/YYYY-MM-DD/task_slug/plan.md.
> ```
>
> **Codex — manual example:**
> ```text
> Activate skill $init-netrunner. Continue this manual Netrunner session in a separate Codex thread: project_book/session_logs/YYYY-MM-DD/task_slug/.
> ```

## Execution Mode

Choose one:

- research
- planning
- implementation
- validation
- documentation
- manual QA
- external service action
- publishing

## Required Files

- `path/to/file` (Reason: why this file matters)

When clean docs are required, start with `project_book/clean_docs/index.md`,
then list exact root docs, module indexes, and focused module files.

Avoid broad read instructions such as `project_book/clean_docs/*.md` unless the
task is specifically a clean-doc inventory or migration.

## Step-by-Step Plan

1. Read this plan.
2. Confirm Execution Path, Execution Rationale, Execution Mode, scope, and stop
   condition.
3. Read Required Files.
4. Execute the smallest useful version of the task.
5. Validate the result.
6. If validation fails inside scope and the fix is clear, fix it and rerun
   validation.
7. If root cause is unclear or systemic, record evidence for a research or
   rework session.
8. Update `logs.md`.
9. Update relevant clean docs if current project truth changed.
10. Update module indexes or `relationships.md` if routing or cross-area
    relationships changed.
11. Update `session_index.md` to `awaiting fixer review`, `blocked`, or
    `needs rework` as appropriate.

## Failure Protocol

- In-scope validation failure: fix and log the validation loop.
- Unknown or systemic root cause: record evidence for Fixer research planning.
- Missing tool, environment, access, or user action: mark blocked only if no
  useful non-conflicting work can continue.
- Product uncertainty: defer the question unless it blocks later work.
- Do not widen scope to make the session appear successful.

## Manual Session Rules

Use this section only for `Execution Path: manual netrunner`. Otherwise write
`not applicable`.

- Product surface under test: TBD
- Small-fix boundary: TBD
- Escalation rules: TBD
- Logging rules across passes: TBD
- Stop condition for the manual thread: TBD

## MCP / Tool Selection

Only include this section when a special tool or connector is needed.

- Tool: `TBD`
- Reason: `TBD`
- Boundary: `TBD`

## Validation

Describe exact checks the Netrunner must run or perform.

Use the validation method that fits the project. If no useful validation exists
and autonomous work would otherwise be guesswork, add the smallest practical
check.

For documentation sessions, include a check that changed clean docs remain
reachable from `project_book/clean_docs/index.md`.

## Stop Condition

State what finished means and what counts as a true blocker.

For manual Netrunner sessions, also state when the Architect should close the
manual pass or return larger issues to the Fixer.

## Out Of Scope

- TBD

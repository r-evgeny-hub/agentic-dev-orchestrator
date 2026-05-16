---
name: fixer-handoff
description: "Use before the Fixer stops, switches operators, crosses an autonomous iteration boundary, or approaches context compaction. Refresh project_book/FIXER_HANDOFF.md."
---

# Fixer Handoff

Use this skill to preserve continuity for the next Fixer.

## Purpose

- Keep `project_book/FIXER_HANDOFF.md` short, current, and actionable.
- Tell the next Fixer exactly where to resume.
- Preserve the Autonomy Mandate state.
- Preserve enough state to resume after context compaction.
- Avoid forcing the next agent to rediscover current state.

## Required Reading

Read only what is needed:

1. `project_book/FIXER_HANDOFF.md`
2. `project_book/clean_docs/session_index.md`
3. `project_book/clean_docs/index.md`
4. Relevant clean docs named by the current task
5. Relevant recent session `plan.md`, `logs.md`, and `review.md`

Read `project_book/private/access.md` only when the next action needs access
details. Do not copy access values into the handoff.

## Required Sections

`FIXER_HANDOFF.md` must include:

- Current Objective
- Read First
- Recent Decisions
- Active Or Pending Tasks
- Blockers Or Deferred Questions
- Exact Next Action
- Exact Next Architect Command

It may also include:

- Autonomy Mandate
- Compression Snapshot
- Active Session Cursor

The cursor is a lightweight recovery hint only. Do not treat it as project
truth if actual session files disagree.

## Writing Rules

- Write artifacts in English unless the Architect asks otherwise.
- Replace the handoff with the current operational snapshot; do not append a
  diary.
- Use exact relative paths.
- Prefer current truth over historical detail.
- Point to `clean_docs/index.md` plus specific relevant module docs.
- Keep Compression Snapshot focused on recent cycles, validation evidence,
  accepted/rework/blocker decisions, deferred questions, and exact resume point.
- If there is no blocker, say so explicitly.
- If questions can wait, list them as deferred instead of stopping the project.
- When next action is Netrunner work, include the exact Architect launch command.
- When a session is `awaiting fixer review`, set next action to Fixer review.

## When To Use

- After every autonomous review cycle.
- Before moving to the next autonomous session.
- Before pauses, operator switches, manual stops, or context compaction risk.
- After tool, environment, or subagent failures.
- Before handing the project to another Fixer.

## Boundaries

- Do not write product code.
- Do not duplicate large parts of clean docs.
- Do not copy access values into the handoff.
- Do not leave stale handoff state after project state changes.

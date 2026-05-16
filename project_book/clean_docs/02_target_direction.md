# Target Direction

## Desired Operating System

This workspace should help the Architect run repeatable AI-assisted project work:

1. Capture the current truth.
2. Convert vague intent into one bounded task.
3. Choose the Netrunner execution path.
4. Log what happened.
5. Review the result.
6. Update the project truth.

## Target Qualities

- Clear enough for a new Codex or Claude Code agent run to resume quickly.
- Small enough that documentation does not become bureaucracy.
- Concrete enough that Netrunner agents do not have to guess.
- Business-aware enough that technical work stays tied to useful outcomes.
- Flexible enough to support different future projects.
- Opinionated enough to give good starting defaults without hardcoding one product's architecture.

## Agent Workflow

```text
Autonomous:
Architect
  -> Fixer
    -> plan.md with Execution Path: autonomous netrunner + Execution Rationale + Architect Launch Command
      -> Netrunner subagent
        -> logs.md + changed files
          -> Fixer reviews
            -> accepted / needs rework
              -> updated clean_docs

Manual:
Architect
  -> Fixer
    -> plan.md with Execution Path: manual netrunner + Execution Rationale + Architect Launch Command
      -> Architect opens a separate platform session/thread
        -> Manual Netrunner works with Architect and appends logs.md
          -> Fixer reviews
            -> accepted / needs rework / follow-up session

Automatic:
Architect gives Autonomy Mandate
  -> Auto Fixer repeats the same lifecycle sequentially
    -> one autonomous Netrunner at a time
      -> Fixer review
        -> handoff refresh
          -> next bounded step or true blocker

After context compaction:
  -> read FIXER_HANDOFF.md
    -> active Autonomy Mandate resumes Auto Fixer
    -> inactive Autonomy Mandate resumes Fixer
```

## What To Avoid

- Building a platform before the first useful product loop.
- Keeping old project history in active docs after it stops helping.
- Giving Netrunner broad missions without exact files, validation, and stop conditions.
- Letting finished work disappear without logs.
- Treating agent output as accepted before review.

# Autonomy Mandate Note

Use this short note only when the Architect gives an autonomous-work instruction
such as "работай автономно", "запусти автофиксера", "делай дальше сам",
`/auto-fixer`, or `$auto-fixer`.

The Architect does not need to manually fill this file. The Fixer records the
mandate in `project_book/FIXER_HANDOFF.md` so the next agent can resume after a
pause or compaction.

## Suggested Handoff Text

```markdown
## Autonomy Mandate

- Status: active
- Granted by: Architect in chat
- Last confirmed: <YYYY-MM-DD HH:MM TZ>
- Meaning: continue sequential Fixer -> Netrunner -> Fixer-review cycles until
  the project goal is reached or a true blocker appears.
- Scope: all actions needed for the project goal, including local work, tests,
  external service actions, account operations, and public publishing.
- Parallelism: one autonomous Netrunner at a time.
- Stop only for true blockers:
  - required access/environment is missing and no useful non-conflicting work remains;
  - business/product judgment is needed before later work can safely continue;
  - validation cannot be made meaningful without Architect input;
  - Architect explicitly stops or pauses the loop.
```

## Writing Rule

Do not create a second source of truth. Once the mandate is recorded in
`FIXER_HANDOFF.md`, keep it there and update it as part of normal handoff
refreshes.

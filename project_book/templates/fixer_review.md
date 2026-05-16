# Fixer Review

## Result

Choose one: `accepted` / `needs rework` / `blocked`

## Session Reviewed

- Session path: `project_book/session_logs/YYYY-MM-DD/task_slug/`
- Execution Path: autonomous netrunner / manual netrunner
- Status before review: awaiting fixer review / blocked

## Scope Check

State whether the Netrunner finished the assigned `plan.md` without widening
scope. If not, name the exact scope drift.

## Files Changed

- TBD

## Validation Observed

Describe the validation evidence reviewed. If validation is missing or weak,
say so directly and decide whether the missing validation is fixable without
Architect input.

## Failure Or Blocker Assessment

Use this when the session hit an error, unclear root cause, environment problem,
tool problem, access problem, or product decision.

- Root cause known: yes / no / partial
- In-scope fix available: yes / no
- Can non-conflicting work continue: yes / no
- Recommended path: accept / bounded rework / research session / manual session / Architect judgment
- Evidence: TBD

## Failure Pattern

Use only if Result = `needs rework`.

Choose one:

- `single bug`: local cause is known. Prepare one bounded rework session.
- `systemic issue`: root cause is unclear or wider than original scope. Prepare
  a research session first, then a fix session.
- `unclear scope`: goal itself is wrong or ambiguous. Return to Architect only
  if this blocks later work.

## Manual Session Check

For `Execution Path: manual netrunner`, state whether Architect-reported issues,
manual passes, fixes, validation, and remaining follow-ups were logged clearly.
Otherwise write `not applicable`.

## Documentation Check

State whether `project_book/clean_docs/`, module indexes, `relationships.md`,
and `session_index.md` were updated, or why no update was needed.

For documentation work, check that changed docs remain discoverable from
`project_book/clean_docs/index.md`.

## Deferred Questions

List questions to ask the Architect later because they do not block current
non-conflicting work. Otherwise write `none`.

## Risks

TBD

## Next Action

State the exact next action. If rework or research is needed, keep it to one
bounded next session.

## Continuation Decision

Choose one: continue automatically / prepare rework / prepare research / prepare manual QA / wait for Architect / not applicable

Use `wait for Architect` only for a true blocker.

## Next Architect Command

If the Architect needs to start a Netrunner session, provide the exact command.
Otherwise write `not applicable`.

# Current State

## Status

No concrete product project is active yet.

## What Exists

- A clean `project_book` structure.
- One unified Project Book workflow for Codex and Claude Code.
- Four required role skills: `init-fixer`, `init-netrunner`,
  `fixer-handoff`, and `auto-fixer`.
- Portable install copies for both platforms under
  `project_book/templates/skills/`.
- Netrunner sessions support two execution paths: autonomous platform
  subagent/worker execution and manual Architect-led execution in a separate
  session or thread.
- Templates for project initialization, session plans, logs, Fixer reviews,
  Autonomy Mandate notes, and visible access storage.
- A rebuild reference for the four required Project Book global skills.
- Architecture defaults for early technical choices.
- An empty `initial_package/` area for future project intake materials.
- `project_book/private/access.md` for real logins, passwords, tokens, account
  notes, and service links requested in chat.
- Claude Code compaction settings with `autoCompactWindow = 400000`.
- Optional hook helpers for resume reminders after compaction or session
  restart.

## What Does Not Exist Yet

- Product code.
- Project-specific requirements.
- Real user/customer inputs.
- Validation examples.
- Deployment or live-system boundaries.
- Current project intake materials.

## Known Constraints

- The Architect is business/product-oriented and values clear explanations over unnecessary technical detail.
- Agents should translate technical choices into product and business consequences.
- Work should stay small enough to review and learn from.
- Project Book itself tracks progress through Project Book files only.
- Autonomous work is sequential: one Netrunner at a time.
- Auto Mode starts from the Architect's instruction and records that instruction
  as an Autonomy Mandate in `FIXER_HANDOFF.md`.

## Open Questions

- What is the first project that should use this Project Book?
- What business outcome should that project optimize for?
- What is the smallest useful first result?
- What should be measured first?
- Which architecture defaults apply, and which should be changed for a deliberate reason?

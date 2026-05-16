# Initial Package

Use this folder for raw or semi-processed intake materials for the current project.

Examples:

- notes from the Architect
- exported docs that still need synthesis
- research dumps
- reference files for the first Fixer pass
- source materials that are useful but not yet clean project truth

## Rules

- Do not treat this folder as current truth by default.
- Summarize durable decisions into `project_book/clean_docs/`.
- Move stale material to `project_book/archive/` when it stops helping active work.
- Do not store real logins, passwords, API keys, tokens, or personal access
  details here. Put those values in `project_book/private/access.md`.
- If an intake file contains access details, move the values to
  `project_book/private/access.md` and leave only a short pointer here.
- Keep large generated artifacts out of this folder unless they are true input
  material for the first Fixer pass.

# Automatic Work Mode

Automatic Work Mode lets a Project Book project continue through multiple
bounded autonomous Netrunner sessions without asking the Architect to start each
one manually.

It starts when the Architect gives an Autonomy Mandate in chat or via platform
command:

```text
работай автономно
запусти автофиксера
делай дальше сам
Run /auto-fixer ...
Activate skill $auto-fixer ...
```

The Fixer records that mandate in `project_book/FIXER_HANDOFF.md`. The Architect
does not manually fill a separate form.

## Loop

```text
check handoff and mandate
  -> review any awaiting-fixer-review session
  -> plan one bounded autonomous session
  -> run one autonomous Netrunner
  -> inspect logs and validation evidence
  -> write Fixer review
  -> refresh FIXER_HANDOFF.md
  -> next bounded autonomous session or true blocker
```

Run only one Netrunner at a time.

## Continue When

Auto Mode may continue when:

- the next step is autonomous;
- required files, validation, and stop condition are clear;
- any open questions can be deferred without conflicting with later work.

## Research During Auto Mode

Research is part of the loop when needed. It is launched when:

- the same problem repeats;
- the root cause appears systemic;
- validation points to a deeper design issue;
- the Fixer cannot plan a reliable fix without understanding the issue first.

Research should produce one practical output: the smallest next development or
rework plan.

## Stop And Return To Architect When

Return to the Architect only for a true blocker:

- a required access, file, account, environment, or service is missing and no
  useful non-conflicting work remains;
- the next decision is business/product judgment that blocks later work;
- validation cannot be made meaningful without the Architect;
- the next step is intentionally manual;
- the Architect asks to stop, pause, switch mode, or inspect manually.

The response should include the exact next decision or command.

## Handoff And Compaction

Refresh `project_book/FIXER_HANDOFF.md` after every review cycle and before any
pause or compaction risk.

The handoff must include:

- Autonomy Mandate state;
- recent accepted, rework, or blocked decisions;
- validation evidence summary;
- deferred questions that matter;
- exact resume point.

It may include an Active Session Cursor or Compression Snapshot as recovery
hints. These hints never override the actual session files.

After compaction, role selection comes from `FIXER_HANDOFF.md`:

- active Autonomy Mandate -> resume as Auto Fixer;
- inactive Autonomy Mandate -> resume as Fixer.

The resume path uses `FIXER_HANDOFF.md`, `clean_docs/session_index.md`, and the
relevant recent session folder instead of relying on chat memory.

#!/usr/bin/env python3
"""Project Book resume helper for Claude Code and Codex hooks.

This script does not store project truth. It only reads FIXER_HANDOFF.md and
returns a short role reminder when a hook can add context.
"""

from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path


CONTINUE_WORDS = (
    "continue",
    "resume",
    "keep going",
    "auto",
    "compact",
    "handoff",
    "дальше",
    "продолж",
    "авто",
    "сжат",
    "контекст",
)

STOP_WORDS = (
    "wait for architect",
    "return to the architect",
    "ask the architect",
    "architect judgment",
    "manual netrunner",
    "manual session",
    "true blocker",
    "goal is reached",
    "stop or pause",
    "pause",
)


def read_stdin_json() -> dict:
    raw = sys.stdin.read().strip()
    if not raw:
        return {}
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return {}


def find_project_root(payload: dict) -> Path:
    candidates = []
    for key in ("cwd", "project_dir"):
        value = payload.get(key)
        if value:
            candidates.append(Path(value))
    env_project = os.environ.get("CLAUDE_PROJECT_DIR") or os.environ.get("CODEX_CWD")
    if env_project:
        candidates.append(Path(env_project))
    candidates.append(Path.cwd())

    for candidate in candidates:
        current = candidate.resolve()
        for path in (current, *current.parents):
            if (path / "project_book" / "FIXER_HANDOFF.md").is_file():
                return path
    return Path.cwd().resolve()


def section(text: str, title: str) -> str:
    pattern = rf"^## {re.escape(title)}\s*$"
    match = re.search(pattern, text, flags=re.MULTILINE)
    if not match:
        return ""
    start = match.end()
    next_match = re.search(r"^## ", text[start:], flags=re.MULTILINE)
    end = start + next_match.start() if next_match else len(text)
    return text[start:end].strip()


def autonomy_active(handoff: str) -> bool:
    mandate = section(handoff, "Autonomy Mandate").lower()
    return bool(re.search(r"status:\s*active\b", mandate))


def should_continue_from_stop(handoff: str, payload: dict) -> bool:
    if payload.get("stop_hook_active") is True:
        return False
    if not autonomy_active(handoff):
        return False

    next_action = section(handoff, "Exact Next Action").lower()
    blockers = section(handoff, "Blockers Or Deferred Questions").lower()
    combined = f"{next_action}\n{blockers}"

    if any(word in combined for word in STOP_WORDS):
        return False
    if "no blocker is known" in blockers:
        return True
    return "blocker" not in blockers


def resume_context(handoff: str) -> str:
    active = autonomy_active(handoff)
    mode = "active" if active else "inactive"
    skill_line = (
        "Autonomy Mandate is active: continue as Auto Fixer "
        "(`/auto-fixer` on Claude Code, `$auto-fixer` on Codex)."
        if active
        else "Autonomy Mandate is inactive: resume as Fixer "
        "(`/init-fixer` on Claude Code, `$init-fixer` on Codex)."
    )

    cursor = section(handoff, "Active Session Cursor")
    next_action = section(handoff, "Exact Next Action")

    lines = [
        "Project Book resume context:",
        f"- Autonomy Mandate: {mode}.",
        f"- {skill_line}",
        "- Read project_book/FIXER_HANDOFF.md first.",
        "- If the handoff has an Active Session Cursor, treat it as a recovery hint, not project truth.",
        "- If the cursor points to a session folder, verify against that session plan/log/review before broad docs.",
        "- Continue one Netrunner at a time. Stop only for a true blocker or explicit Architect pause.",
    ]
    if cursor:
        lines.append("- Current cursor from handoff:")
        cursor_lines = []
        for line in cursor.splitlines():
            if line.strip().lower().startswith("status values"):
                break
            if line.strip() == "" and cursor_lines:
                break
            cursor_lines.append(line)
        lines.extend(f"  {line}" for line in cursor_lines[:8])
    if next_action:
        lines.append("- Exact next action from handoff:")
        lines.extend(f"  {line}" for line in next_action.splitlines()[:8])
    return "\n".join(lines)


def continuation_prompt(handoff: str) -> str:
    return "\n".join(
        [
            "Project Book Auto Fixer appears active.",
            "Read project_book/FIXER_HANDOFF.md first, treat Active Session Cursor as a hint only, activate Auto Fixer behavior (`/auto-fixer` on Claude Code or `$auto-fixer` on Codex), and continue the exact next action if no true blocker is recorded.",
            "Run one Netrunner at a time and refresh FIXER_HANDOFF.md after the review cycle.",
            "Stop only if the handoff records a true blocker, the goal is reached, or the Architect explicitly asked to stop.",
        ]
    )


def main() -> int:
    mode = sys.argv[1] if len(sys.argv) > 1 else "context"
    payload = read_stdin_json()
    root = find_project_root(payload)
    handoff_path = root / "project_book" / "FIXER_HANDOFF.md"
    if not handoff_path.is_file():
        return 0
    handoff = handoff_path.read_text(encoding="utf-8", errors="replace")

    if mode == "stop":
        if should_continue_from_stop(handoff, payload):
            print(continuation_prompt(handoff), file=sys.stderr)
            return 0
        return 0

    if mode == "user-prompt":
        prompt = (payload.get("prompt") or "").lower()
        if not any(word in prompt for word in CONTINUE_WORDS):
            return 0
        print(resume_context(handoff))
        return 0

    if mode in {"session-start", "context"}:
        print(resume_context(handoff))
        return 0

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

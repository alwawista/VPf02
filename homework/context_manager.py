"""Хранение контекста диалогов пользователей в памяти."""

from __future__ import annotations

from config import MAX_CONTEXT_MESSAGES

_contexts: dict[int, list[dict[str, str]]] = {}


def get_messages(user_id: int) -> list[dict[str, str]]:
    return list(_contexts.get(user_id, []))


def add_user_message(user_id: int, content: str) -> None:
    history = _contexts.setdefault(user_id, [])
    history.append({"role": "user", "content": content})
    _trim(history)


def add_assistant_message(user_id: int, content: str) -> None:
    history = _contexts.setdefault(user_id, [])
    history.append({"role": "assistant", "content": content})
    _trim(history)


def clear(user_id: int) -> None:
    _contexts.pop(user_id, None)


def message_count(user_id: int) -> int:
    return len(_contexts.get(user_id, []))


def _trim(history: list[dict[str, str]]) -> None:
    max_messages = max(MAX_CONTEXT_MESSAGES, 2)
    if len(history) > max_messages:
        del history[:-max_messages]

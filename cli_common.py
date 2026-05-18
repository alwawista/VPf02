"""Общие функции для интерактивных CLI-скриптов."""

from __future__ import annotations


def read_chat_params() -> tuple[str, float, int, str, list[dict[str, str]]] | None:
    question = input("Введите ваш вопрос: ").strip()
    if not question:
        print("Вопрос не может быть пустым")
        return None

    temperature = float(input("Введите temperature (0.0-2.0, по умолчанию 0.7): ") or "0.7")
    if not 0.0 <= temperature <= 2.0:
        print("Temperature должен быть от 0.0 до 2.0")
        return None

    max_tokens = int(input("Введите max_tokens (по умолчанию 1000): ") or "1000")
    if max_tokens <= 0:
        print("max_tokens должен быть больше 0")
        return None

    system_message = input("Введите system message (опционально): ").strip()

    messages: list[dict[str, str]] = []
    if system_message:
        messages.append({"role": "system", "content": system_message})
    messages.append({"role": "user", "content": question})

    return question, temperature, max_tokens, system_message, messages


def print_chat_result(answer: str, usage: dict | None) -> None:
    print("\n--- Ответ ---\n")
    print(answer)
    if usage:
        prompt = usage.get("prompt_tokens", 0)
        completion = usage.get("completion_tokens", 0)
        total = usage.get("total_tokens", prompt + completion)
        print(
            f"\n--- Токены: prompt={prompt}, completion={completion}, total={total} ---"
        )

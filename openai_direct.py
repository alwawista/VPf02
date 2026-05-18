"""Запрос к OpenAI через официальную библиотеку."""

from __future__ import annotations

import os

from dotenv import load_dotenv
from openai import OpenAI

from cli_common import print_chat_result, read_chat_params


def main() -> None:
    load_dotenv()

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Ошибка: не найден OPENAI_API_KEY в .env файле")
        return

    model = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")
    client = OpenAI(api_key=api_key)

    params = read_chat_params()
    if params is None:
        return

    _question, temperature, max_tokens, _system_message, messages = params

    print("\nОтправляем запрос к OpenAI...")

    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
        )
    except Exception as exc:
        print(f"Ошибка API: {exc}")
        return

    answer = response.choices[0].message.content or ""
    usage = None
    if response.usage:
        usage = {
            "prompt_tokens": response.usage.prompt_tokens,
            "completion_tokens": response.usage.completion_tokens,
            "total_tokens": response.usage.total_tokens,
        }

    print_chat_result(answer, usage)


if __name__ == "__main__":
    main()

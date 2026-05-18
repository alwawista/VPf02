"""Запрос к OpenAI через ProxyAPI (HTTP requests)."""

from __future__ import annotations

import os

import requests
from dotenv import load_dotenv

from cli_common import print_chat_result, read_chat_params


def main() -> None:
    load_dotenv()

    api_key = os.getenv("PROXYAPI_API_KEY") or os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Ошибка: не найден PROXYAPI_API_KEY (или OPENAI_API_KEY) в .env")
        return

    base_url = os.getenv("PROXYAPI_BASE_URL", "https://api.proxyapi.ru/openai/v1").rstrip("/")
    model = os.getenv("PROXYAPI_MODEL", "gpt-3.5-turbo")
    url = f"{base_url}/chat/completions"

    params = read_chat_params()
    if params is None:
        return

    _question, temperature, max_tokens, _system_message, messages = params

    print("\nОтправляем запрос к ProxyAPI...")

    payload = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens,
    }
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=120)
        response.raise_for_status()
        data = response.json()
    except requests.RequestException as exc:
        print(f"Ошибка HTTP: {exc}")
        if hasattr(exc, "response") and exc.response is not None:
            print(exc.response.text)
        return
    except ValueError as exc:
        print(f"Ошибка разбора JSON: {exc}")
        return

    if "error" in data:
        print(f"Ошибка API: {data['error']}")
        return

    try:
        answer = data["choices"][0]["message"]["content"] or ""
    except (KeyError, IndexError, TypeError):
        print(f"Неожиданный формат ответа: {data}")
        return

    print_chat_result(answer, data.get("usage"))


if __name__ == "__main__":
    main()

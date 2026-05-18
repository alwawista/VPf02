"""Клиент для запросов к LLM (OpenAI или GenAPI)."""

from __future__ import annotations

import logging
from typing import Any

from openai import OpenAI

import config

logger = logging.getLogger(__name__)


def _build_client() -> tuple[OpenAI, str]:
    provider = config.API_PROVIDER

    if provider == "openai":
        return OpenAI(api_key=config.OPENAI_API_KEY), config.CHAT_MODEL
    if provider == "genapi":
        return (
            OpenAI(
                api_key=config.GENAPI_KEY,
                base_url=config.GENAPI_BASE_URL,
            ),
            config.CHAT_MODEL,
        )

    raise RuntimeError(f"Неизвестный провайдер: {provider}")


def chat_completion(
    messages: list[dict[str, str]],
    *,
    temperature: float | None = None,
    max_tokens: int | None = None,
) -> tuple[str, dict[str, Any]]:
    client, model = _build_client()
    temp = config.DEFAULT_TEMPERATURE if temperature is None else temperature
    tokens = config.DEFAULT_MAX_TOKENS if max_tokens is None else max_tokens

    logger.info(
        "LLM request: provider=%s model=%s temperature=%s max_tokens=%s messages=%s",
        config.API_PROVIDER,
        model,
        temp,
        tokens,
        len(messages),
    )

    kwargs: dict[str, Any] = {
        "model": model,
        "messages": messages,
    }

    try:
        response = client.chat.completions.create(
            **kwargs,
            temperature=temp,
            max_tokens=tokens,
        )
    except Exception as first_exc:
        logger.warning("Запрос с temperature/max_tokens не прошёл: %s", first_exc)
        try:
            response = client.chat.completions.create(**kwargs)
        except Exception as second_exc:
            logger.exception("Ошибка LLM API: %s", second_exc)
            raise

    answer = response.choices[0].message.content or ""
    usage: dict[str, Any] = {}
    if response.usage:
        usage = {
            "prompt_tokens": response.usage.prompt_tokens,
            "completion_tokens": response.usage.completion_tokens,
            "total_tokens": response.usage.total_tokens,
        }
        logger.info("LLM usage: %s", usage)

    return answer, usage

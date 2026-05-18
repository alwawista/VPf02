"""Конфигурация бота и LLM-провайдера."""

from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv

_PROJECT_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(_PROJECT_ROOT / ".env")

BOT_TOKEN = os.getenv("BOT_TOKEN", "").strip()

API_PROVIDER = os.getenv("API_PROVIDER", "openai").strip().lower()
CHAT_MODEL = os.getenv("CHAT_MODEL", "gpt-3.5-turbo").strip()
DEFAULT_TEMPERATURE = float(os.getenv("DEFAULT_TEMPERATURE", "0.7"))
DEFAULT_MAX_TOKENS = int(os.getenv("DEFAULT_MAX_TOKENS", "1000"))
MAX_CONTEXT_MESSAGES = int(os.getenv("MAX_CONTEXT_MESSAGES", "20"))

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "").strip()

GENAPI_KEY = os.getenv("GENAPI_KEY", "").strip()
GENAPI_BASE_URL = os.getenv("GENAPI_BASE_URL", "https://proxy.gen-api.ru/v1").rstrip("/")


def validate_config() -> None:
    if not BOT_TOKEN:
        raise RuntimeError("BOT_TOKEN не задан. Заполните .env в корне проекта (см. EnvExample).")

    if API_PROVIDER == "openai" and not OPENAI_API_KEY:
        raise RuntimeError("Для API_PROVIDER=openai нужен OPENAI_API_KEY.")
    if API_PROVIDER == "genapi" and not GENAPI_KEY:
        raise RuntimeError("Для API_PROVIDER=genapi нужен GENAPI_KEY.")
    if API_PROVIDER not in ("openai", "genapi"):
        raise RuntimeError(
            f"Неизвестный API_PROVIDER={API_PROVIDER!r}. "
            "Допустимо: openai или genapi."
        )

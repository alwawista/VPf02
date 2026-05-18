"""Telegram-бот с контекстом диалога и LLM."""

from __future__ import annotations

import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

import config
from api_client import chat_completion
import context_manager

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    stream=sys.stdout,
)
logger = logging.getLogger(__name__)

RESET_PHRASES = {"очистить контекст", "clear context", "reset"}


def _is_reset(text: str) -> bool:
    normalized = text.strip().lower()
    return normalized in RESET_PHRASES


async def cmd_start(message: Message) -> None:
    await message.answer(
        "Привет! Я бот с памятью диалога.\n\n"
        "Пишите вопросы обычными сообщениями.\n"
        "Команды:\n"
        "/reset — очистить контекст\n"
        "или текст «очистить контекст»\n\n"
        f"Провайдер: {config.API_PROVIDER}, модель: {config.CHAT_MODEL}"
    )


async def cmd_reset(message: Message) -> None:
    user_id = message.from_user.id if message.from_user else 0
    context_manager.clear(user_id)
    logger.info("Контекст очищен для user_id=%s", user_id)
    await message.answer("Контекст диалога очищен.")


async def handle_message(message: Message) -> None:
    if not message.from_user or not message.text:
        return

    user_id = message.from_user.id
    text = message.text.strip()

    if not text:
        await message.answer("Отправьте текстовое сообщение.")
        return

    if _is_reset(text):
        context_manager.clear(user_id)
        logger.info("Контекст очищен (фраза) для user_id=%s", user_id)
        await message.answer("Контекст диалога очищен.")
        return

    history = context_manager.get_messages(user_id)
    messages_for_api = history + [{"role": "user", "content": text}]

    logger.info(
        "Запрос от user_id=%s, сообщений в контексте: %s",
        user_id,
        len(messages_for_api),
    )

    try:
        answer, usage = await asyncio.to_thread(chat_completion, messages_for_api)
    except Exception as exc:
        logger.exception("Ошибка при запросе к LLM: %s", exc)
        await message.answer(f"Ошибка при обращении к модели: {exc}")
        return

    context_manager.add_user_message(user_id, text)
    context_manager.add_assistant_message(user_id, answer)

    suffix = ""
    if usage.get("total_tokens"):
        suffix = (
            f"\n\n[токены: {usage.get('prompt_tokens', 0)}+"
            f"{usage.get('completion_tokens', 0)}="
            f"{usage.get('total_tokens', 0)}]"
        )

    await message.answer(answer + suffix)


async def main() -> None:
    config.validate_config()

    bot = Bot(token=config.BOT_TOKEN)
    dp = Dispatcher()

    dp.message.register(cmd_start, CommandStart())
    dp.message.register(cmd_reset, Command("reset"))
    dp.message.register(handle_message, F.text)

    logger.info(
        "Бот запущен (provider=%s, model=%s)",
        config.API_PROVIDER,
        config.CHAT_MODEL,
    )
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

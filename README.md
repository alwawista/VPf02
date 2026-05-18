# VPf02 — OpenAI, ProxyAPI, GenAPI и Telegram-бот

Учебный проект: CLI-скрипты для LLM и Telegram-бот (домашнее задание в папке [homework/](homework/)).

## Установка

```bash
cd VPf02
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Скопируйте `EnvExample` в `.env` в **корне** проекта. Для бота: `BOT_TOKEN` + **либо** `OPENAI_API_KEY`, **либо** `GENAPI_KEY` (`API_PROVIDER=openai` или `genapi`).

## CLI-скрипты

```bash
python openai_direct.py
python openai_proxyapi.py
python genapi_chat.py
```

Интерактивно: вопрос, temperature (0.0–2.0), max_tokens, system message (опционально).

## Telegram-бот (ДЗ)

```bash
python homework/bot.py
```

Код и отчёт: [homework/README.md](homework/README.md)

## Сдача

https://github.com/alwawista/VPf02

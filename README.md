# VPf02 — OpenAI, ProxyAPI, GenAPI и Telegram-бот

Учебный проект: CLI-скрипты для LLM и Telegram-бот (домашнее задание в папке [homework/](homework/)).

## Установка

```bash
cd VPf02
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

- CLI: `EnvExample` → `.env` в корне проекта.
- Бот: [homework/EnvExample](homework/EnvExample) → `homework/.env` или тот же `.env` в корне.

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

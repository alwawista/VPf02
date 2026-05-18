# Домашнее задание VPf02

## Выполнено

### 1. Telegram-бот с контекстом

| Требование | Реализация |
|------------|------------|
| Стек | aiogram 3 + `api_client.py` (OpenAI SDK) |
| Контекст | `context_manager.py`, dict в памяти |
| Команды | диалог; `/reset` и «очистить контекст» |
| Ключи | `BOT_TOKEN` + `OPENAI_API_KEY` **или** `GENAPI_KEY` — [EnvExample](EnvExample) → `homework/.env` или `../.env` |
| Логи | параметры запроса и ошибки в консоль (`logging`) |

**Файлы:** [bot.py](bot.py), [config.py](config.py), [context_manager.py](context_manager.py), [api_client.py](api_client.py), [EnvExample](EnvExample)

**Запуск** (из корня проекта, после `pip install -r requirements.txt`):

```bash
python homework/bot.py
```

### 2. CLI-скрипты урока (корень репозитория)

- `openai_direct.py` — OpenAI SDK
- `openai_proxyapi.py` — ProxyAPI, `requests`
- `genapi_chat.py` — GenAPI, `requests`

## Таблица экспериментов

| Модель | temperature | max_tokens | № прогона | Эффект (сжатость/креатив) | Токены (in/out/total) | ~стоимость |
|--------|-------------|------------|-----------|---------------------------|------------------------|------------|
| gpt-3.5-turbo | 0.7 | 1000 | 1 | «Привет, как дела?» | | |
| gpt-3.5-turbo | 0.1 | 1000 | 2 | тот же вопрос | | |
| gpt-3.5-turbo | 0.1 | 1000 | 3 | скрипт транскрибации (Whisper) — строгий код | | |
| gpt-3.5-turbo | 1.0 | 1000 | 4 | тот же промпт — более вольный код | | |
| gpt-4.1-2025-04-14 | 0.7 | 1000 | 5 | транскрибация — точнее код | | |
| gpt-4.1-2025-04-14 | 0.7 | 1000 | 6 | system: преподаватель Python + типы данных | | |

Сценарии: см. [корневой README](../README.md).

## Сдача

**GitHub:** https://github.com/alwawista/VPf02

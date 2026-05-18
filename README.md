# Домашнее задание VPf02

Telegram-бот с контекстом диалога (aiogram + OpenAI или GenAPI).

## Установка

```bash
git clone https://github.com/alwawista/VPf02.git
cd VPf02
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Скопируйте `EnvExample` в `.env`. Нужны `BOT_TOKEN` и **либо** `OPENAI_API_KEY`, **либо** `GENAPI_KEY` (`API_PROVIDER=openai` или `genapi`).

## Запуск

```bash
python bot.py
```

## Файлы проекта

| Файл | Назначение |
|------|------------|
| `bot.py` | логика Telegram |
| `config.py` | настройки из `.env` |
| `context_manager.py` | контекст в памяти |
| `api_client.py` | запросы к LLM |
| `EnvExample` | шаблон переменных окружения |

## Выполнено по ТЗ

| Требование | Реализация |
|------------|------------|
| Стек | aiogram 3 + `api_client.py` |
| Контекст | `context_manager.py`, dict в памяти |
| Команды | диалог; `/reset` и «очистить контекст» |
| Ключи | через `.env` |
| Логи | параметры запроса и ошибки (`logging`) |

## Таблица экспериментов

| Модель | temperature | max_tokens | № прогона | Эффект (сжатость/креатив) | Токены (in/out/total) | ~стоимость |
|--------|-------------|------------|-----------|---------------------------|------------------------|------------|
| gpt-3.5-turbo | 0.7 | 1000 | 1 | «Привет, как дела?» | | |
| gpt-3.5-turbo | 0.1 | 1000 | 2 | тот же вопрос | | |
| gpt-3.5-turbo | 0.1 | 1000 | 3 | скрипт транскрибации — строгий код | | |
| gpt-3.5-turbo | 1.0 | 1000 | 4 | тот же промпт — более вольный код | | |
| gpt-4.1-2025-04-14 | 0.7 | 1000 | 5 | транскрибация — точнее код | | |
| gpt-4.1-2025-04-14 | 0.7 | 1000 | 6 | system: преподаватель Python + типы данных | | |

## Сдача

https://github.com/alwawista/VPf02

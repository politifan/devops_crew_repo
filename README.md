# DevOps Crew Training Site

Простой FastAPI-сайт для практики DevOps-процессов: тесты, GitHub Actions, Docker,
деплой на сервер и перенос изменений в `dev`-ветку.

## Локальный запуск

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
uvicorn app.main:app --reload
```

На Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements-dev.txt
uvicorn app.main:app --reload
```

Сайт будет доступен на `http://127.0.0.1:8000`.

## Проверки

```bash
pytest
ruff check .
```

## Docker

```bash
docker build -t devops-crew-training-site .
docker run --rm -p 8000:8000 devops-crew-training-site
```

Или через Compose:

```bash
docker compose up --build
```

## Полезные endpoint-ы

- `/` - HTML-страница.
- `/health` - health-check для балансировщика, CI и мониторинга.
- `/api/info` - простой JSON API.
- `/docs` - Swagger UI от FastAPI.

## Учебный сценарий

Задания для DevOps-разработчика лежат в [docs/devops-training.md](docs/devops-training.md).

## Что показывает проект

Учебный стенд для проверки пути «изменение кода → тесты → контейнер → проверка
доступности». Это портфолио практики, без заявления о production SLA или
коммерческом масштабе. Исходное приложение содержит HTML, JSON API и health endpoint.

| Возможность | Где проверить |
| --- | --- |
| HTML, статика и FastAPI | `app/main.py`, `app/templates`, `app/static` |
| Автоматические проверки HTTP | `tests/test_app.py` |
| Сборка и запуск контейнера | `Dockerfile`, `docker-compose.yml` |
| CI для push и pull request | `.github/workflows/ci.yml` |

CI запускает pytest и Ruff, отдельно собирает контейнер и проверяет `/health`.
Статус конкретного запуска виден во вкладке Actions. Публикация образа и деплой
на внешний сервер не настроены; соответствующие пункты в учебном задании — план.

Для локальных проверок запускайте команды из корня репозитория:

```bash
python -m pytest tests/ -q
python -m ruff check .
docker compose config --quiet
```

После `docker compose up --build -d`:

```bash
curl --fail http://127.0.0.1:8000/health
docker compose ps
docker compose logs --tail=50 web
docker compose down
```

`/health` подтверждает ответ процесса; он не проверяет внешние зависимости и не
доказывает доступность сервиса извне. Стенд не требует секретов или платного облака.
На общем сервере публикуйте порт только за настроенным прокси и ограничением доступа.

Подробности демонстрации и диагностики: [портфолио проекта](docs/portfolio.md).

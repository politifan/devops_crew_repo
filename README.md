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

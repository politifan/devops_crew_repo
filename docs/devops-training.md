# DevOps training tasks

Этот проект специально маленький, чтобы на нем было удобно тренировать весь путь
от pull request до деплоя.

## 1. Dev branch

1. Создать ветку `dev` от `main`.
2. Настроить правило: все изменения сначала идут в `dev`.
3. После проверки переносить изменения из `dev` в `main`.

## 2. Tests

1. Установить зависимости из `requirements-dev.txt`.
2. Запустить `pytest`.
3. Запустить `ruff check .`.
4. Добавить новый тест для `/api/info`.

## 3. GitHub Actions CI

Создать workflow, который на `pull_request` и `push` выполняет:

1. Checkout репозитория.
2. Установку Python 3.12.
3. Установку зависимостей.
4. `ruff check .`.
5. `pytest`.

## 4. Docker image

Создать отдельный workflow или job, который:

1. Собирает Docker image.
2. Запускает контейнер.
3. Проверяет `/health`.
4. Публикует image в GitHub Container Registry или другой registry.

## 5. Server deploy

Один из вариантов деплоя:

1. Подключиться к серверу по SSH.
2. Обновить код или скачать новый Docker image.
3. Перезапустить приложение через `docker compose`.
4. Проверить `/health`.

## 6. Production checklist

- Секреты хранятся в GitHub Actions Secrets, а не в репозитории.
- Деплой запускается только после успешных тестов.
- Есть health-check.
- Есть rollback-план.
- Есть понятная схема веток: `main`, `dev`, feature branches.

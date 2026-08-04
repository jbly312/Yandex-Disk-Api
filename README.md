# Yandex Disk API Tests

[Live Allure Report](https://jbly312.github.io/Yandex-Disk-Api/2/index.html)

Автотесты REST API Яндекс.Диска (`https://cloud-api.yandex.net`).

## Стек

Python 3.14.0 · pytest · requests · python-dotenv · pydantic · allure-pytest · GitHub Actions

## Что покрыто

| Метод | Проверки                                                                                      |
|---|-----------------------------------------------------------------------------------------------|
| GET | информация о диске, метаданные ресурса, отсутствие ресурса после удаления, содержимое корзины |
| PUT | создание папки (201), повторное создание (409), восстановление из корзины                     |
| POST | копирование, перемещение, копирование на занятый путь (409)                                   |
| DELETE | безвозвратное удаление (204), мягкое удаление в корзину, удаление из корзины                  |

Всего 13 тестов. Валидация схемы ответов через pydantic (`DiskInfo`, `Resource`, `FileResource`).

## Запуск

```bash
pip install -r requirements.txt

cp .env.example .env    # вписать OAuth-токен

pytest -v
```

## Allure

```bash
pytest --alluredir=allure-results
allure serve allure-results
```

Отчёт также публикуется автоматически в CI на каждый push — ссылка вверху README.

Локальный просмотр требует Allure CLI — утилита ставится отдельно, через pip не устанавливается.

## Структура

```
api/
├── client.py            HTTP-клиент: сессия, авторизация, Allure-вложения
└── disk_api.py          обёртки над эндпоинтами Диска
models/
├── disk_info.py         pydantic-модель ответа /v1/disk
└── resource.py          pydantic-модели ресурса (Resource, FileResource)
tests/
├── conftest.py          фикстуры, изоляция и уборка тестовых данных
├── test_disk_info.py
├── test_folders.py
├── test_operations.py
└── test_trash.py
config.py
```

## CI

GitHub Actions запускает тесты на каждый push и pull request в `main`.
Allure-отчёт собирается и публикуется на GitHub Pages, история прогонов сохраняется.

## Примечания

- Все операции выполняются внутри `/autotests`, папка создаётся и удаляется автоматически.
- Пути генерируются с UUID — тесты не конфликтуют между собой.
- Токен передаётся через `.env` локально и через GitHub Secrets в CI.


# Сервис тестирования
Сервис делится на два режима: сервер и воркер

## Структура

- `application/` - слой приложения
  - `<module-name>/`
    - `usecases/`
      - `__init__.py` - экспортирует все классы юзкейсов 
      - `<usecase-name>.py` - отдельный файл на каждый юзкейс 
    - `<gateway-name>.py` - если нужен какой-то гейтвей только для этого модуля, то в папке модуля
    - `exceptions.py` - исключения, которые используются в модуле
  - `transactions.py` - гейтвей для использования транзакций в юзкейсах
  - `<gateway-name>.py` - глобальные гейтвеи
- `domain/` - слой домена
  - `<module-name>/`
    - `entites.py` - сущности в виде датаклассов модуля
    - `repositories.py` - интерфейсы репозиториев сущностей
    - `exceptions.py` - исключения, которые может вызвать репозиторий
    - `dtos.py` - (Опционально) модуль (возможно, в виде папки) с DTO в виде датаклассов
    - `enums.py` - (Опционально) енамы для сущностей в этом модуле
  - `exceptions.py` - базовые исключения сущностей, от которых должны наследоваться исключения в модулях в этом слое
- `infrastructure/` - слой инфраструктуры
  - `database/` - всё, что связано с sqlalchemy
    - `alembic/` - миграции
    - `repositories/` - реализации репозиториев в бд
      - `<module-name>/`
        - `mappers.py` - мапперы из/в бд сущностей/dto (желательно использовать adaptix)
        - `models.py` - модели sqlalchemy для сущностей этого модуля
        - `repositories.py` - реализация репозиториев из доменного слоя, используя sqlalchemy модели
      - `repository.py` - базовый sqlalchemy репозиторий, который содержит общие методы (CRUD) для работы с сессиями. Умеет запускать и маппить запросы. Требует передачи сессии и конфига
    - `mappers.py` - базовый retort, от которого желательно наследоваться в мапперах внутри модулей. Вероятно в будущем появятся общие типы для маппинга из/в бд
    - `postgres.py` - Base для моделей, нейминг для alembic, получение engine и sesionmaker
    - `transactions.py` - реализация гейтвея транзакций из слоя приложений
  - `http/` - всё, что связано с fastapi
    - `api/`
      - `v1/` отдельные роуты для каждой версии api (пока что v1)
        - `__init__.py` - роут, который объединяет роуты всех модулей
        - `<module-name>/`
          - `__init__.py` - экспорт роутера с соответствующим названием 
          - `mappers.py` - маппинг из/в сущностей/дто pydantic и сущностей/дто в слое домена/приложения
          - `models.py` - pydantic модели (необходимо наследовать от CamelBase) для сериализации в api
          - `router.py` - роутер и эндпоинты (для работы dishka необходимо ставить `route_class=DishkaRoute` роутеру!); в эндпоинтах обычно происходит просто маппинг и вызов юзкейсов
        - `models.py` - CamelBase и ErrorModel для openapi
        - `retort.py` - базовый retort для мапперов внутри модулей
    - `app.py` - создание и настройка приложения FastAPI
  - `providers/` - провайдеры для dishka
    - `container.py` - функция для создания контейнеров из всех провайдеров
    - `config.py` - провайдер конфига
    - `database.py` - провайдер всего необходимого для работы с sqlalchemy
    - `repositories.py` - провайдер реализаций репозиториев с использованием sqlalchemy
    - `usecases.py` - провайдер всех юзкейсов
  - `config.py` - конфиг приложения
  - `server.py` - создание app для режима сервера
  - `worker.py` - app для режима воркера
- `__main__.py` - точка входа приложения с параметра режима

## Как запускать

### Инфраструктура
1. Создайте .env файл (можно скопировать значения из `.env.example`)
2. Локально запустите необходимую инфраструктуру

`docker compose -f ./docker-compose.dev.yaml up -d`

или

`podman-compose -f ./docker-compose.dev.yaml up -d`

### Установите зависимости

`poetry install` (если poetry не установлен: `pip install poetry`)

### Запустите миграции

`alembic upgrade head`

или

`poetry run alembic upgrade head`

### PyCharm (Windows)
Терминал PyCharm некорректно обрабатывает перезагрузку uvicorn, поэтому в настройках конфигурации запуска необходимо включить `Modify options -> Emulate terminal in output console`

Также в scripts укажите server (если хотите запускать в режиме сервера)

### Остальное
Со включённым venv:
`python __main__.py server` или worker

Через poetry: `poetry run python __main__.py server` или worker

## Как создавать миграции

Убедитесь, что ваши модели (и соответствующие репозитории) попадают в провайдер

`alembic revision --autogenerate -m "message to migration (e.g. added users models)"`

или

`poetry run alembic revision --autogenerate -m "msg"`

После этого их нужно применить через `alembic upgrade head`
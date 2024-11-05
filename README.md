# Тестовое задание

Тестово задание для DOCLUB-TV.

## Установка

- Установить [Docker](https://hub.docker.com/)

## Создать .env файл
- DJ__SECRET_KEY - секретный ключ от Django, 'secret'
- DJ__DEBUG - Режим отладки, пример 'true'
- DJ__ALLOWED_HOSTS - Доступные хосты для Django, пример 'localhost,127.0.0.1'
- DJ__CSRF_TRUSTED_ORIGINS - Доступные хосты для небезопасных HTTP запросов в Django, пример https://*.ngrok-free.app
- POSTGRES_DSN - Ссылка для подключения к базе данных Postgres, пример postgres://nexus_user:12345@127.0.0.1:5432/course


```shell
$ docker-compose up -d
```

## Создать суперпользователя

```shell
$ docker compose run --rm django python manage.py createsuperuser --no-input
```

## Вход в админку
- Перейдите по http://127.0.0.1:8000/admin

## Swagger, автодокументация для разработчиков
- Перейдите по http://127.0.0.1:8000/swagger

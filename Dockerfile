FROM python:3.10

ARG BASE_DIR=/opt/app

ENV \
    # python
    PYTHONUNBUFFERED=1 \
    # prevents python creating .pyc files
    PYTHONDONTWRITEBYTECODE=1 \
    \
    # poetry
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    \
    # pip
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

RUN curl -sSL https://install.python-poetry.org | POETRY_VERSION=1.8.4 python3 -
ENV PATH="/root/.local/bin:${PATH}"

WORKDIR ${BASE_DIR}
COPY ./pyproject.toml ./poetry.lock ./
RUN poetry install --no-ansi

WORKDIR ${BASE_DIR}/src

ENV PYTHONPATH "$PYTHONPATH:${BASE_DIR}/src/:${BASE_DIR}/src/.contrib-candidates"

COPY ./src ./

ENV \
    DJANGO_SETTINGS_MODULE=project.settings \
    PORT=80

EXPOSE 80/tcp
VOLUME ["/media"]

RUN \
    DJ__SECRET_KEY=empty \
    POSTGRES_DSN=postgres://user:password@db:5432/not-exist \
    ./manage.py collectstatic --noinput

ENTRYPOINT ["sh", "-c", "python manage.py migrate && exec gunicorn project.wsgi:application --access-logfile -"]

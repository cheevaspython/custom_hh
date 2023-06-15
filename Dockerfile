
FROM python:3.11

ARG ENV

ENV ENV=${ENV} \
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=1.4.0

RUN apt-get -y install libpq-dev
RUN pip install "poetry==$POETRY_VERSION"

WORKDIR /fast_api_hh
COPY poetry.lock pyproject.toml /fast_api_hh/

RUN poetry config virtualenvs.create false \
  && poetry install $(test "$ENV" == production && echo "--no-dev") --no-interaction --no-ansi

COPY . /fast_api_hh

EXPOSE 8000
RUN adduser --disabled-password docker-admin
USER docker-admin 



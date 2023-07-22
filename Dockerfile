# Pull base image
FROM --platform=arm64 python:3.10.4-slim-bullseye

#set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=1.1.11 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_CACHE_DIR='/var/cache/pypoetry' \
    PYTHONDONTWRITEBYTECODE=1 \
    pYTHONUNBUFFERED=1 

# Set working directory
WORKDIR /code

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    curl \
    build-essential \
    libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

# Install project dependencies
COPY poetry.lock pyproject.toml /code/
RUN $HOME/.poetry/bin/poetry install --no-dev --no-interaction --no-ansi

# Install depencies for the project
COPY ./requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt

# Copy project
COPY . /code/
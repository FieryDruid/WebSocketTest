FROM python:3.10.9-slim-buster

WORKDIR /opt/websocket_test

# Установка прод зависимостей
RUN pip install poetry==1.4.2 --no-cache-dir && \
    poetry config virtualenvs.create false

COPY poetry.lock pyproject.toml /opt/websocket_test/
RUN poetry install --without dev --no-interaction --no-ansi && \
    rm -rf ~/.cache/pypoetry/cache/ && \
    rm -rf ~/.cache/pypoetry/artifacts/

COPY . /opt/websocket_test/

RUN chmod +x run.sh

EXPOSE 9000

CMD ./run.sh

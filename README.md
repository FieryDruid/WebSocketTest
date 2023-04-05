# WebSocketTest

Для запуска проекта достаточно собрать и запустить контейнер:

```bash
docker-compose -f production.yml build
```

и

```bash
docker-compose up
```

Либо при помощи [poetry](https://python-poetry.org/) установить зависимости и запустить проект локально:

```bash
poetry install --without dev
```

и

```bash
poetry run main.py
```
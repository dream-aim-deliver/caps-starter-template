# Kernel Planckster for Satellite Data Augmentation

*Data Systems Group @MPI-SWS*

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


## Features


## Installation


## Developer Tips

### Database Models

### Autogenerate Alembic Migrations

```bash
cd tests
docker compose up -d
cd ../
alembic upgrade head
alembic revision --autogenerate -m "migration message"
alembic upgrade head
alembic downgrade base
alembic upgrade head
cd tests
docker compose down
```

You can access `adminer` at `http://localhost:8080` to check the database. The credentials are:
```
System: PostgreSQL
Server: kp-db
Username: postgres
Password: postgres
Database: kp-test
```

Before submitting a pull request, please:

1. Run mypy, at the root of the project, and fix all of the errors:
```bash
poetry run mypy .
```
2. Run black, at the root of the project
```bash
poetry run black .
```

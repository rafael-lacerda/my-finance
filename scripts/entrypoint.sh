#!/bin/bash

# Run database migrations using Alembic
poetry run alembic upgrade head

# Start application
poetry run uvicorn my_finance.main:app --host 0.0.0.0 --port 80

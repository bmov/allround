# Allround: Ultimate CRUD helper

![Python version supports](https://img.shields.io/badge/python-3.10_|_3.11_|_3.12_|_3.13-007ec6)

Allround is a tool that creates custom databases and CRUD scenarios to make your web services.

Similar to a Contents Management System, that makes it easy for manage data.

# Development stack

Python 3, Connexion-based web app.

The following DBMSs will be supported: MySQL >= 8.0, MariaDB, PostgreSQL, SQLite

# Run

## Configure

- Copy `.env.server` to `.env`.
- Edit `SQL_DATABASE_URI`:

  ```
  # mysql
  mysql+aiomysql://user:password@localhost/db_name

  # postgresql
  postgresql+asyncpg://user:password@localhost/db_name

  # sqlite
  sqlite+aiosqlite:///path
  ```

- Edit `APP_SECRET`. This recommend a minimum of 32 characters [0-9a-zA-Z].

## Run

```bash
# Create venv
python -m venv .venv

# unix
source .venv/bin/activate

# windows
./venv/Scripts/activate

# Install packages
pip install -r ./requirements.txt

# Upgrade the database
alembic upgrade head

# Run
uvicorn main:app # add '--reload' to watch the source directory
```

# Swagger UI

http://localhost:8000/api/ui/

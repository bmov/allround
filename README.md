# Allround: Ultimate CRUD helper

![Python version supports](https://img.shields.io/badge/python-3.9_|_3.10_|_3.11_|_3.12-007ec6)

Allround is a tool that creates custom databases and CRUD scenarios to make your web services.

Similar to a Contents Management System, that makes it easy for manage data.

# Development stack

Python 3, Connexion-based web app.

The following DBMSs will be supported: MariaDB, PostgreSQL, SQLite

# Run

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

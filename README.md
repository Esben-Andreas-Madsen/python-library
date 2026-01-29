# Python-library
A simple python online-library with a many-to-many Author<->Book relation

Technologies used:
- SQAlchemy
- SQLite DB
- Django
- Flask
- pytest

Also includes an automatic integration test in `.github/workflows/pytest.yaml` that runs every push/pull on main branch.

Flow of application: DB <-> DAO <-> Services <-> API <-> Frontend

## Todo
- make data searchable
- update api

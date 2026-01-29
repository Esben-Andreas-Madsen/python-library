# Python-library
A simple python online-library with a many-to-many Author<->Book relation

How to run:
1. clone repository your preffered way
2. install requirements `pip install -r requirements.txt`
3. run the app `python run.py`
4. head to `http://localhost:5000/`

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
- add docker-compose option to run

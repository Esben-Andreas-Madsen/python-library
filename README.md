# python-library

## Thoughts / would've done differently / wish I knew before implementing

#### Would've-

- used sqalchemy from the very beginning as this would've allowed me to implement </br>
  tests way easier, and not write SQL (although writing SQL is a usefull skill)
- set up `create_app()` method in `app.py` so that I could include a `ProdConfig` and </br>
  `TestConfig` where I define database path, also for testing purposes and loose coupling
- included more subfolders, such as `/app`, `/configs`, and a `run.py` access point

Seems like these changes would take a bit of refactoring and time </br>
The test in `/tests/test_app.py` currently doesn't utilize the mock_db, but the actual db </br>
When I wanted to change the `db_path` I came to the conclusion, refactoring it a bit of a task atm </br>
So what do you do - you put in on the board and wait for someone else to pick it up (this is a one-man project)

### TODO:
- refactor model and dao classes to use sqalchemy
- refactor `app.py`
- add folder structure
- add `run.py`
- add prod & test configs for app

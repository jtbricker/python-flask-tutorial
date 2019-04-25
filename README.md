# Flask App

A simple flask blog application following Miguel Grinberg's [The Flask Mega Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)

## Requirements 

1. Python 3
1. `pipenv`

## Setup

To ensure that required dependencies are install, run setup and start commands using `pipenv run [command]`

### Run the Application

```bash
pipenv run python run.py
```

### Create Database and Run Intial Migrations

Note: Application currently uses stubbed data. But the initial configuration to write to a database has been included.

```bash
pipenv run python db_create.py
pipenv run python db_migrate.py
pipenv run python db_upgrade.py
```
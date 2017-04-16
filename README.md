# SETUP
## Download Packages
pip install flask
pip install flask-login
pip install flask-openid
pip install flask-mail
pip install flask-sqlalchemy
pip install sqlalchemy-migrate
pip install flask-whooshalchemy
pip install flask-wtf
pip install flask-babel
pip install guess_language
pip install flipflop
pip install coverage

## Run db creation script
./db_create.py

## Create the initial db migration
./db_migrate.py

## Apply the migration
./db_upgrade.py

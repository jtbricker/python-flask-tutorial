# SETUP
## Create Virtual Env
pip install virtualenv
virtualenv flask
./flask/Scripts/activate

## Download Packages
./flask/Scripts/pip install flask
./flask/Scripts/pip install flask-login
./flask/Scripts/pip install flask-openid
./flask/Scripts/pip install flask-mail
./flask/Scripts/pip install flask-sqlalchemy
./flask/Scripts/pip install sqlalchemy-migrate
./flask/Scripts/pip install flask-whooshalchemy
./flask/Scripts/pip install flask-wtf
./flask/Scripts/pip install flask-babel
./flask/Scripts/pip install guess_language
./flask/Scripts/pip install flipflop
./flask/Scripts/pip install coverage

## Create necessary file structure
mkdir tmp

## Run db creation script
./db_create.py

## Create the initial db migration
./db_migrate.py

## Apply the migration
./db_upgrade.py

## May need to Wipe Posts and Delete the Search Database
# ./db_purge_posts.py
# rm -R ./search.db

# Set email username and password as environment variables
export MAIL_USERNAME=username
export MAIL_PASSWORD=password 
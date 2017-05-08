import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
WHOOSH_BASE = os.path.join(basedir, 'search.db')
MAX_SEARCH_RESULTS = 50


WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

OPENID_PROVIDERS = [
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'}]

# email server
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

# administrator list
ADMINS = ['justintbricker@gmail.com']

# pagination
POSTS_PER_PAGE = 3

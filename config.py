import os
basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
SECRET_KEY = ''

SQLALCHEMY_DATABASE_URI = '@10.0.1.211/master'
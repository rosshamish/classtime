
import os

SECRET_KEY = os.environ.get('SECRET_KEY', 'debug')
if SECRET_KEY == 'debug':
    DEBUG = True
else:
    DEBUG = False

SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:////tmp/classtime.db')


import os
from classtime.logging import logging
logging = logging.getLogger(__name__)

SECRET_KEY = os.environ.get('SECRET_KEY', 'debug')
if SECRET_KEY == 'debug':
    DEBUG = True
else:
    DEBUG = False

SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:////tmp/classtime.db')
logging.info('Using SQLALCHEMY_DATABASE_URI {}'.format(SQLALCHEMY_DATABASE_URI))

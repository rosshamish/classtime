
from classtime import app

from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.restless import APIManager
from flask.ext.cors import CORS

db = SQLAlchemy(app)

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
api_manager = APIManager(app, flask_sqlalchemy_db=db)

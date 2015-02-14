import os

from flask import Flask, request, Response
from flask import render_template, url_for, redirect, send_from_directory
from flask import send_file, make_response, abort

from classtime import app

# Initializes the Flask-Restless API
import classtime.api.api
import classtime.api.apiv1

# flask-sqlalchemy database
from classtime.core import db

@app.errorhandler(404)
def page_not_found(e):
    return make_response(open('classtime/templates/404.html').read()), 404

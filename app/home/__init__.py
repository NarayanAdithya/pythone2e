from flask import Blueprint

home: Blueprint = Blueprint('home', __name__)

from . import routes

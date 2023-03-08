from flask import Blueprint

bp = Blueprint('users', __name__)

from app.user_blueprint.api import user
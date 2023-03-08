from flask import Blueprint

bp = Blueprint('arrangements', __name__)

from app.arrangement_blueprint.api import arrangement
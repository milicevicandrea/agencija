from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("SQLALCHEMY_DATABASE_URI")
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.arrangement_blueprint import bp as arrangements_bp  #TODO promeni u arrangements i users! - done
from app.user_blueprint import bp as users_bp

app.register_blueprint(arrangements_bp)
app.register_blueprint(users_bp)



import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from app.config import Config

app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), 'templates'))
app.config.from_object(Config)

# Initialize extensions
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)
migrate = Migrate(app, db)

from app.models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

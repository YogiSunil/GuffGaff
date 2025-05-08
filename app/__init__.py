from flask import Flask
from .config import Config
from .extensions import db, login_manager, bcrypt
from  .auth.routes import auth_bp
from .main.routes import main_bp
from app.models import User


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)

    bcrypt.init_app(app)

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(main_bp)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app

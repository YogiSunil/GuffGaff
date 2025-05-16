from flask import Flask
from app.extensions import db, login_manager, bcrypt, migrate
from app.routes.auth import auth_bp
from app.routes.main import main_bp
from app.routes.chat import chat_bp
from app.routes.challenge import challenge_bp
from app.routes.movies import movies_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config.Config")

    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(main_bp)
    app.register_blueprint(chat_bp)
    app.register_blueprint(challenge_bp)
    app.register_blueprint(movies_bp)

    return app

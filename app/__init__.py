from flask import Flask
from app.extensions import db, login_manager, bcrypt, migrate
from app.auth.routes import auth_bp
from app.main.routes import main_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config.Config")

    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)

    return app

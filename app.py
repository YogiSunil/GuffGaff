from app.extensions import app, db
from app.main.routes import main_bp
from app.auth.routes import auth_bp

app.register_blueprint(main_bp)
app.register_blueprint(auth_bp)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)

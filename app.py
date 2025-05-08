from app import create_app
from app.extensions import db
from flask.cli import with_appcontext

app = create_app()

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)

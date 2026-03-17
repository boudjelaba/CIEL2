import os
from flask import Flask
from .routes import student_bp
from .models import db

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = (
        f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}"
        f"@postgres_db:5432/{os.getenv('POSTGRES_DB')}"
    )

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    app.register_blueprint(student_bp)

    @app.route("/")
    def home():
        return {"status": "ok", "message": "API Student Running"}

    with app.app_context():
        db.create_all()

    return app
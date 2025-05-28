from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')  # This must match your config.py

    db.init_app(app)
    login_manager.init_app(app)

    from . import models  # Ensure models are imported after db is initialized

    @login_manager.user_loader
    def load_user(user_id):
        return models.User.query.get(int(user_id))

    from .routes import main
    app.register_blueprint(main)

    return app
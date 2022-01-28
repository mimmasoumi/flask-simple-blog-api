from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.secret_key = "1f184d88-fd9f-43bd-b18c-f5832166ad6c"

    db.init_app(app)

    from .views import main
    app.register_blueprint(main)

    return app


# run this commands before start project
# export FLASK_API=.
# export FLASK_DEBUG=1

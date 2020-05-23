import os

from flask import Flask
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()


def create_app(env=None):
    from core import config, error, routes
    from swagger import swagger

    app = Flask(__name__)
    config.init_app(app, env)
    CORS(app)

    db.init_app(app)
    error.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    routes.init_app(app)
    swagger.init_app(app)

    return app

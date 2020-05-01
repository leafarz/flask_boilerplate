import os

from flask import Flask
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()


def create_app(env=None):
    from core import config, routes

    app = Flask(__name__)
    config.init_app(app, env)

    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    routes.init_app(app)

    return app

from decouple import config
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()


def create_app():
    app = Flask(__name__)
    app.config.from_object(f'core.config.{config("BUILD_CONFIG").title()}')

    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)

    from user.routes import user_bp

    app.register_blueprint(user_bp)

    return app

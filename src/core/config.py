import inspect
import os
import sys

from decouple import config

BASEDIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


class Default(object):
    DEBUG = False

    SWAGGER_URL = "/api/docs"
    SWAGGER_PATH = os.path.join(BASEDIR, "swagger/swagger.yml")


class Development(Default):
    DEBUG = True
    CONFIG_NAME = "development"
    SECRET_KEY = config("SECRET_KEY_DEVELOPMENT")

    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(
        BASEDIR, "db-development.sqlite"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Production(Default):
    DEBUG = False
    CONFIG_NAME = "production"
    SECRET_KEY = config("SECRET_KEY_PRODUCTION")

    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(
        BASEDIR, "db-production.sqlite"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False


def get_config(config_name):
    configs_dict = {
        obj.CONFIG_NAME: obj
        for name, obj in inspect.getmembers(sys.modules[__name__])
        if inspect.isclass(obj) and name != "Default"
    }

    if config_name not in configs_dict:
        print(f"Config not found found: [{config_name}]")
        assert False, f"Config not found found: [{config_name}]"

    return configs_dict[config_name]


def init_app(app, config_name):
    cfg = get_config(config_name)
    app.config.from_object(cfg)

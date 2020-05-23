import inspect
import os
import sys

from decouple import config

BASEDIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


class Default(object):
    DEBUG = False


class Dev(Default):
    DEBUG = True
    CONFIG_NAME = "dev"
    SECRET_KEY = config("SECRET_KEY_DEV")

    # DB
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(
        BASEDIR, "database/db-dev.sqlite"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Swagger
    SWAGGER_ENABLE = True
    SWAGGER_URL = ""
    SWAGGER_PATH = os.path.join(BASEDIR, "swagger/swagger.yml")


class Prod(Default):
    DEBUG = False
    CONFIG_NAME = "prod"
    SECRET_KEY = config("SECRET_KEY_PROD")

    # DB
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(
        BASEDIR, "database/db-prod.sqlite"
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

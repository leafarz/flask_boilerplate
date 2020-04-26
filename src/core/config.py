import os

from decouple import config


class Default(object):
    DEBUG = False
    SECRET_KEY = config("SECRET_KEY")


class Dev(Default):
    DEBUG = True

    basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "db.sqlite")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Prod(Default):
    DEBUG = False

    # TODO: change to postgresql
    basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "db.sqlite")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

import os

from flask_migrate import MigrateCommand
from flask_script import Manager

from core import create_app

env = os.getenv("FLASK_ENV") or "development"
app = create_app(env)

manager = Manager(app)
manager.add_command("db", MigrateCommand)

if __name__ == "__main__":
    manager.run()

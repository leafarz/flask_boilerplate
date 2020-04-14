from flask_migrate import MigrateCommand

from core import create_app
from flask_script import Manager

manager = Manager(create_app)
manager.add_command("db", MigrateCommand)

if __name__ == "__main__":
    manager.run()

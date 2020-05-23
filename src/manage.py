import os

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from core import create_app, db

env = os.getenv("FLASK_ENV") or "dev"
app = create_app(env)

migrate = Migrate(app=app, db=db, directory=f'database/migrations_{env}', compare_type=True)
manager = Manager(app)
manager.add_command("db", MigrateCommand)

if __name__ == "__main__":
    manager.run()

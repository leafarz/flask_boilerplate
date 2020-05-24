import os

from core import create_app
from decouple import config

env = config("FLASK_ENV")
app = create_app(env)

if __name__ == "__main__":
    app.run(debug=True)

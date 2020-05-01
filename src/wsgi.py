import os

from core import create_app

env = os.getenv("FLASK_ENV") or "development"
app = create_app(env)

if __name__ == "__main__":
    app.run(debug=True)

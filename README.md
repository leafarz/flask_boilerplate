# Flask-Boilerplate

## Setup
1. In root directory, create an environment variable and activate
    ```
    python -m venv venv
    venv\Scripts\activate
    ```
2. Install packages
    ```
    pip install -r requirements.txt
    ```
3. In `src`, create a `.env` file and add
    ```
    BUILD_CONFIG=Dev        :: OR Prod
    SECRET_KEY=SECRET_KEY
    ```

## Running
1. In `src`, do migrations
    ```
    python manage.py db init
    python manage.py db migrate
    python manage.py db upgrade
    ```
2. Run server
    ```
    python manage.py runserver
    ```

## Todo
1. Not yet ready for Heroku
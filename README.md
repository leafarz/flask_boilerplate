# Flask-Boilerplate
![img](https://github.com/leafarz/resources/blob/master/flask_boilerplate_01.PNG?raw=true)


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
    SECRET_KEY_DEVELOPMENT=SECRET_KEY
    SECRET_KEY_PRODUCTION=SECRET_KEY
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


## Swagger UI
1. Swagger can be run on `/api/docs` endpoint


## Todo
1. Not yet ready for Heroku
# Flask-Boilerplate

Flask boilerplate project with multiple API version support.
![img](https://raw.githubusercontent.com/leafarz/resources/master/flask_boilerplate_02.PNG)

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
   FLASK_ENV=dev       # or prod
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
3. Open http://127.0.0.1:5000/ and it should show the Swagger-UI. This is disabled in `prod` environment.

## Deployment

- Heroku
   1. Create heroku app
   2. Update config with the Postgres URL from Heroku
   3. Initialize, migrate and upgrade the database
   4. Set the environment variables in Heroku
   5. Deploy the app

from flask_swagger_ui import get_swaggerui_blueprint
from yaml import Loader, load


def init_app(app):
    swagger_url = app.config['SWAGGER_URL']
    swagger_path = app.config['SWAGGER_PATH']

    swagger_yml = load(open(swagger_path, "r"), Loader=Loader)

    blueprint = get_swaggerui_blueprint(
        swagger_url, swagger_path, config={"spec": swagger_yml}
    )
    app.register_blueprint(blueprint, url_prefix=swagger_url)

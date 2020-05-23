from flask_swagger_ui import get_swaggerui_blueprint
from yaml import Loader, load


def init_app(app):
    if 'SWAGGER_ENABLE' in app.config and app.config['SWAGGER_ENABLE']:
        swagger_url = app.config['SWAGGER_URL']
        swagger_path = app.config['SWAGGER_PATH']

        swagger_yml = load(open(swagger_path, "r"), Loader=Loader)

        blueprint = get_swaggerui_blueprint(
            base_url=swagger_url,
            api_url=swagger_path,
            config={"spec": swagger_yml}
        )
        app.register_blueprint(blueprint, url_prefix=swagger_url)

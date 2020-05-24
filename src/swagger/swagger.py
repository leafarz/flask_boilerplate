import os

from flask import send_from_directory
from flask_swagger_ui import get_swaggerui_blueprint
from yaml import Loader, load


def init_app(app):
    if "SWAGGER_ENABLE" in app.config and app.config["SWAGGER_ENABLE"]:
        base_url = app.config["SWAGGER_BASE_URL"]
        base_path = app.config["SWAGGER_BASE_PATH"]

        # get all swagger yaml files
        files = [f for f in os.listdir(base_path) if f.endswith("yml")]

        if len(files) == 0:
            print("No files in docs")
            return

        files.sort()

        specs = [f"v{i+1}" for i in range(len(files))]
        urls = [{"name": n, "url": f"{base_url}/{u}"} for n, u in zip(specs, files)]

        filepath = os.path.join(base_path, files[0])
        swagger_yml = load(open(filepath, "r"), Loader=Loader)

        blueprint = get_swaggerui_blueprint(
            base_url=base_url,
            api_url=filepath,
            config={"spec": swagger_yml, "urls": urls, "urls.primaryName": specs[0]},
        )
        app.register_blueprint(blueprint, url_prefix=base_url)

        # dynamically create routes for each yaml files
        basedir = os.path.dirname(os.path.abspath(__file__))
        docsdir = os.path.join(basedir, "docs")
        for spec, file in zip(specs, files):
            app.add_url_rule(
                f"/{file}", spec, lambda file=file: send_from_directory(docsdir, file)
            )

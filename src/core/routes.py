from user.v1.routes import user_v1_bp
from user.v2.routes import user_v1_bp


def init_app(app):
    app.register_blueprint(user_v1_bp, url_prefix="/api/v1")
    app.register_blueprint(user_v1_bp, url_prefix="/api/v2")

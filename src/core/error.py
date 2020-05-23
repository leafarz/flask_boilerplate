from flask import Blueprint, jsonify

error_bp = Blueprint("error_bp", __name__)


@error_bp.app_errorhandler(401)
def unauthorized(e):
    return jsonify(msg=e.description), 401


@error_bp.app_errorhandler(404)
def not_found(e):
    return jsonify(msg=e.description), 404


@error_bp.app_errorhandler(422)
def unprocessable_entity(e):
    return jsonify(msg=e.description), 422


def init_app(app):
    app.register_blueprint(error_bp)

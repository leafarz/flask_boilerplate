import json

from flask import Blueprint, jsonify

from user.views import UserAPI

user_view = UserAPI.as_view("user")

user_bp = Blueprint("user_bp", __name__, template_folder="templates")
user_bp.add_url_rule(
    "/user/", defaults={"id": None}, view_func=user_view, methods=["GET"]
)
user_bp.add_url_rule("/user/<int:id>", view_func=user_view, methods=["GET"])
user_bp.add_url_rule("/user/", view_func=user_view, methods=["POST"])

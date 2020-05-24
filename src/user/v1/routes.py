from flask import Blueprint

from user.v1.views import UserAPI

user_view = UserAPI.as_view("user")

user_v1_bp = Blueprint("user_v1_bp", __name__, template_folder="templates")
user_v1_bp.add_url_rule(
    "/user/", defaults={"id": None}, view_func=user_view, methods=["GET"]
)
user_v1_bp.add_url_rule("/user/<int:id>", view_func=user_view, methods=["GET"])
user_v1_bp.add_url_rule("/user/", view_func=user_view, methods=["POST"])

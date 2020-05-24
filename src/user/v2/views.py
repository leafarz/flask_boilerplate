from flask import abort, jsonify
from flask.views import MethodView
from sqlalchemy.exc import IntegrityError

from common.decorators import parse_request
from common.helpers import copy_attr
from core import db
from user.models import User
from user.serializers import user_create_serializer, user_serializer, users_serializer


class UserAPI(MethodView):
    def get(self, id):
        if id is None:
            users = User.query.all()
            json_result = users_serializer.dump(users)
            return jsonify(json_result), 200
        else:
            user = User.query.filter_by(id=id).first()
            if user is None:
                abort(404, "Account not found")
            json_result = user_serializer.dump(user)
            return json_result, 200

from flask import jsonify, request
from flask.views import MethodView

from common import copy_attr
from core import db
from user.models import User
from user.serializers import user_serializer, users_serializer


class UserAPI(MethodView):
    def get(self, id):
        if id is None:
            users = User.query.all()
            json_result = users_serializer.dump(users)
            return jsonify(json_result), 200
        else:
            user = User.query.filter_by(id=id).first()
            json_result = user_serializer.dump(user)
            return json_result, 200

    def post(self):
        data = request.get_json()
        user = User()
        copy_attr(data, user)

        try:
            db.session.add(user)
            db.session.commit()
        except:
            return {}, 200

        json_result = user_serializer.dump(user)
        return json_result, 200

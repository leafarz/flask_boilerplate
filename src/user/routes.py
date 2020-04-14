import json

from flask import Blueprint, jsonify
from flask.views import MethodView

from core import db
from user.models import User
from user.serializers import user_serializer, users_serializer

user_bp = Blueprint('user_bp', __name__, template_folder='templates')

class UserAPI(MethodView):
   def get(self, id):
      if id is None:
         users = users_serializer.dump(User.query.all())
         return {
            'data': users
         }
      else:
         user = User.query.filter_by(id=id).first()
         return {
            'data': user_serializer.dump(user)
         }

   def post(self):
      user = User(username='user1', email='email1@email.com')
      db.session.add(user)
      db.session.commit()
      return user_serializer.dump(user), 200

user_view = UserAPI.as_view('user')
user_bp.add_url_rule('/user/', defaults={'id': None}, view_func=user_view, methods=['GET'])
user_bp.add_url_rule('/user/<int:id>', view_func=user_view, methods=['GET'])
user_bp.add_url_rule('/user/', view_func=user_view, methods=['POST'])

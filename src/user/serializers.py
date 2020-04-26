from core import ma
from user.models import User


class UserSerializer(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        include_fk = True


user_serializer = UserSerializer()
users_serializer = UserSerializer(many=True)

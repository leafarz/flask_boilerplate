from core import ma
from user.models import User


class UserSerializer(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User


class UserCreateSerializer(ma.SQLAlchemyAutoSchema):
    class Meta:
        fields = (
            "username",
            "email"
        )


user_serializer=UserSerializer()
users_serializer=UserSerializer(many=True)

user_create_serializer=UserCreateSerializer()

from rest_framework.serializers import ModelSerializer
from django.contrib.auth.hashers import make_password

from users.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }

    def create(self, validated_data):
        """Хэширует пароль при создании пользователя."""
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

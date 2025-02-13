from rest_framework.serializers import ModelSerializer
from rest_framework.exceptions import ValidationError

from datetime import date

from posts.models import Post, Comment


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['author', 'created_at', 'updated_at']

    def validate(self, data):
        """Проверка возраста автора (18+)."""
        request = self.context.get('request')
        if not request or not request.user.is_authenticated:
            raise ValidationError("Авторизация обязательна.")
        user = request.user
        age = (date.today() - user.birth_date).days // 365
        if age < 18:
            raise ValidationError('Автор должен быть старше 18 лет.')
        return data


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['author', 'post', 'created_at', 'updated_at']

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

from posts.models import Post, Comment
from posts.serializers import PostSerializer, CommentSerializer
from users.permissions import IsAdminOrOwner


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_permissions(self):
        """Настраивает права доступа для действий с постами."""
        if self.action == 'create':
            self.permission_classes = (IsAuthenticated,)  # Создание для авторизованных
        elif self.action in ['update', 'destroy']:
            self.permission_classes = (IsAdminOrOwner,)  # Редактирование/удаление только автором/админом
        elif self.action in ['retrieve', 'list']:
            self.permission_classes = (AllowAny,)  # Просмотр для всех

        return super().get_permissions()

    def perform_create(self, serializer):
        """Автоматически назначает автора поста."""
        serializer.save(author=self.request.user)


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        """Настраивает права доступа для действий с комментариями."""
        if self.action == 'create':
            self.permission_classes = (IsAuthenticated,)  # Создание для авторизованных
        elif self.action in ['update', 'destroy']:
            self.permission_classes = (IsAdminOrOwner,)  # Редактирование/удаление только автором/админом
        elif self.action in ['retrieve', 'list']:
            self.permission_classes = (AllowAny,)  # Просмотр для всех

        return super().get_permissions()

    def perform_create(self, serializer):
        """Автоматически назначает автора комментария."""
        serializer.save(author=self.request.user)

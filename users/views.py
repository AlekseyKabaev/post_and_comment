from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

from users.models import User
from users.serializers import UserSerializer
from users.permissions import IsAdminOrSelf


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        """Настраивает права доступа для действий с пользователями."""
        if self.action == 'create':
            self.permission_classes = (AllowAny,)  # Регистрация доступна всем
        elif self.action in ['retrieve', 'list']:
            self.permission_classes = (IsAuthenticated,)  # Просмотр для авторизованных
        elif self.action == 'update':
            self.permission_classes = (IsAdminOrSelf,)  # Редактирование для админа/владельца
        elif self.action == 'destroy':
            self.permission_classes = (IsAdminUser,)  # Удаление только для админов
        else:
            self.permission_classes = (IsAdminUser,)  # Запрещаем все остальные действия по умолчанию

        return super().get_permissions()

    def get_queryset(self):
        if self.request.user.is_staff:
            return User.objects.all()
        return User.objects.filter(id=self.request.user.id)

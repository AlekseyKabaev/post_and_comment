from rest_framework import permissions


class IsAdminOrSelf(permissions.BasePermission):
    """Проверяет, является ли пользователь администратором или автором."""

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or obj == request.user:
            return True
        return False


class IsAdminOrOwner(permissions.BasePermission):
    """Проверяет, является ли пользователь администратором или автором."""

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or obj.author == request.user:
            return True
        return False



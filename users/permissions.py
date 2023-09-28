from rest_framework.permissions import BasePermission

from users.models import UserRoles


class IsAdmin(BasePermission):
    """ Класс для определения администратора """
    message = "Вы не являетесь администратором!"

    def has_permission(self, request, view):
        if request.user.role == UserRoles.admin:
            return True
        return False


class IsOwner(BasePermission):
    """ Класс для определения владельца """
    message = 'Вы не являетесь владельцем!'

    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False
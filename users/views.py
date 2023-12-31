
from rest_framework.generics import ListAPIView, UpdateAPIView

from users.models import User
from users.serializers import UserSerializer


# Create your views here.
class UserListView(ListAPIView):
    """Список пользавателей"""
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserUpdateView(UpdateAPIView):
    """Обновление пользавателя"""
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        if self.request.user.is_staff:
            return User.objects.all()
        return User.objects.filter(pk=self.request.user.id)

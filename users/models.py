from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy

NULLABLE = {
    'blank': True,
    'null': True
}
class UserRoles(models.TextChoices):
    admin = 'admin', gettext_lazy('admin')
    owner = 'owner', gettext_lazy('owner')

# Create your models here.
class User(AbstractUser):
    """
     Модель пользователя
     """
    username = None

    email = models.EmailField(unique=True, verbose_name='Почта')
    first_name = models.CharField(max_length=150, verbose_name='Имя', **NULLABLE)
    last_name = models.CharField(max_length=150, verbose_name='Фамилия', **NULLABLE)
    phone = models.CharField(max_length=150, verbose_name='номер телефона', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='Фото', **NULLABLE)
    telegram_username = models.CharField(max_length=100, verbose_name='Телеграм', **NULLABLE)
    role = models.CharField(max_length=20, **NULLABLE, choices=UserRoles.choices)



    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

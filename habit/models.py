from django.db import models

from config import settings
from users.models import NULLABLE

PEREODICITY = [
    ('EVERY DAY', 'раз в день'),
    ('EVERY OTHER DAY', 'через день'),
    ('EVERY WEEK', 'раз в неделю'),
]


# Create your models here.
class Habit(models.Model):
    """
    Базовая модель
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Создатель привычки',
                             **NULLABLE)
    place = models.CharField(max_length=200, verbose_name='Место')
    time = models.TimeField(verbose_name='Время')
    action = models.CharField(max_length=250, unique=True, verbose_name='Действие')
    is_published = models.BooleanField(default=True, verbose_name='Признак публичности привычки')
    duration = models.PositiveIntegerField(default=120, verbose_name='Продолжительность')


class PleasantHabit(Habit):
    """
    Модель приятной привычки
    """

    is_pleasant_habit = models.BooleanField(default=True, verbose_name='Признак приятной привычки')

    class Meta:
        verbose_name = 'Приятная привычка'
        verbose_name_plural = 'Приятные привычки'

    def __str__(self):
        return f'{self.action}, время: {self.time}, место: {self.place}, выполнить за {self.duration} секунд'


class UsefulHabit(Habit):
    """
    Модель полезнай привычки
    """
    pleasant_habit = models.ForeignKey(PleasantHabit, on_delete=models.CASCADE, verbose_name='приятная привычка',
                                       **NULLABLE)
    reward = models.TextField(verbose_name='Вознаграждение', **NULLABLE)
    frequency = models.CharField(max_length=100, default='EVERY DAY', choices=PEREODICITY, verbose_name='Переодичность')

    class Meta:
        verbose_name = 'Полезная привычка'
        verbose_name_plural = 'Полезные привычки'

    def __str__(self):
        return f'{self.action}, время: {self.time}, место: {self.place}, выполнить за {self.duration} ' \
               f' секунд (приятное действие: {self.pleasant_habit if self.pleasant_habit else "-"})'

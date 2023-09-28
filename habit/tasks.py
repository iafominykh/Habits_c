
from telebot import TeleBot

from celery import shared_task
from config.settings import TELEGRAM_TOKEN
from habit.models import Habit



@shared_task
def send_habit_massage(object_pk):
    """ Отправка сообщения"""
    habit = Habit.objects.get(pk=object_pk)
    bot = TeleBot(TELEGRAM_TOKEN)
    message = f'Нужно выполнить {habit.action} в {habit.time} в {habit.place}'
    print(message)
    bot.send_message(habit.user.telegram_username, message)

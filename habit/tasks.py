from datetime import datetime
from telebot import TeleBot
import requests
from celery import shared_task
from config.settings import TELEGRAM_TOKEN
from habit.models import Habit
from users.models import User


# @shared_task
# def send_habit_message():
#     # time_now = datetime.now()
#     # for hab in Habit.objects.all():
#     #     if hab.time.minute == time_now.minute and hab.time.hour == time_now.hour:
#     #         message = f" В {hab.time} нужно выполнить {hab.action} в {hab.place}"
#     #         url_get_updates = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage?&telegram_username=669690493&text={message}"
#     #         response = requests.get(url_get_updates)
#
@shared_task
def send_habit_massage(object_pk):
    habit = Habit.objects.get(pk=object_pk)
    bot = TeleBot(TELEGRAM_TOKEN)
    message = f'Нужно выполнить {habit.action} в {habit.time} в {habit.place}'
    print(message)
    bot.send_message(habit.user.telegram_username, message)

from django.urls import path

from habit.apps import HabitConfig
from habit.views import HabitListAPIView, HabitCreateAPIView, HabitRetrieveAPIView, HabitUpdateAPIView, \
    HabitDestroyAPIView, HabitPublicListAPIView

app_name = HabitConfig.name

urlpatterns = [
    path('habits/', HabitListAPIView.as_view(), name='habit_list'),
    path('habits/create/', HabitCreateAPIView.as_view(), name='habit_create'),
    path('habits/detail/<int:pk>/', HabitRetrieveAPIView.as_view(), name='habit_detail'),
    path('habits/update/<int:pk>/', HabitUpdateAPIView.as_view(), name='habit_update'),
    path('habits/delete/<int:pk>/', HabitDestroyAPIView.as_view(), name='habit_delete'),
    path('habits/public/', HabitPublicListAPIView.as_view(), name='habits_public_list'),
]


from django.contrib import admin

from habit.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'time', 'is_pleasant', 'is_publication')
    list_filter = ('id',)
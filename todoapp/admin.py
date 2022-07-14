from django.contrib import admin
from . models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'todo_item', 'date_created', 'date_to_begin', 'status']
    autocomplete_fields = ['user']
    search_fields = ['email']
    list_per_page = 10
    list_filter = ['date_created', 'date_to_begin']
    ordering = ['-date_created']



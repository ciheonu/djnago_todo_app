from django.contrib import admin
from profiles.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'last_name', 'sex']
    list_per_page = 10
    search_fields = ['email']
    list_filter = ['sex']

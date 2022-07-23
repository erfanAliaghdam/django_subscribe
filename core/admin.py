from django.contrib import admin
from django.contrib.auth import get_user_model
@admin.register(get_user_model())
class UserAdmin(admin.ModelAdmin):
    search_fields = ('username', 'email', 'first_name', 'last_name')
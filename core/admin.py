from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as AdminUser

@admin.register(get_user_model())

class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_staff', 'is_active', 'is_superuser')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)
    add_fieldsets = (
    (None, {
        'classes': ('wide',),
        'fields': ('email', 'first_name', 'last_name', 'password1', 'password2'),
    }),
    )
    
    list_filter = ('is_staff', 'is_superuser', 'is_active',)

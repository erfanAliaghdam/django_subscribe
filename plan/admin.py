from django.contrib import admin
from .models import Plan

@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'description', 'price', 'plan_type', 'is_active')
    list_filter = ('plan_type',)
    search_fields = ('user', 'description', 'price', 'plan_type', 'name',)
    
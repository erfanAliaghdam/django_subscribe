from django.contrib import admin
from .models import Plan

@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'description', 'price', 'plan_type', 'is_active')
    list_filter = ('plan_type',)
    search_fields = ('user', 'description', 'price', 'plan_type', 'name',)
    
    fieldsets = (
        (("title for Plan"), {"fields": ("name",)}),
        (("Plan Type"), {"fields": ("plan_type",)}),
        (("price"), {"fields": ("price",)}),
        (("Plan Details"), {"fields": ("description", "slug", "is_active",)}),
    )

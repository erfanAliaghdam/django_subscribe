from django.contrib import admin
from .models import PlanItem, Subscribe

@admin.register(PlanItem)
class PlanAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'description', 'price', 'is_active')
    search_fields = ('user', 'description', 'price', 'name',)
    list_per_page = 20

    fieldsets = (
        (("title for Plan"), {"fields": ("name",)}),
        (("Plan duration"), {"fields": ("duration",)}),
        (("price"), {"fields": ("price",)}),
        (("Plan Details"), {"fields": ("description", "slug", "is_active",)}),
    )

@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ( 'user', 'plan', 'is_active', 'created_at', 'finish_at')
    list_filter = ('is_active',)
    search_fields = ('user',)
    list_per_page = 20
    autocomplete_fields = ('user', 'plan',)
    fieldsets = (
        (("User "), {"fields": ("user",)}),
        (("Plan "), {"fields": ("plan",)}),
        (("status"), {"fields": ("is_active",)}),
        (("Plan Details"), {"fields": ( "created_at", "finish_at",)}),
        (("Subscription status"), {"fields": ("subscription_check",)})
    )
    readonly_fields = ('created_at', 'finish_at', 'subscription_check')
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('user', 'plan')
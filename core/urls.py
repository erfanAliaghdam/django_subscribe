from .views import activate_user, free_plan
from django.urls import path, include

urlpatterns = [
    path('auth/activate/<str:uid>/<str:token>/', activate_user, name='activate_user_url'),
    path('trial/', free_plan, name='plan-free')
]
from .views import activate_user
from django.urls import path, include

urlpatterns = [
    path('auth/activate/<str:uid>/<str:token>/', activate_user, name='activate_user_url')
]
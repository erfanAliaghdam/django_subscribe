from unicodedata import name
from rest_framework import routers
from .views import PlanViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register('', PlanViewSet, basename='plans')

urlpatterns = [
    path('plans/', include(router.urls))
]



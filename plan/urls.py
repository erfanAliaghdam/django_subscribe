from django.urls import path, include



urlpatterns = [
    path('', include('plan.api.v1.urls'), name='plans'),
]

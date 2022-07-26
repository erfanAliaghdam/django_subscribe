from pytest import mark, fixture
from rest_framework.test import APIClient
from rest_framework import status
from model_bakery import baker
from plan.models import PlanItem
from django.contrib.auth import get_user_model


class TestPlan:
    @fixture
    def conf(self):
        self.client = APIClient()
        self.user = baker.make(get_user_model(), is_active=True)
        self.client.force_authenticate(user = self.user )
        self.plan = baker.make(PlanItem, is_active = True, price=0, duration=30)

        
    @mark.django_db   
    def test_if_user_can_subscribe_to_free_plan(self, conf):
        response = self.client.post(f'/api/plans/{self.plan.id}/subscribe/')
        print(response.data)
        assert response.status_code == status.HTTP_201_CREATED

    @mark.django_db
    def test_if_anonymous_user_can_get_subscribed_plans(self, conf):
        self.client.logout()
        response = self.client.post(f'/api/plans/{self.plan.id}/subscribe/')
        print(response.data)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED   


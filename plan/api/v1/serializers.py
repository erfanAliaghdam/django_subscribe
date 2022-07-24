from plan.models import Plan, Subscribe
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Plan
        fields = ('id', 'name', 'price', 'description', 'is_active')


class SubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Subscribe
        fields = ('id', 'plan', 'user', 'created_at')

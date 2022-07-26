from plan.models import PlanItem, Subscribe
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

class PlanSerializer(serializers.ModelSerializer):
    name = serializers.CharField(read_only=True)
    price = serializers.DecimalField(read_only = True, max_digits=10, decimal_places=2)
    is_active = serializers.BooleanField(read_only=True)
    description = serializers.CharField(read_only=True)
    class Meta:
        model  = PlanItem
        fields = ('id', 'name', 'price', 'description', 'is_active')


class SubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Subscribe
        fields = ('id', 'plan', 'user', 'created_at')

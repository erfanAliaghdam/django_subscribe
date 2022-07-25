from django.db import models
from django.contrib.auth import get_user_model
from django.utils.timezone import now, timedelta
from django.db.utils import IntegrityError
from rest_framework import status, exceptions, serializers
from django.core.exceptions import ValidationError
class Plan(models.Model):
    ONJOIN            = '0'
    ONEMONTH          = '30'
    TREEMONTH         = '90'
    SIXMONTH          = '180'
    PLAN_TYPE = [
        (ONJOIN, 'on Join 30 days free'),
        (ONEMONTH, '1 month'),
        (TREEMONTH, '3 months'),
        (SIXMONTH, '6 months'),
    ]
    description = models.TextField(max_length=500)
    price = models.IntegerField()
    plan_type = models.CharField(max_length=100, choices=PLAN_TYPE)
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=500, unique=True)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.name


class Subscribe(models.Model):
    user       = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='subscription')
    plan       = models.ForeignKey(Plan, on_delete=models.CASCADE)
    is_active  = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    finish_at  = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return (str(self.user.email) + '--> Plan ' + str(self.plan.name))
    
    class Meta:
        unique_together = ('user', 'plan')
        ordering = ['created_at']

    @property
    def subscription_check(self):
        if self.finish_at == None:
            return None
        if self.finish_at > now():
            return True
        elif self.is_active == False:
            return False
        else: return False
    #! this section will save finish date on save new subscription .
    def save(self, *args, **kwargs):
        print(self.plan.plan_type)
        if not self.pk:
            print('XXX')
            self.finish_at = now() + timedelta(days = int(self.plan.plan_type))

        sub_check = [obj for obj in Subscribe.objects.filter(user=self.user).all() if obj.subscription_check == True]
        if len(sub_check) > 0:
            raise ValidationError('You already have an active subscription', status.HTTP_400_BAD_REQUEST)
        print(self.subscription_check)
        super().save(*args, **kwargs)

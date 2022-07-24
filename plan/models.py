from django.db import models
from django.contrib.auth import get_user_model


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
    user       = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    plan       = models.ForeignKey(Plan, on_delete=models.CASCADE)
    is_active  = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    finish_at  = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return (str(self.user.email) + '--> Plan ' + str(self.plan.name))
    
    class Meta:
        unique_together = ('user', 'plan')
        ordering = ['created_at']

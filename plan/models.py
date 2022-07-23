from django.db import models
from django.contrib.auth import get_user_model


class Plan(models.Model):
    ONJOIN            = 'onjoinFree'
    ONPAYMANT         = 'onpaymentFree'
    ONCARD            = 'oncardFree'
    ONREFERRAL        = 'onreferralFree'
    ONREFERRALPAYMENT = 'onreferralpaymentFree'
    ONREFERRALCARD    = 'onreferralcardFree'
    ONREFERRALJOIN    = 'onreferraljoinFree'
    ONEMONTH          = 'onemonth'
    TREEMONTH         = 'treemonth'
    SIXMONTH          = 'sixmonth'
    PLAN_TYPE = [
        ('onJoin free', ONJOIN),
        ('onPayment free',  ONPAYMANT),
        ('onCard free', ONCARD),
        ('onReferralPayment free', ONREFERRALPAYMENT),
        ('onReferralCard free', ONREFERRALCARD),
        ('onReferralJoin free', ONREFERRALJOIN),
        ('1month', ONEMONTH),
        ('3month', TREEMONTH),
        ('6month', SIXMONTH),
    ]
    description = models.TextField(max_length=500)
    price = models.IntegerField()
    plan_type = models.CharField(max_length=100, choices=PLAN_TYPE)
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=500, unique=True)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.name
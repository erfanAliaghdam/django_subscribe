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
        ('on Join free', ONJOIN),
        ('on Payment free',  ONPAYMANT),
        ('on Card free', ONCARD),
        ('on Referral Payment free', ONREFERRALPAYMENT),
        ('on Referral Card free', ONREFERRALCARD),
        ('on Referral Join free', ONREFERRALJOIN),
        ('1 month', ONEMONTH),
        ('3 month', TREEMONTH),
        ('6 month', SIXMONTH),
    ]
    description = models.TextField(max_length=500)
    price = models.IntegerField()
    plan_type = models.CharField(max_length=100, choices=PLAN_TYPE)
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=500, unique=True)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.name
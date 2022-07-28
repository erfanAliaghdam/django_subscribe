from django.db import models
from django.contrib.auth import get_user_model
from rest_framework import status
from django.core.exceptions import ValidationError
from django.utils import timezone


class PlanItem(models.Model):
    description = models.TextField(max_length=500)
    price    = models.IntegerField()
    duration = models.IntegerField()
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=500, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Subscribe(models.Model):
    user       = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='subscription')
    plan       = models.ForeignKey(PlanItem, on_delete=models.CASCADE, related_name = 'subscribes')
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
        if self.finish_at > timezone.now():
            return True
        elif self.is_active == False:
            return False
        else: return False
    #! this section will save finish date on save new subscription .
    def save(self, *args, **kwargs):
        if not self.pk:
            print('XXX')
            planObj = PlanItem.objects.get(pk = self.plan.id)
            print(planObj.duration)
            date = timezone.now()+timezone.timedelta(days=self.plan.duration)
            print(date)
            self.finish_at  = date
            

        sub_check = [obj for obj in Subscribe.objects.filter(user=self.user).all() if obj.subscription_check == True]
        if len(sub_check) > 0:
            raise ValidationError('You already have an active subscription', status.HTTP_400_BAD_REQUEST)
        print(self.subscription_check)
        super().save(*args, **kwargs)

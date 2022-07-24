from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db import transaction
from SmsService.tasks import send_email

@receiver(post_save, sender=get_user_model())
def signal_send_email(sender, **kwargs):
    if kwargs['instance'].is_active:
        with transaction.atomic():
            send_email.delay(kwargs['instance'].email, 'Subscription email content !')
            print('Email was sent')
            print('-------------------------')

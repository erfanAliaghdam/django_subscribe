from celery import shared_task
from django.contrib.auth import get_user_model

@shared_task
def send_email(email, message):
    print('Sending emails... :')
    print(email)
    #! will send  email to user
    print(message)
    print('Emails were successfully sent. ')
    print('-------------------------')
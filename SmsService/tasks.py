from celery import shared_task
from django.core.mail import send_mail as email_sender, EmailMultiAlternatives
from django.urls import reverse
from django.template.loader import render_to_string


@shared_task
def send_email(email, message):
    print('Sending emails... :')
    print(email)
    merge_data = {
        'greetings': "hello"
    }
    html_body = render_to_string("trial_email.html", merge_data)
    message = EmailMultiAlternatives(
       subject='free trial',
       body="het click on this button and get 30 day freee trial.",
       from_email='xyz@abc.com',
       to=['wxyz1@abc.com']
    )
    message.attach_alternative(html_body, "text/html")
    message.send(fail_silently=False)
    print('Emails were successfully sent. ')
    print('-------------------------')

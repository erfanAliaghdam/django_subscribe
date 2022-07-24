from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager as BaseUserManager
from SmsService.tasks import send_email
from django.utils import timezone
from SmsService.tasks import send_email

class UserManager(BaseUserManager):
    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        if not email:
            raise ValueError('user must have email address')
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(
                email=email,
                is_staff=is_staff,
                is_active=True,
                is_superuser=is_superuser,
                last_login=now,
                date_joined=now,
                **extra_fields
                )
        # We check if password has been given
        if password:
            user.set_password(password)
            user.save(using=self._db)
            return user

    #We change following functions signature to allow "No password"
    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        user=self._create_user(email, password, True, True, **extra_fields)
        user.save(using=self._db)
        return user


class User(AbstractUser):

    username = None
    email = models.EmailField(('email address'), unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    objects = UserManager()
    __original_is_active = None
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__original_is_active = self.is_active

    def save(self, *args, **kwargs):
        if self.is_active == True and self.__original_is_active == False:
            print('XXXXXXXXXX')
            from SmsService.tasks import send_email
            send_email.delay(self.email, "trial email")
        super().save(*args, **kwargs)
        self.__original_is_active = self.is_active

    def __str__(self):
        return self.email 

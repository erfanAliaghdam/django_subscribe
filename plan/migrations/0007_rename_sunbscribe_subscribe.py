# Generated by Django 4.0.6 on 2022-07-23 10:44

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('plan', '0006_alter_plan_plan_type_sunbscribe'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Sunbscribe',
            new_name='Subscribe',
        ),
    ]

# Generated by Django 4.0.6 on 2022-07-28 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0002_alter_planitem_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planitem',
            name='duration',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

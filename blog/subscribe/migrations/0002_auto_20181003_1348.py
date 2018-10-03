# Generated by Django 2.1.1 on 2018-10-03 10:48

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscribe',
            name='subscribed_user',
        ),
        migrations.AlterField(
            model_name='subscribe',
            name='subscription',
            field=models.ManyToManyField(null=True, related_name='subscription', to=settings.AUTH_USER_MODEL),
        ),
    ]

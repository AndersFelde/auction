# Generated by Django 3.1.5 on 2021-05-07 09:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0015_notification_read'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='expiration',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 7, 20, 21, 18, 651195)),
        ),
    ]

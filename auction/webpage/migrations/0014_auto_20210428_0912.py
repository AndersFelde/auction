# Generated by Django 3.1.5 on 2021-04-28 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0013_notification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='bid',
            field=models.IntegerField(),
        ),
    ]

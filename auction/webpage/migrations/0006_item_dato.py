# Generated by Django 3.1.5 on 2021-04-25 16:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0005_auto_20210425_1847'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='dato',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

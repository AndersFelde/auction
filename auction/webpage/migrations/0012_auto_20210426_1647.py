# Generated by Django 3.1.5 on 2021-04-26 14:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webpage', '0011_auto_20210426_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='user',
            field=models.ForeignKey(default=11, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
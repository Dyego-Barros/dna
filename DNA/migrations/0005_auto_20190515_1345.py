# Generated by Django 2.2 on 2019-05-15 16:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DNA', '0004_machine_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
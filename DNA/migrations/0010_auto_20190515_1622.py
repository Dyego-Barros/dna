# Generated by Django 2.2 on 2019-05-15 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DNA', '0009_auto_20190515_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='image',
            field=models.FileField(upload_to='image<django.db.models.fields.CharField>'),
        ),
    ]

# Generated by Django 2.2 on 2019-05-15 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DNA', '0012_auto_20190515_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='image',
            field=models.FileField(max_length=900, upload_to='image/machine/%Y%m%d'),
        ),
    ]

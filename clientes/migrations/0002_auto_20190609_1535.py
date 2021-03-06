# Generated by Django 2.2 on 2019-06-09 18:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='city',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='cliente',
            name='clientAddress',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='cliente',
            name='clientCep',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='cliente',
            name='cnpj',
            field=models.CharField(blank=True, max_length=18),
        ),
        migrations.AddField(
            model_name='cliente',
            name='code',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='cliente',
            name='companyName',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='cliente',
            name='country',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='cliente',
            name='mail',
            field=models.EmailField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='cliente',
            name='nameClient',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='cliente',
            name='nameFantasy',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='cliente',
            name='phone',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='cliente',
            name='state',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='cliente',
            name='stateIncentives',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='cliente',
            name='typeIncentives',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cliente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

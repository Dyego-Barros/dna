from django.db import models
from django.contrib.auth.models import User
from DNA_AUTOMATION.settings import BASE_DIR

class Cliente(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, name='cliente')
    code = models.CharField(max_length=300, blank=True)
    nameClient = models.CharField(max_length=300, blank=True)
    companyName = models.CharField(max_length=300, blank=True)
    nameFantasy = models.CharField(max_length=200, blank=True)
    cnpj = models.CharField(max_length=18, blank=True)
    stateIncentives = models.CharField(max_length=100, blank=True)
    typeIncentives = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    clientAddress = models.CharField(max_length=300, blank=True)
    clientCep = models.CharField(max_length=100, blank=True)
    mail = models.EmailField(max_length=100, blank=True)
    phone = models.CharField(max_length=100, blank=True)
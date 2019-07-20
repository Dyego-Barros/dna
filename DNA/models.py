from django.db import models
from django.contrib.auth.models import User
from DNA_AUTOMATION.settings import BASE_DIR

#Função Retorna Primeiro Nome do Usuario
def get_first_name(self):
    return self.first_name
User.add_to_class("__str__", get_first_name)


#Classe modelo do Perfil do Usuario
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    function = models.CharField(max_length=255)
    image = models.FileField(upload_to="image/%Y/%m/%d/")

    def __str__(self):
       return self.function

#Classe Modelo de Cadastro de Máquinas
class Machine(models.Model):
    user =  models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    nameMachine = models.CharField(max_length= 500 , blank=True)
    descriptionMachine = models.TextField(max_length=5000, blank=True)
    calibration = models.TextField(max_length= 5000)
    city = models.CharField(max_length=100)
    factory = models.CharField(max_length=130)
    group = models.CharField(max_length=100)
    subGroup = models.CharField(max_length=100, blank= True)
    sector = models.CharField(max_length=100, blank=True)
    situation = models.CharField(max_length=100, blank=True)
    manoFacture = models.CharField(max_length=100, blank=True)
    identificationTag = models.CharField(max_length=100, blank=True)
    serialNumber = models.CharField(max_length=100)
    numberManofacturing = models.CharField(max_length=100)
    numberInvoice = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    numberPatrimony = models.CharField(max_length=100)
    warranty = models.CharField(max_length=100)
    registrationDate = models.DateField(auto_now=True)
    responsible = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
        

    def __str__(self):
        return str(self.id)


class bdImage(models.Model):
    user =  models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    idmachine = models.ForeignKey(Machine, on_delete=models.CASCADE, null=True)
    image = models.FileField(max_length=900, upload_to="image/machine/%Y-%m-%d")


class Meta:
    ordering = ["id"]











    
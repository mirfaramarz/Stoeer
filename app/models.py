from django.db import models
from django.contrib.auth.models import User
from localflavor.generic.models import IBANField



class BankData(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=200)
    #iban = IBANField()
    iban = models.CharField(max_length=27 , unique=True)

    

    def __str__(self):
        return self.first_name



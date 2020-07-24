from django.db import models

class Registration(models.Model):
    firstname =models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    Email = models.EmailField()
    password = models.CharField(max_length=50)
    phonenumber = models.CharField(max_length=100, default='07')
    ID_number = models.CharField(max_length=75, unique=True)

def __str__(self):
    return self.first_name



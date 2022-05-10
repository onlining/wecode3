from django.db import models

# Create your models here.
class Signup(models.Model):
    name=models.CharField(max_length=45)
    email=models.EmailField(max_length=45)
    password=models.CharField(max_length=45)
    phonenumber=models.IntegerField()
    personal=models.CharField(max_length=45)
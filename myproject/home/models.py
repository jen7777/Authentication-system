from django.db import models

# Create your models here.
class signup(models.Model):
    firstname=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255)
    email=models.EmailField()
    password1=models.CharField(max_length=255)
    password2=models.CharField(max_length=255)
    
    
from django.db import models

# Create your models here.
class Login(models.Model):
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    def __str__(self) -> str:
        return self.email
class Register(models.Model):
    username=models.CharField(max_length=500)
    email=models.EmailField()
    create_password=models.CharField(max_length=500)
    conform_password=models.CharField(max_length=500)
    conformpassword=models.CharField(max_length=500)
    def __str__(self)->str:
        return self.username
class ContactForm(models.Model):
    Firstname=models.CharField(max_length=100)
    Lastname=models.CharField(max_length=100)
    Email=models.EmailField()
    Address=models.CharField(max_length=500)
    Message=models.TextField()
    def __str__(self) -> str:
        return self.Firstname

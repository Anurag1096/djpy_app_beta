from django.db import models

# Create your models here.

class Book(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    published_date=models.DateField()
    
    def __str__(self) -> str:
        return self.title
    

class Login(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=15)
    
    def __str__(self) -> str:
        return self.username
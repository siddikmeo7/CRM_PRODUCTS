from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=50) 
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(null=True)
    email = models.EmailField(max_length=254)
    date = models.DateField(auto_now_add=True)
    
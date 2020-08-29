from django.db import models

# Create your models here.


class Person(models.Model):
    """Person model representation"""

    last_name = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    birth_day = models.DateTimeField()
    phone = models.IntegerField()
    mobile = models.IntegerField()
    email = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    address = models.CharField(max_length=254)
    address_number = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

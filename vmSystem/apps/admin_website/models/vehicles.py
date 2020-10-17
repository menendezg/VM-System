from django.db import models
from .companies import Companies


class Vehicles(models.Model):
    """
    Vehicles model class reprensentation.
    """

    company = models.OneToOneField(Companies, on_delete=models.CASCADE)
    brand = models.CharField(max_length=128)
    model = models.CharField(max_length=128)
    color = models.CharField(max_length=64)
    color_code = models.CharField(max_length=64)
    fuel = models.CharField(max_length=32)
    kilometers = models.IntegerField()
    detail = models.CharField(max_length=254)
    state = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = "admin_website"

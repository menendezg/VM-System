# Django
from django.db import models

# Models
from vmSystem.apps.companies.models import Companies


class Providers(models.Model):
    """
    Providers model representation.
    """
    company = models.OneToOneField(Companies, on_delete=models.CASCADE)
    category = models.CharField(max_length=64)
    subcategory = models.CharField(max_length=64)
    debt_to_pay = models.DecimalField(max_digits=11, decimal_places=2)

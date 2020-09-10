# Django
from django.db import models
from vmSystem.apps.entities.models.provinces import Provinces


class Cities(models.Model):
    """
    Cities model representation.
    """

    province = models.ForeignKey(Provinces, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)

    class Meta:
        app_label = 'entities'

from django.db import models


class Provinces(models.Model):
    """
    Provinces model representation.
    """

    name = models.CharField(max_length=128)

    class Meta:
        app_label = 'admin_website'

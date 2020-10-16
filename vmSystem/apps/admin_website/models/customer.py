from django.db import models

from .person import Person


class Customer(models.Model):
    """customer model representation"""

    business_name = models.CharField(max_length=128)
    cuix = models.CharField(max_length=255, default='')
    status = models.BooleanField(default='True')
    last_name = models.CharField(max_length=64)
    person_id = models.OneToOneField(Person, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.business_name

    class Meta:
        app_label = "admin_website"

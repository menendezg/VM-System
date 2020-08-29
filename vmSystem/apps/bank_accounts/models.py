from django.db import models

# Create your models here.


class BankAccounts(models.Model):
    """
    BankAccounts class representation.
    """

    cbu = models.IntegerField()
    bank = models.CharField(max_length=128)

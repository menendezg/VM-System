from django.db import models
from vmSystem.apps.persons.models import Person
from vmSystem.apps.bank_accounts.models import BankAccounts

# Create your models here.


class Employee(models.Model):
    """
    Employee class representation.
    """

    cuil = models.IntegerField()
    position = models.CharField(max_length=128)
    admission_date = models.DateTimeField(auto_now_add=True)
    departure_date = models.DateTimeField()
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    bank_account = models.OneToOneField(BankAccounts, on_delete=models.CASCADE)

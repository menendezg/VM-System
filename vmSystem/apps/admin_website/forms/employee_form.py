"""User forms."""

# Django
from django import forms

# Models
from vmSystem.apps.admin_website.models.employee import Employee
from vmSystem.apps.admin_website.models.person import Person
from vmSystem.apps.admin_website.models.provinces import Provinces
from vmSystem.apps.admin_website.models.bank_accounts import BankAccounts
from vmSystem.apps.admin_website.models.cities import Cities


class CustomDateInput(forms.DateInput):
    input_type = "date"


class EmployeeForm(forms.Form):
    """Sign up form."""

    dni = forms.CharField(min_length=4, max_length=128)
    name = forms.CharField(min_length=4, max_length=64)
    last_name = forms.CharField(min_length=4, max_length=64)
    birthdate = forms.DateField(widget=CustomDateInput())
    homephone = forms.IntegerField()
    mobilephone = forms.IntegerField()
    email = forms.CharField(min_length=6, max_length=128, widget=forms.EmailInput())
    province = forms.ModelChoiceField(
        queryset=Provinces.objects.all(), empty_label=None
    )
    city = forms.ModelChoiceField(queryset=Cities.objects.all(), empty_label=None)
    address = forms.CharField(min_length=4, max_length=254)
    address_number = forms.IntegerField()
    cuil = forms.CharField(min_length=4, max_length=255)
    position = forms.CharField(max_length=128)
    admission_date = forms.DateField(widget=CustomDateInput())
    person = forms.ModelChoiceField(queryset=Person.objects.all(), empty_label=None)
    bank_account = forms.ModelChoiceField(
        queryset=BankAccounts.objects.all(), empty_label=None
    )
    cbu = 255

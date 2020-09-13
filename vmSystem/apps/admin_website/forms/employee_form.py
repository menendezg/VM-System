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
    birth_day = forms.DateField(widget=CustomDateInput())
    phone = forms.IntegerField()
    mobile = forms.IntegerField()
    email = forms.CharField(min_length=6, max_length=128, widget=forms.EmailInput())
    # province = forms.ModelChoiceField(
    #    queryset=Provinces.objects.all(), empty_label=None
    # )
    city = forms.ModelChoiceField(queryset=Cities.objects.all(), empty_label=None)
    address = forms.CharField(min_length=4, max_length=254)
    address_number = forms.IntegerField()
    cuil = forms.CharField(min_length=4, max_length=255)
    position = forms.CharField(max_length=128)
    bank_account = forms.ModelChoiceField(
        queryset=BankAccounts.objects.all(), empty_label=None
    )
    cbu = 255

    def save(self):
        """Create employee and person"""
        data = {
            "dni": self.cleaned_data["dni"],
            "name": self.cleaned_data["name"],
            "last_name": self.cleaned_data["last_name"],
            "birth_day": self.cleaned_data["birth_day"],
            "phone": self.cleaned_data["phone"],
            "mobile": self.cleaned_data["mobile"],
            "email": self.cleaned_data["email"],
            "city": self.cleaned_data["city"],
            "address": self.cleaned_data["address"],
            "address_number": self.cleaned_data["address_number"],
        }
        person = Person(**data)
        person.save()
        profile = Employee(
            cuil=self.cleaned_data["cuil"],
            position=self.cleaned_data["position"],
            person=person,
            bank_account=self.cleaned_data["bank_account"],
        )
        profile.save()

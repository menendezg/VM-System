"""Companies forms."""

# Django
from django import forms


class CompanyForm(forms.Form):
    """Profile form."""

    city_name = forms.CharField(max_length=128, required=True)
    bank_account_cbu = forms.CharField(max_length=255, required=True)
    bank_account_name = forms.CharField(max_length=128, required=True)
    cuit = forms.CharField(max_length=11, required=True)
    business_name = forms.CharField(max_length=128, required=True)
    contact_person = forms.CharField(max_length=128, required=False)
    phone = forms.CharField(max_length=20, required=False)
    mobile = forms.CharField(max_length=20, required=False)
    address = forms.CharField(max_length=254, required=True)
    address_number = forms.IntegerField(required=True)
    email = forms.CharField(max_length=200, required=False)
    website = forms.URLField(max_length=200, required=False)
    details = forms.CharField(max_length=255, required=False)
    state = forms.CharField(max_length=64, required=True)

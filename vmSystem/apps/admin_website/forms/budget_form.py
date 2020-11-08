from django import forms
from vmSystem.apps.admin_website.models.vehicle_owner import VehicleOwner


class BudgetForm(forms.Form):
    """Budget form."""
    owner = forms.ModelChoiceField(queryset=VehicleOwner.objects.all(),
                                   empty_label=None)
    state = forms.CharField(max_length=64)
    detail = forms.CharField(max_length=64)
    real_cost = forms.ImageField()
    estimated_cost = forms.ImageField()

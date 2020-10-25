"""
check how we can re use the forms to combine forms.
friendly reminer. When im using a formset factory, is making an array
of forms. thats why we are getting the data with an self.cleaned_data[0]
"""

from django import forms
from django.forms import BaseFormSet, formset_factory
from vmSystem.apps.admin_website.forms.employee_form import EmployeeForm
from vmSystem.apps.admin_website.models.person import Person
from vmSystem.apps.admin_website.models.bank_accounts import BankAccounts
from vmSystem.apps.admin_website.models.employee import Employee
from vmSystem.apps.admin_website.models.customer import Customer


class CustomerForm(BaseFormSet):

    def add_fields(self, form, index):
        super().add_fields(form, index)
        form.fields["cuix"] = forms.CharField(min_length=22, max_length=22)
        form.fields["business_name"] = forms.CharField(min_length=22, max_length=22)

    def save(self):
        """Create employee and person"""
        data = {
            "dni": self.cleaned_data[0]["dni"],
            "name": self.cleaned_data[0]["name"],
            "last_name": self.cleaned_data[0]["last_name"],
            "birth_day": self.cleaned_data[0]["birth_day"],
            "phone": self.cleaned_data[0]["phone"],
            "mobile": self.cleaned_data[0]["mobile"],
            "email": self.cleaned_data[0]["email"],
            "city": self.cleaned_data[0]["city"],
            "address": self.cleaned_data[0]["address"],
            "address_number": self.cleaned_data[0]["address_number"],
        }
        person = Person(**data)
        person.save()

        # then, we create the bank account
        data = {
            "cbu": self.cleaned_data[0]["cbu"],
            "bank": self.cleaned_data[0]["bank"],
        }
        bank_account = BankAccounts(**data)
        bank_account.save()
        customer = Customer(
            business_name=self.cleaned_data[0]["business_name"],
            cuix=self.cleaned_data[0]["cuix"],
            last_name="last_name",
            person=person,
        )
        customer.save()

    def update(self, data):
        import pdb;
        pdb.set_trace()
        person = Person.objects.get(dni=data["dni"])
        person.update_attributes(data=data)
        person.save()
        customer = Customer.objects.get(cuix=data["cuix"])
        customer.update_atrributes(data=data, person_object=person)
        customer.save()


CustomerFormSet = formset_factory(EmployeeForm, formset=CustomerForm)

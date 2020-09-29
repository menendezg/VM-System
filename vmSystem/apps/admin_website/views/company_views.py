# Django
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import (
    View,
    ListView,
)

# Models
from vmSystem.apps.admin_website.models.bank_accounts import BankAccounts
from vmSystem.apps.admin_website.models.cities import Cities
from vmSystem.apps.admin_website.models.companies import Companies

# Forms
from vmSystem.apps.admin_website.forms.companies_form import (
    CompanyForm,
    CreateCompanyForm,
)


class ListCompaniesView(ListView):
    """
    Return all providers created.
    """

    template_name = 'companies/index.html'
    model = Companies
    paginate_by = 30
    context_object_name = 'companies'

    def get_queryset(self):
        """Return only companies without providers."""
        queryset = Companies.objects.filter(company_type='Aseguradora').order_by('id')
        return queryset

    def get_context_data(self, **kwargs):
        """Add another object to context."""
        context = super().get_context_data(**kwargs)
        active_companies = Companies.objects.filter(state='Activa')
        total_companies = Companies.objects.filter(company_type='Aseguradora')
        active_percent = int((len(active_companies) * 100) / len(total_companies))
        context['active_percent'] = active_percent
        return context


class EditCompanyView(View):
    """Edit company view."""

    def get(self, request, *args, **kwargs):
        form = CompanyForm()
        company = Companies.objects.get(id=kwargs['id'])

        return render(
            request=request,
            template_name='companies/edit.html',
            context={
                'companies': company,
                'form': form
            }
        )

    def post(self, request, *args, **kwargs):
        company = Companies.objects.get(id=kwargs['id'])
        form = CompanyForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            # Bank Account
            bank_acc = BankAccounts.objects.get(cbu=company.bank_account.cbu)
            bank_acc.cbu = data['bank_account_cbu']
            bank_acc.bank = data['bank_account_name']
            bank_acc.save()

            # City
            new_city = Cities.objects.get(name=data['city_name'])

            # Entire Company object
            company.city = new_city
            company.cuit = data['cuit']
            company.business_name = data['business_name']
            company.contact_person = data['contact_person']
            company.phone = data['phone']
            company.mobile = data['mobile']
            company.address = data['address']
            company.address_number = data['address_number']
            company.email = data['email']
            company.website = data['website']
            company.details = data['details']
            company.state = data['state']
            company.save()

            return redirect('companies_list')
        else:
            return render(
                request=request,
                template_name='companies/edit.html',
                context={
                    'companies': company,
                    'form': form
                }
            )


class CreateCompanyView(View):
    """
    Class to handler Create view.
    """

    def get(self, request, *args, **kwargs):
        form = CreateCompanyForm()

        return render(
            request=request,
            template_name='companies/create.html',
            context={
                'form': form
            }
        )

    def post(self, request, *args, **kwargs):
        form = CreateCompanyForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('companies_list')

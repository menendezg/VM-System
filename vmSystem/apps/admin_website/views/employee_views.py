from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.views.generic import View, FormView, UpdateView
from vmSystem.apps.admin_website.models.employee import Employee
from django.urls import reverse_lazy

# Forms
from vmSystem.apps.admin_website.forms.employee_form import EmployeeForm


class EmployeePage(View):
    """
    class to handler index view.
    return: index view with the list of employees
    """

    template_name = "employees/index.html"

    def get(self, request, *args, **kwargs):
        employees = Employee.objects.all()
        return render(request, self.template_name, {"employees": employees})


class EmployeeCreate(FormView):
    """
    Class to handler Create view.
    return: Create the user, and is succesful return to main employee page
    """

    template_name = "employees/create_employee.html"
    form_class = EmployeeForm
    success_url = reverse_lazy("employees_list")

    def form_valid(self, form):
        """Save form data."""
        form.save()
        return super().form_valid(form)


class EmployeeDelete(View):
    """
    Class to handler delete user
    return: Delete the user, and is succesful return the main employee page
    """

    template_name = "employees/index.html"

    # TODO: create logic to delete the selected item
    def get(self, request, *args, **kwargs):
        employees = Employee.objects.all()
        return render(request, self.template_name, {"employees": employees})


class EmployeeDetailView(View):
    """
    class to handler detail view
    return: the resource uri requested
    """

    template_name = "employees/detail.html"

    def get(self, request, *args, **kwargs):
        form = EmployeeForm
        queryset = Employee.objects.get(cuil=kwargs["cuil"])

        return render(
            request=request,
            template_name=self.template_name,
            context={"employees": queryset, "form": form},
        )

    def post(self, request, *args, **kwargs):
        pass
        # TO BE CREATED
        # company = Companies.objects.get(id=kwargs['id'])
        # form = CompanyForm(request.POST)
        #
        # if form.is_valid():
        #     data = form.cleaned_data
        #
        #     # Bank Account
        #     bank_acc = BankAccounts.objects.get(cbu=company.bank_account.cbu)
        #     bank_acc.cbu = data['bank_account_cbu']
        #     bank_acc.bank = data['bank_account_name']
        #     bank_acc.save()
        #
        #     # City
        #     new_city = Cities.objects.get(name=data['city_name'])
        #
        #     # Entire Company object
        #     company.city = new_city
        #     company.cuit = data['cuit']
        #     company.business_name = data['business_name']
        #     company.contact_person = data['contact_person']
        #     company.phone = data['phone']
        #     company.mobile = data['mobile']
        #     company.address = data['address']
        #     company.address_number = data['address_number']
        #     company.email = data['email']
        #     company.website = data['website']
        #     company.details = data['details']
        #     company.state = data['state']
        #     company.save()
        #
        #     return redirect('companies_list')
        # else:
        #     return render(
        #         request=request,
        #         template_name='companies/edit.html',
        #         context={
        #             'companies': company,
        #             'form': form
        #         }
        #     )

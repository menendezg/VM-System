from django.shortcuts import render
from django.views.generic import View, FormView, DetailView
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


class EmployeeDetailView(DetailView):
    """
    class to handler detail view
    return: the resource uri requested
    """

    template_name = "employees/detail.html"
    slug_field = "cuil"
    slug_url_kwarg = "cuil"
    queryset = Employee.objects.all()

from django.shortcuts import render
from django.views.generic import View, FormView
from vmSystem.apps.admin_website.models.employee import Employee
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

# Forms
from vmSystem.apps.admin_website.forms.employee_form import EmployeeForm


class EmployeePage(View):
    """
    class home page repr.
    """

    form_class = EmployeeForm
    # initial = {"key": "value"}
    template_name = "employees/index.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        employees = Employee.objects.all()
        # contex_object = "employee"
        return render(
            request, self.template_name, {"employees": employees, "form": form}
        )

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        print(request.POST)
        print(form)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect("/success/")

        employees = Employee.objects.all()
        return render(
            request, self.template_name, {"employees": employees, "form": form}
        )


class EmployeeCreate(FormView):
    template_name = "employees/create_employee.html"
    form_class = EmployeeForm
    success_url = reverse_lazy("employees_list")

    def form_valid(self, form):
        """Save form data."""
        form.save()
        return super().form_valid(form)

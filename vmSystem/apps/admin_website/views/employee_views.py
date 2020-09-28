from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, redirect
from django.views.generic import View, FormView
from vmSystem.apps.admin_website.models.employee import Employee
from vmSystem.apps.admin_website.models.cities import Cities
from vmSystem.apps.admin_website.views.serializers.employee_serializer import \
    EmployeeSerializer
from django.urls import reverse_lazy

# Forms
from vmSystem.apps.admin_website.forms.employee_form import EmployeeForm
import sys


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
        cities = Cities.objects.all()

        return render(
            request=request,
            template_name=self.template_name,
            context={"employees": queryset, "form": form, "cities": cities},
        )

    def post(self, request, *args, **kwargs):
        form = EmployeeForm(request.POST, context="update", identity_key=kwargs["cuil"])
        if form.is_valid():
            data = form.cleaned_data
            employee_serializer = EmployeeSerializer(data, kwargs["cuil"])
            try:
                employee_serializer.employee_update()
            except:
                print("Unexpected error:", sys.exc_info()[0])
                # Warning lazy except
                # TODO: make a nice try and except
                pass
            return redirect("employees_list")
        else:
            return render(
                request=request,
                template_name="employees/detail.html",
                context={"employee": Employee, "form": form},
            )

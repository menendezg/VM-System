from django.shortcuts import render
from django.views.generic import View
from vmSystem.apps.employees.models import Employee


# Create your views here.


class EmployeePage(View):
    """
    class home page repr.
    """

    def get(self, request, *args, **kwargs):
        template_name = "employees/index.html"
        employees = Employee.objects.all()
        # contex_object = "employee"
        return render(request, template_name, {'employees': employees})

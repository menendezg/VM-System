from django.shortcuts import render
from django.views.generic import View
from vmSystem.apps.admin_website.models.employee import Employee


class EmployeePage(View):
    """
    class home page repr.
    """

    def get(self, request, *args, **kwargs):
        template_name = "employees/index.html"
        employees = Employee.objects.all()
        # contex_object = "employee"
        return render(request, template_name, {'employees': employees})

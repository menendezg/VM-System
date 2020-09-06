from django.shortcuts import render
from django.views.generic import View

# Create your views here.


class EmployeePage(View):
    """
    class home page repr.
    """

    def get(self, request, *args, **kwargs):
        template_name = "employees/index.html"
        # contex_object = "employee"
        return render(request, template_name)

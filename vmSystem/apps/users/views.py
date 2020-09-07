from django.shortcuts import render
from django.views.generic import View

# Create your views here.


class LoginHome(View):
    """
    Login Home page view
    """

    def get(self, request, *args, **kwargs):
        template_name = "login.html"
        return render(request, template_name)

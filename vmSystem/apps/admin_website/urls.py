# Django
from django.urls import path

# Views
from vmSystem.apps.admin_website.views.company_views import ListCompaniesView
from vmSystem.apps.admin_website.views.employee_views import (
    EmployeePage,
    EmployeeCreate,
)
from vmSystem.apps.admin_website.views.provider_views import ListProvidersView

urlpatterns = [
    path("companies", ListCompaniesView.as_view(), name="companies_list"),
    path("", EmployeePage.as_view(), name="employees_list"),
    path("employees/create/", EmployeeCreate.as_view(), name="employees_create"),
    path("providers", ListProvidersView.as_view(), name="providers_list"),
]

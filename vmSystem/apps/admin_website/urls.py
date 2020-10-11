# Django
# Views
from vmSystem.apps.admin_website.views.company_views import (
    EditCompanyView, ListCompaniesView,
)
from vmSystem.apps.admin_website.views.employee_views import (
    EmployeeCreate, EmployeeDelete, EmployeeDetailView, EmployeePage,
)
from vmSystem.apps.admin_website.views.provider_views import ListProvidersView

from django.urls import path

urlpatterns = [
    path("companies", ListCompaniesView.as_view(), name="companies_list"),
    path("company/<int:id>/edit", EditCompanyView.as_view(), name="company_edit"),
    path("", EmployeePage.as_view(), name="employees_list"),
    path("employees/create/", EmployeeCreate.as_view(), name="employees_create"),
    path("employees/<pk>/delete/", EmployeeDelete.as_view(), name="employees_delete"),
    path(
        "employees/<str:cuil>/",
        EmployeeDetailView.as_view(),
        name="employees_detail",
    ),
    path("providers", ListProvidersView.as_view(), name="providers_list"),
]

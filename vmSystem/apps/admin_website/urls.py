# Django
from django.urls import path

# Views
from vmSystem.apps.admin_website.views.company_views import ListCompaniesView, EditCompanyView
from vmSystem.apps.admin_website.views.employee_views import EmployeePage
from vmSystem.apps.admin_website.views.provider_views import ListProvidersView

urlpatterns = [
    path('companies', ListCompaniesView.as_view(), name='companies_list'),
    path('company/<int:id>/edit', EditCompanyView.as_view(), name='company_edit'),
    path("", EmployeePage.as_view(), name="employees_list"),
    path('providers', ListProvidersView.as_view(), name='providers_list'),
]

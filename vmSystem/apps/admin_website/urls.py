# Django
# Views

from vmSystem.apps.admin_website.views.company_views import (
    EditCompanyView,
    ListCompaniesView,
)

from vmSystem.apps.admin_website.views.vehicle_views import (
    VehicleView,
    VehicleDelete,
    VehicleCreateView,
    VehicleDetailView,
)

from vmSystem.apps.admin_website.views.customers_views import (
    CustomerView,
    CustomerDetailView,
    CustomerDelete,
    CustomerCreate,
)
from vmSystem.apps.admin_website.views.employee_views import (
    EmployeeCreate,
    EmployeeDelete,
    EmployeeDetailView,
    EmployeePage,
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
    path("customers/", CustomerView.as_view(), name="customer_list"),
    path("customers/create/", CustomerCreate.as_view(), name="customer_create"),
    path("customers/<int:id>/edit", CustomerDetailView.as_view(), name="customer_edit"),
    path("customers/<pk>/delete/", CustomerDelete.as_view(), name="customer_delete"),
    path("vehicles/", VehicleView.as_view(), name="vehicles_list"),
    path("vehicles/create/", VehicleCreateView.as_view(), name="vehicles"
                                                               "_create"),
    path("vehicles/<int:id>/edit/", VehicleDetailView.as_view(),
         name="vehicle_edit"),
    path("vehicles/<pk>/delete/", VehicleDelete.as_view(), name="vehicles_delete"),
    path("providers", ListProvidersView.as_view(), name="providers_list"),
]

from django.urls import path
from .views import EmployeePage

urlpatterns = [
    path("", EmployeePage.as_view(), name="employee"),
]

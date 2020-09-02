from django.urls import path
from .views import LoginHome

urlpatterns = [
    path("", LoginHome.as_view(), name="login"),
]

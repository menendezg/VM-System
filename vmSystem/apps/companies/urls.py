# Django
from django.urls import path

# Views
from .views import ListCompaniesView


urlpatterns = [
    path(
        route='',
        view=ListCompaniesView.as_view(),
        name='list'
    ),
]

# Django
from django.urls import path

# Views
from .views import ListProvidersView


urlpatterns = [
    path(
        route='',
        view=ListProvidersView.as_view(),
        name='list'
    ),
]

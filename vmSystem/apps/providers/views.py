# Django
from django.views.generic import ListView

# Models
from .models import Providers


class ListProvidersView(ListView):
    """
    Return all providers created.
    """

    template_name = 'providers/index.html'
    model = Providers
    paginate_by = 30
    context_object_name = 'providers'

# Django
from django.views.generic import ListView

# Models
from .models import Companies


class ListCompaniesView(ListView):
    """
    Return all providers created.
    """

    template_name = 'companies/index.html'
    model = Companies
    paginate_by = 30
    context_object_name = 'companies'

    def get_queryset(self):
        """Return only companies without providers."""
        queryset = Companies.objects.filter(company_type='Aseguradora')
        return queryset

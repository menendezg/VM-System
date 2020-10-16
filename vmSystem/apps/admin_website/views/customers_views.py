from django.views.generic import DeleteView, FormView, View, ListView
from vmSystem.apps.admin_website.models.customer import Customer
from django.urls import reverse_lazy
from vmSystem.apps.admin_website.forms.customer_form import CustomerFormSet


class CustomerView(ListView):
    """
    class to handler the index view
    return: index view with the list of employees
    """

    template_name = "customers/index.html"
    model = Customer
    paginate_by = 30
    context_object_name = "customers"

    def get_queryset(self):
        """Return only companies without providers."""
        queryset = Customer.objects.all()
        return queryset


class CustomerCreate(FormView):
    """
    Class to handle crate view
    return: create the user. if success, return to main client view
    """

    template_name = "customers/create_customer.html"
    form_class = CustomerFormSet
    success_url = reverse_lazy("customer_list")

    def form_valid(self, form):
        """Save form data."""
        form.save()
        return super().form_valid(form)


class CustomerDelete(DeleteView):
    """
    Class to handle delete view
    return: if success return to main view
    """

    model = Customer

    # required by the clased delete view
    template_name = "customers/customer_confirm_delete.html"
    success_url = reverse_lazy("customer_list")


class CustomerDetailView(View):
    """
    class to handler detail view
    return: the resource uri requested
    """

    pass

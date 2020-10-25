from django.views.generic import DeleteView, FormView, View, ListView
from vmSystem.apps.admin_website.models.customer import Customer
from vmSystem.apps.admin_website.models.cities import Cities
from django.urls import reverse_lazy
from vmSystem.apps.admin_website.forms.customer_form import CustomerFormSet
from django.shortcuts import render, redirect, get_object_or_404


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
        """Return all customers queryset"""
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
    template_name = "customers/detail.html"

    def get(self, request, *args, **kwargs):
        form = CustomerFormSet
        queryset = Customer.objects.get(id=kwargs["id"])
        cities = Cities.objects.all()

        return render(
            request=request,
            template_name=self.template_name,

            context={
                "customer": queryset,
                "form": form,
                "cities": cities,
            }
        )

    def post(self, request, *args, **kwargs):
        data = self._serialize_data(request)
        import pdb;
        pdb.set_trace()
        form = CustomerFormSet(request.POST)
        if form.is_valid():
            form.update(data)
            return redirect("vehicles_list")
        else:
            return render(
                request=request,
                template_name=self.template_name,
                context={"customer": Customer, "form": form},
            )

    def _serialize_data(self, request):
        data = {
            "cuix": request.POST["cuix"],
            "business_name": request.POST["business_name"],
            "dni": request.POST["dni"],
            "name": request.POST["name"],
            "last_name": request.POST["last_name"],
            "birth_day": request.POST["birth_day"],
            "phone": request.POST["phone"],
            "mobile": request.POST["mobile"],
            "email": request.POST["email"],
            "city": request.POST["city"],
            "address": request.POST["address"],
            "address_number": request.POST["address_number"],
        }
        return data

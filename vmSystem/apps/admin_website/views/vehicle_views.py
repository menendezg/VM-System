from django.views.generic import DeleteView, FormView, View, ListView
from vmSystem.apps.admin_website.models.vehicles import Vehicles
from django.urls import reverse_lazy


class VehicleView(ListView):
    """
    class to handler the index view
    return: index view with the list of vehicles
    """

    template_name = "vehicles/index.html"
    model = Vehicles
    paginate_by = 30
    context_object_name = "vehicles"

    def get_queryset(self):
        """return all vehicles queryset"""
        queryset = Vehicles.objects.all()
        return queryset


class VehicleDetailView(FormView):
    pass


class VehicleDelete(DeleteView):
    """
    class to delete register
    return a view to accept delete the record
    """

    model = Vehicles

    template_name = "vehicles/vehicle_delete_confirm_delete.html"
    success_url = reverse_lazy("vehicles_list")

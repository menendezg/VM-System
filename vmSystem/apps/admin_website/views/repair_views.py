from django.views.generic import DeleteView, FormView, ListView
from django.views.generic.edit import UpdateView
from vmSystem.apps.admin_website.models.repair import Repair
from django.urls import reverse_lazy
from vmSystem.apps.admin_website.forms.repair_form import RepairForm


class RepairList(ListView):
    """
    class to handler the index view
    return: index view with the list of repairs
    """
    template_name = "repairs/index.html"
    models = Repair
    paginate_by = 30
    context_object_name = "repairs"

    def get_queryset(self):
        """return all repairs."""
        queryset = Repair.objects.all()
        return queryset


class RepairUpdateView(UpdateView):
    pass


class RepairDetailView():
    pass


class RepairCreateView(FormView):
    """
    class to handler a create view
    return: create the repair object. is success return to main repair page.
    """
    template_name = "repairs/create.html"
    form_class = RepairForm
    success_url = reverse_lazy("repair_list")

    def form_valid(self, form):
        """save form data."""
        form.save()
        return super().form_valid(form)


class RepairDeleteView(DeleteView):
    """
    class to delete register
    return: a view to accept delete record.
    """

    model = Repair

    template_name = "repairs/repairs_delete_confirm_delete.html"
    success_url = reverse_lazy("repair_list")

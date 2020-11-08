from django.views.generic import FormView, ListView
from vmSystem.apps.admin_website.models.budgets import Budget
from django.urls import reverse_lazy
from vmSystem.apps.admin_website.forms.budget_form import BudgetForm


class BudgetList(ListView):
    """
    class to handler the index view
    return: index view with te list of the budgets
    """
    template_name = "budgets/index.html"
    models = Budget
    paginate_by = 30
    context_object_name = "budgets"

    def get_queryset(self):
        """return all budgets"""
        queryset = Budget.objects.all()
        return queryset


class BudgetCreateView(FormView):
    """
    class to handler a create view
    return: create the budget. is success return to main budget page
    """
    template_name = "budgets/create_budget.html"
    form_class = BudgetForm
    success_url = reverse_lazy("budget_list")

    def form_valid(self, form):
        """save form data."""
        form.save()
        return super().form_valid(form)

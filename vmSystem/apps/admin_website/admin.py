from django.contrib import admin
from vmSystem.apps.admin_website.models.bank_accounts import BankAccounts
from vmSystem.apps.admin_website.models.person import Person
from vmSystem.apps.admin_website.models.cities import Cities
from vmSystem.apps.admin_website.models.provinces import Provinces
from vmSystem.apps.admin_website.models.employee import Employee
from vmSystem.apps.admin_website.models.providers import Providers
from vmSystem.apps.admin_website.models.companies import Companies

# Register your models here.
admin.site.register(Person)
admin.site.register(Provinces)
admin.site.register(Cities)
admin.site.register(BankAccounts)
admin.site.register(Employee)
admin.site.register(Providers)
admin.site.register(Companies)

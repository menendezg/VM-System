from django.contrib import admin
from vmSystem.apps.admin_website.models.bank_accounts import BankAccounts
from vmSystem.apps.admin_website.models.person import Person
from vmSystem.apps.admin_website.models.cities import Cities
from vmSystem.apps.admin_website.models.provinces import Provinces
from vmSystem.apps.admin_website.models.employee import Employee
from vmSystem.apps.admin_website.models.providers import Providers
from vmSystem.apps.admin_website.models.companies import Companies
from vmSystem.apps.admin_website.models.customer import Customer
from vmSystem.apps.admin_website.models.vehicles import Vehicles
from vmSystem.apps.admin_website.models.vehicle_owner import VehicleOwner

# Register your models here.
admin.site.register(Person)
admin.site.register(Provinces)
admin.site.register(Cities)
admin.site.register(BankAccounts)
admin.site.register(Employee)
admin.site.register(Providers)
admin.site.register(Companies)
admin.site.register(Customer)
admin.site.register(Vehicles)
admin.site.register(VehicleOwner)

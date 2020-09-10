from django.contrib import admin
from vmSystem.apps.entities.models.person_entity import Person
from vmSystem.apps.entities.models.provinces import Provinces
from vmSystem.apps.entities.models.cities import Cities


# Register your models here.
admin.site.register(Person)
admin.site.register(Provinces)
admin.site.register(Cities)

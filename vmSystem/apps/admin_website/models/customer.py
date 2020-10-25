from django.db import models

from .person import Person


class Customer(models.Model):
    """customer model representation"""

    business_name = models.CharField(max_length=128)
    cuix = models.CharField(max_length=255, default='')
    status = models.BooleanField(default='True')
    last_name = models.CharField(max_length=64)
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def update_atrributes(self, data, person_object):
        import pdb; pdb.set_trace()
        self.business_name = data["business_name"]
        self.cuix = data["cuix"]
        self.last_name = "last_name"
        self.person = person_object

    def __str__(self):
        return self.business_name

    class Meta:
        app_label = "admin_website"

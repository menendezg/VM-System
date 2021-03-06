from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    """Profile representation"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    state = models.BooleanField(default=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """return class representation."""
        return self.user.username

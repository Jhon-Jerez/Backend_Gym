from django.db import models
from django.conf import settings

class Gym(models.Model):
    name = models.CharField(max_length=150, unique=True)
    owner = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name="owned_gym")
    is_active = models.BooleanField(default=True) 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({'Activo' if self.is_active else 'Inactivo'})"

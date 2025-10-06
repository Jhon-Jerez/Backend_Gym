from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    class Roles(models.TextChoices):
        SUPERADMIN = "SUPERADMIN", "Superadmin"
        OWNER = "OWNER", "Dueño"
        RECEPTIONIST = "RECEPTIONIST", "Recepcionista"
        CLIENT = "CLIENT", "Cliente"

    role = models.CharField(max_length=20, choices=Roles.choices, default=Roles.CLIENT)

    gym = models.ForeignKey("gyms.Gym", on_delete=models.CASCADE, null=True, blank=True, related_name="users")

    def is_superadmin(self):
        return self.role == self.Roles.SUPERADMIN

    def is_owner(self):
        return self.role == self.Roles.OWNER

    def is_receptionist(self):
        return self.role == self.Roles.RECEPTIONIST

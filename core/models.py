from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    class Roles(models.TextChoices):
        SUPERADMIN = "superadmin", "Superadmin"
        OWNER = "owner", "Dueño de Gimnasio"
        RECEPTIONIST = "receptionist", "Recepcionista"
        

    role = models.CharField(max_length=20, choices=Roles.choices, default=Roles.OWNER)
    gym = models.ForeignKey("gyms.Gym",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="users"
    )

    def __str__(self):
        return f"{self.username} ({self.role})"

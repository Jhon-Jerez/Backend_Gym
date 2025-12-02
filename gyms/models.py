from django.db import models
from datetime import date, timedelta

MEMBERSHIP_DURATIONS = {
    "Mensual": 30,
    "Semana": 7,
    "Quincena": 15,
    "Sin membresía": 0,
}

class Gym(models.Model):
    name = models.CharField(max_length=150, unique=True)
    owner = models.OneToOneField(
        "core.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="owned_gym"
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({'Activo' if self.is_active else 'Inactivo'})"


class Member(models.Model):
    gym = models.ForeignKey(Gym, on_delete=models.CASCADE, related_name="members")
    full_name = models.CharField(max_length=100)
    cedula = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    joined_at = models.DateTimeField(auto_now_add=True)
    membership_type = models.CharField(max_length=50, default="Sin membresía")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.full_name} - {self.gym.name}"

    @property
    def membership_end(self):
        days = MEMBERSHIP_DURATIONS.get(self.membership_type, 0)
        if days == 0:
            return None
        return self.joined_at.date() + timedelta(days=days)

    @property
    def dias_restantes(self):
        if not self.membership_end:
            return None
        today = date.today()
        diff = (self.membership_end - today).days
        return diff if diff > 0 else 0

    @property
    def estado_membresia(self):
        dias = self.dias_restantes

        if dias is None:
            return "Sin membresía"
        if dias == 0:
            return "Vencida"
        if dias <= 5:
            return "Por vencer"
        return "Activa"
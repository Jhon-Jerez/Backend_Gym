from django.db import models

class Gym(models.Model):
    name = models.CharField(max_length=150, unique=True)
    owner = models.OneToOneField(
        "core.User",  # 🔹 Referencia perezosa en lugar de settings.AUTH_USER_MODEL
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
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.gym.name}"

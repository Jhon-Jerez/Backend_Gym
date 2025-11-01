from rest_framework import serializers
from django.apps import apps
from .models import User

class RegisterOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        Gym = apps.get_model('gyms', 'Gym')  # 👈 evita import circular
        user = User.objects.create_user(
            **validated_data,
            role=User.Roles.OWNER
        )
        # crea un gimnasio automático para ese dueño
        Gym.objects.create(name=f"Gimnasio de {user.username}", owner=user)
        return user

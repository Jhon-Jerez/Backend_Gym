from rest_framework import serializers
from django.contrib.auth import get_user_model
from gyms.models import Gym

User = get_user_model()

# ----- Serializador base de usuario -----
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role', 'gym']


# ----- Registrar dueño -----
class RegisterOwnerSerializer(serializers.ModelSerializer):
    gym_name = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'gym_name']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        gym_name = validated_data.pop('gym_name')
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            role=User.Roles.OWNER
        )
        Gym.objects.create(name=gym_name, owner=user)
        return user


# ----- Registrar recepcionista -----
class RegisterReceptionistSerializer(serializers.ModelSerializer):
    gym_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'gym_id']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        gym_id = validated_data.pop('gym_id')
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            role=User.Roles.RECEPTIONIST,
            gym_id=gym_id
        )
        return user

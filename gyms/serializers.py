from rest_framework import serializers
from .models import Gym, Member

class GymSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField()

    class Meta:
        model = Gym
        fields = ["id", "name", "owner", "is_active", "created_at"]



class MemberSerializer(serializers.ModelSerializer):
    dias_restantes = serializers.SerializerMethodField()
    estado_membresia = serializers.SerializerMethodField()
    membership_end = serializers.SerializerMethodField()
    class Meta:
        model = Member
        fields =['id','full_name','cedula','email','phone','joined_at','is_active','membership_type','dias_restantes','estado_membresia','membership_end']
        read_only_fields = ["joined_at"]


    def get_dias_restantes(self, obj):
        return obj.dias_restantes

    def get_estado_membresia(self, obj):
        return obj.estado_membresia

    def get_membership_end(self, obj):
        return obj.membership_end
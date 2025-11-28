from rest_framework import serializers
from .models import Gym, Member

class GymSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField()

    class Meta:
        model = Gym
        fields = ["id", "name", "owner", "is_active", "created_at"]



class MemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = Member
        fields =['id','full_name','email','phone','joined_at','is_active','membership_type']
        read_only_fields = ["joined_at"]

    
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import RegisterOwnerSerializer
from .models import User
from gyms.models import Gym 


class RegisterOwnerView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterOwnerSerializer




@api_view(['GET'])
@permission_classes([IsAuthenticated])
def me(request):
    user = request.user
    return Response({
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "role": user.role,
        "gym_id": user.gym.id if user.gym else None
    })

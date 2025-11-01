from rest_framework import generics
from .serializers import RegisterOwnerSerializer
from .models import User

class RegisterOwnerView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterOwnerSerializer

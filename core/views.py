from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from .serializers import (
    RegisterOwnerSerializer,
    RegisterReceptionistSerializer,
    UserSerializer
)
from django.contrib.auth import get_user_model

User = get_user_model()


# ----- Registrar dueño -----
class RegisterOwnerView(APIView):
    def post(self, request):
        serializer = RegisterOwnerSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ----- Registrar recepcionista -----
class RegisterReceptionistView(APIView):
    def post(self, request):
        serializer = RegisterReceptionistSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ----- Login -----
class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            return Response({
                'message': 'Inicio de sesión exitoso',
                'user': UserSerializer(user).data
            })
        return Response({'error': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)

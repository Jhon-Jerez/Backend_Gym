from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Gym, Member
from .serializers import GymSerializer, MemberSerializer


class GymListView(generics.ListAPIView):
    queryset = Gym.objects.all()
    serializer_class = GymSerializer


class MemberListCreateView(generics.ListCreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    def perform_create(self, serializer):
        gym_id = self.request.data.get("gym_id")
        gym = Gym.objects.get(id=gym_id)
        serializer.save(gym=gym)


@api_view(["GET"])
@permission_classes([AllowAny])

def gym_estadisticas(request, gym_id):
    try:
        gym = Gym.objects.get(id=gym_id)
    except Gym.DoesNotExist:
        return Response({"error": "Gimnasio no encontrado"}, status=status.HTTP_404_NOT_FOUND)

    # 📊 Obtener datos reales desde la base de datos
    total_usuarios = gym.members.count()

    # Si en Member tuvieras un campo "activo" (por ejemplo, para saber si está vigente)
    # puedes hacer filtros reales como estos:
    # activos = gym.members.filter(activo=True).count()
    # inactivos = gym.members.filter(activo=False).count()
    # presentes = gym.members.filter(presente=True).count()

    # Pero por ahora, si no existen esos campos, devolvemos los contadores base:
    data = {
        "gym_name": gym.name,
        "usuarios_totales": total_usuarios,
        "usuarios_activos": 0,    # cuando agregues campo 'activo' puedes cambiar esto
        "usuarios_presentes": 0,  # igual para 'presente'
        "usuarios_inactivos": 0,  # igual para 'activo=False'
    }

    return Response(data, status=status.HTTP_200_OK)

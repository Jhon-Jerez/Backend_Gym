from rest_framework import generics
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Gym, Member
from .serializers import GymSerializer, MemberSerializer


class GymListView(generics.ListAPIView):
    queryset = Gym.objects.all()
    serializer_class = GymSerializer


class MemberListCreateView(generics.ListCreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        user = self.request.user
        if user.role == "owner":
            return Member.objects.filter(gym=user.gym)
        return Member.objects.none()
    
    def perform_create(self, serializer):
        gym = self.request.user.owned_gym  # Gym del usuario autenticado
        serializer.save(gym=gym)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def Gym_stats(request, gym_id):
    members = Member.objects.filter(gym_id=gym_id)
    total = members.count()
    activos = members.filter(is_active=True).count()
    inactivos=members.filter(is_active=False).count()
    return Response({
        "total_clientes": total,
        "clientes_activos": activos,
        "inactivos": inactivos
    })



class MemberRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def buscar_miembro(request):
    cedula = request.query_params.get("cedula", None)
    if not cedula:
        return Response({"detail": "Debe enviar la cédula."}, status=400)

    try:
        miembro = Member.objects.get(cedula=cedula)
        return Response(MemberSerializer(miembro).data, status=200)
    except Member.DoesNotExist:
        return Response({"detail": "Usuario no encontrado."}, status=404)



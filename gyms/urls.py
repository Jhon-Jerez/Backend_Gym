from django.urls import path
from .views import GymListView, MemberListCreateView,MemberRetrieveUpdateDestroyView, Gym_stats, buscar_miembro

urlpatterns = [
    path("gyms/", GymListView.as_view(), name="gym-list"),
    path("members/", MemberListCreateView.as_view(), name="member-list-create"),
    path("members/<int:pk>/", MemberRetrieveUpdateDestroyView.as_view(), name="member-detail"),
    path("estadisticas/<int:gym_id>/", Gym_stats, name="gym_stats"),
    path("buscar-miembro/", buscar_miembro, name="buscar_miembro"),

]

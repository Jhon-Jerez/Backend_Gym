from django.urls import path
from .views import GymListView, MemberListCreateView,MemberRetrieveUpdateDestroyView, Gym_stats

urlpatterns = [
    path("gyms/", GymListView.as_view(), name="gym-list"),
    path("members/", MemberListCreateView.as_view(), name="member-list-create"),
    path("members/<int:pk>/", MemberRetrieveUpdateDestroyView.as_view(), name="member-detail"),
    path("estadisticas/<int:gym_id>/", Gym_stats, name="gym_stats"),
]

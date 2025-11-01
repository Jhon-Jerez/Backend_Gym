from django.urls import path
from .views import GymListView, MemberListCreateView, gym_estadisticas  

urlpatterns = [
    path("gyms/", GymListView.as_view(), name="gym-list"),
    path("members/", MemberListCreateView.as_view(), name="member-list-create"),
    path("estadisticas/<int:gym_id>/", gym_estadisticas, name="gym_estadisticas"),

]

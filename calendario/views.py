from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import CalendarEvent
from .serializers import CalendarEventSerializer


class CalendarEventViewSet(viewsets.ModelViewSet):
    serializer_class = CalendarEventSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        # Superadmin: ve todo
        if user.role == "superadmin":
            return CalendarEvent.objects.all().order_by("start")

        # Dueño o recepcionista → solo lo de su gimnasio
        if user.gym:
            return CalendarEvent.objects.filter(gym=user.gym).order_by("start")

        return CalendarEvent.objects.none()

    def perform_create(self, serializer):
        serializer.save(gym=self.request.user.gym)

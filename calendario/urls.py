from rest_framework.routers import DefaultRouter
from .views import CalendarEventViewSet

router = DefaultRouter()
router.register(r"events", CalendarEventViewSet, basename="calendar-events")

urlpatterns = router.urls

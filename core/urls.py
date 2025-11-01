from django.urls import path
from .views import RegisterOwnerView

urlpatterns = [
    path("register-owner/", RegisterOwnerView.as_view(), name="register-owner"),
]

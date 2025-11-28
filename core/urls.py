from django.urls import path
from .views import RegisterOwnerView,me

urlpatterns = [
    path("register-owner/", RegisterOwnerView.as_view(), name="register-owner"),
    path("me/", me, name="user-me"),


]

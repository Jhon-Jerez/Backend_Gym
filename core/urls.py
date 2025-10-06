from django.urls import path
from .views import RegisterOwnerView, RegisterReceptionistView, LoginView

urlpatterns = [
    path('register/owner/', RegisterOwnerView.as_view(), name='register-owner'),
    path('register/receptionist/', RegisterReceptionistView.as_view(), name='register-receptionist'),
    path('login/', LoginView.as_view(), name='token_obtain_pair'),
]


from django.urls import path
from .views import UserRegistrationAPIView,UserLoginAPIView,UserListAPIView,UserDetailsAPIView

urlpatterns = [
    path('register/', UserRegistrationAPIView.as_view(), name='user-register'),
    path('login/', UserLoginAPIView.as_view(), name='user-login'),
    path('users/', UserListAPIView.as_view(), name='user-list'),
    path('users/<int:user_id>/', UserDetailsAPIView.as_view(), name='user-details'),
     
     
     ]

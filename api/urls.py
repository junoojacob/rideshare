from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .views import UserRegistration
from rest_framework.routers import DefaultRouter
from .views import RideViewSet


router = DefaultRouter()
router.register(r'rides', RideViewSet, basename='ride')


urlpatterns = [
    path('register/', UserRegistration.as_view(), name='register'),
    path('login/', obtain_auth_token, name='login'),
    path('', include(router.urls)),
    
]



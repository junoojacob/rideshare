from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Ride

class RideSerializer(serializers.ModelSerializer):
    """
    Serializes(JSON) the Rider Model
    """
    class Meta:
        model = Ride
        fields = '__all__'   # Serializes all fields
        read_only_fields = ['rider', 'driver', 'status']  # Make this fields Read-only

class UserSerializer(serializers.ModelSerializer):
    """
    Searializes(JSON) the User Model
    """
    class Meta:
        model =User
        fields = ['id', 'username', 'password']
        extra_kwargs = {"password":{'write_only':True}}

    def create(self, validate_data):
        user = User.objects.create_user(**validate_data)
        return user
    
    
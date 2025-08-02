from django.contrib.auth.models import User
from rest_framework import generics, viewsets, permissions, status
from .serializers import UserSerializer
from .models import Ride
from .serializers import RideSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class RideViewSet(viewsets.ModelViewSet):
    queryset = Ride.objects.all()
    serializer_class = RideSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Assign the current user as the rider when creating a ride
        serializer.save(rider=self.request.user)

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def accept(self, request, pk=None):
        ride = self.get_object()
        if ride.status != 'requested':
            return Response({'error': 'Ride is not available for acceptance.'}, status=status.HTTP_400_BAD_REQUEST)

        ride.driver = request.user
        ride.status = 'started' # Or another status like 'accepted'
        ride.save()
        return Response(self.get_serializer(ride).data)

    @action(detail=True, methods=['patch'], url_path='update-status')
    def update_status(self, request, pk=None):
        ride = self.get_object()
        new_status = request.data.get('status')

        # Add logic here to ensure valid status transitions
        # e.g., only a driver can complete a ride, only a rider can cancel, etc.
        if new_status not in [s[0] for s in Ride.STATUS_CHOICES]:
            return Response({'error': 'Invalid status'}, status=status.HTTP_400_BAD_REQUEST)

        ride.status = new_status
        ride.save()
        return Response(self.get_serializer(ride).data)

    @action(detail=True, methods=['patch'], url_path='update-location')
    def update_location(self, request, pk=None):
        ride = self.get_object()
        # Ensure only the driver of the ride can update its location
        if request.user != ride.driver:
            return Response({'error': 'You are not the driver of this ride.'}, status=status.HTTP_403_FORBIDDEN)

        ride.current_location = request.data.get('current_location')
        ride.save()
        return Response({'status': 'location updated', 'current_location': ride.current_location})

class UserRegistration(generics.CreateAPIView):
    querryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes =[]
    

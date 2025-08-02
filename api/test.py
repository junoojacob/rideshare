# api/tests.py
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Ride

class RideModelTest(TestCase):
    def test_ride_creation(self):
        user = User.objects.create_user(username='testuser', password='password')
        ride = Ride.objects.create(
            rider=user,
            pickup_location='Point A',
            dropoff_location='Point B'
        )
        self.assertEqual(ride.status, 'requested')
        self.assertEqual(ride.rider.username, 'testuser')


# Add to api/tests.py
from rest_framework.test import APIClient
from rest_framework import status

class RideAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user('rider', password='password')
        self.client.force_authenticate(user=self.user)

    def test_create_ride(self):
        url = '/api/rides/'
        data = {'pickup_location': 'Home', 'dropoff_location': 'Work'}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Ride.objects.count(), 1)
        self.assertEqual(Ride.objects.get().rider, self.user)
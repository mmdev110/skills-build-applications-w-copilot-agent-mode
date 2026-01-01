from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase

from octofit_tracker.models import Activity, Leaderboard, Team, User, Workout


class ApiSmokeTests(APITestCase):
    def setUp(self):
        marvel = Team.objects.create(name="Marvel")
        self.user = User.objects.create(name="Tony Stark", email="tony@marvel.com", team=marvel)
        Workout.objects.create(name="Super Strength", description="Heavy lifting", suggested_for="Marvel")
        Activity.objects.create(user=self.user, type="Running", duration=30, date=timezone.now().date())
        Leaderboard.objects.create(user=self.user, score=100)

    def test_api_root(self):
        url = reverse('api-root')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('base_url', response.data)

    def test_users_list(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['email'], 'tony@marvel.com')

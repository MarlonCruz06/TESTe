from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

class DashboardTests(TestCase):

    def setUp(self):
        # Create a user for the tests
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.client.login(username='testuser', password='testpassword')

    def test_dashboard_view(self):
        # Test if the dashboard view is accessible
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/dashboard.html')
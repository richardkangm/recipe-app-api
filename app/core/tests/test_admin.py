from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):

    def setUp(self):
        self.client = Client()
        # creating an admin user for testing
        self.admin_user = get_user_model().objects.create_superuser(
            email='richardAdmin@gmail.com',
            password='admintest123'
        )
        self.client.force_login(self.admin_user)
        # creating a regular user for testing
        self.user = get_user_model().objects.create_user(
            email='testgmail.com',
            password='password123',
            name='Test user full name'
        )

    def test_users_listed(self):
        """Tests that users are listed on the user page"""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)  # perform a http get on the url given above

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """Test that the user edit page renders properly / works"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)

        # HTTP response code 200 means okay, so page works
        self.assertEqual(res.status_code, 200)  

    def test_create_user_page(self):
        """Tests that the create user page workds"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
        
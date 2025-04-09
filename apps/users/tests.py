from django.test import TestCase, Client
from django.urls import reverse
from .forms import UserRegistrationForm
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

User = get_user_model()

class RegisterViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('users:register')
        self.home_url = reverse('core:home')
        self.user_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'testpassword',
            'password2': 'testpassword',
            'plan': 'basic',  # Assuming 'basic' is a valid choice in your plan field
        }

    def test_register_view_get(self):
        """Test that the register view returns a 200 OK for GET requests."""
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/register.html')
        self.assertIsInstance(response.context['form'], UserRegistrationForm)

    def test_register_view_post_valid_data(self):
        """Test that a POST request with valid data creates a new user and redirects to the home page."""
        response = self.client.post(self.register_url, self.user_data)
        self.assertEqual(response.status_code, 302)  # Expect a redirect
        self.assertRedirects(response, self.home_url)
        self.assertTrue(User.objects.filter(username='testuser').exists())

    def test_register_view_post_invalid_password_mismatch(self):
        """Test that a POST request with mismatched passwords re-renders the form with errors."""
        invalid_data = self.user_data.copy()
        invalid_data['password2'] = 'differentpassword'
        response = self.client.post(self.register_url, invalid_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/register.html')
        self.assertFormError(response, 'form', 'password2', 'The two password fields didn’t match.')
        self.assertFalse(User.objects.filter(username='testuser').exists())

    # Add more tests for other validation scenarios in your form
    def test_register_view_post_existing_username(self):
        """Test that attempting to register with an existing username shows an error."""
        User.objects.create_user(username='existinguser', password='password')
        invalid_data = self.user_data.copy()
        invalid_data['username'] = 'existinguser'
        response = self.client.post(self.register_url, invalid_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/register.html')
        self.assertFormError(response, 'form', 'username', 'A user with that username already exists.')
        self.assertFalse(User.objects.filter(username='testuser').exists())


class CustomLoginViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('users:login')
        self.home_url = reverse('core:home')
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_login_view_get(self):
        """Test that the login view returns a 200 OK for GET requests."""
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/login.html')

    def test_login_view_post_valid_credentials(self):
        """Test that a POST request with valid credentials logs the user in and redirects to the home page."""
        response = self.client.post(self.login_url, {'username': 'testuser', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.home_url)
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_login_view_post_invalid_credentials(self):
        """Test that a POST request with invalid credentials re-renders the form with an error."""
        response = self.client.post(self.login_url, {'username': 'testuser', 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/login.html')
        self.assertIn('Please enter a correct username and password', response.content.decode())
        self.assertFalse(response.wsgi_request.user.is_authenticated)

    def test_login_view_post_inactive_user(self):
        """Test that attempting to log in with an inactive user shows an error."""
        self.user.is_active = False
        self.user.save()
        response = self.client.post(self.login_url, {'username': 'testuser', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/login.html')
        self.assertIn('Please enter a correct username and password', response.content.decode())
        self.assertFalse(response.wsgi_request.user.is_authenticated)
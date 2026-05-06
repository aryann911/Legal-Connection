from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class TestContactViews(TestCase):
    """
    A class for testing contact app views
    """
    def setUp(self):
        """
        Set Up function to create user and login user
        """
        self.user = User.objects.create_user(
            username='Demi', email='demi@gmail.com',
            password='demidemi')
        self.user.save()
        self.client.login(username='Demi', password='demidemi')

    def test_get_contact_page(self):
        """
        Test contact page
        """
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact-us.html')

    def test_user_can_send_message_to_admin(self):
        """
        Test to check users possibility send message to admin
        """
        response = self.client.post(
            reverse('contact'), {
                'first_name': 'Demi',
                'last_name': 'Demi',
                'email': "demi@gmail.com",
                'message': 'Test message'
            })
        self.assertEquals(response.status_code, 200)

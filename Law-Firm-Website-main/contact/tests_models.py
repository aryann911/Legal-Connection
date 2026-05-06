from django.test import TestCase
from django.contrib.auth.models import User
from .models import ContactModel


class TestContactModel(TestCase):
    """
    test Contact model
    """
    def setUp(self):
        """
        Set Up function to create user, login and message
        """
        self.user = User.objects.create_user(
                username='Demi', email='demi@gmail.com',
                password='demidemi')
        self.user.save()
        self.client.login(username='Demi', password='demidemi')
        self.contact = ContactModel.objects.create(
            user=self.user,
            first_name='Demi',
            last_name='Demi',
            email=self.user.email,
            message='Test message'
        )

    def test_contact_string_method_returns_right_string(self):
        """
        Test to check string return
        """
        contact = self.contact
        string = f"{self.contact.first_name} {self.contact.last_name}, "
        string += f"{self.contact.created_date}"
        self.assertEqual(
            str(contact),
            string
        )

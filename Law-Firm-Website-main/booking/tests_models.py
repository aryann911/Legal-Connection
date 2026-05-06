from django.test import TestCase
from django.contrib.auth.models import User
from .models import Service, Booking
import datetime


class TestBookingModel(TestCase):
    """
    A class for testing Booking model
    """
    def setUp(self):
        """
        Set Up function to create user, login and booking
        """
        self.user = User.objects.create_user(
            username='Demi', email='demi@gmail.com',
            password='demidemi')
        self.user.save()
        self.client.login(username='Demi', password='demidemi')
        self.service = Service.objects.create(
            service_name="test service",
            price=666,
            )
        self.service.save()
        self.booking = Booking.objects.create(
            user=self.user,
            service=self.service,
            name='test',
            email='test@g.com',
            phone='+380553333333',
            date=datetime.date(2023, 4, 12),
            time='10:00'
        )

    def test_booking_string_method_returns_title(self):
        """
        Test to check string method for booking model
        """
        booking = self.booking
        self.assertEqual(str(booking), 'test')

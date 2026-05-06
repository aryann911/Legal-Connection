from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Service, Booking
import datetime


class TestBookingViews(TestCase):
    """
    A class for testing Booking model
    """
    def setUp(self):
        """
        Set Up function to create user, login and booking
        """
        self.client = Client()
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

    def test_get_booknow_page(self):
        """
        test for open booknow page
        """
        response = self.client.get(reverse('booknow'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booknow.html')

    def test_get_booking_page(self):
        """
        test for open booking page
        """
        response = self.client.get(reverse('bookings'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings.html')

    def test_unauthorized_redirect(self):
        self.client.logout()
        response = self.client.get(reverse('bookings'))
        self.assertEqual(response.status_code, 302)

    def test_get_booking_edit_page(self):
        """
        test for open page for edit booking
        """
        response = self.client.get(reverse(
            'change_booking', args=[self.booking.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'change-booking.html')

    def test_get_booking_delete_page(self):
        """
        test for open page for delete booking
        """
        response = self.client.get(reverse(
            'delete_booking', args=[self.booking.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'delete-booking.html')

    def test_user_can_book(self):
        """
        test for book functionality
        """
        response = self.client.post(
            reverse('booknow'),
            {
                'user': self.user,
                'service': self.service.id,
                'name': 'test',
                'email': 'test@g.com',
                'phone': '+380553333333',
                'date':  datetime.date(2023, 4, 11),
                'time': '10:00'
            }
        )

        self.assertRedirects(response, '/booking/bookings/')

    def test_can_edit_booking(self):
        """
        test for edit booking functionality
        """
        id = self.booking.id
        response = self.client.post(
            reverse('change_booking', args=[id]), {
                'user': self.user,
                'service': self.service.id,
                'name': 'test',
                'email': 'test@g.com',
                'phone': '+380553333333',
                'date':  datetime.date(2023, 4, 11),
                'time': '11:00'
            })
        self.assertEquals(response.status_code, 302)
        self.booking.refresh_from_db()
        self.assertEquals(self.booking.time, '11:00')

    def test_can_delete_booking(self):
        """
        test for delete booking functionality
        """
        id = self.booking.id
        response = self.client.post(reverse('delete_booking', args=[id]))
        self.assertRedirects(response, reverse('bookings'), status_code=302)

    def test_can_show_message_if_date_exists(self):
        """
        test for edit booking functionality
        """
        response = self.client.post(
            reverse('booknow'),
            {
                'user': self.user,
                'service': self.service,
                'name': 'test',
                'email': 'test@g.com',
                'phone': '+380553333333',
                'date':  datetime.date(2023, 4, 12),
                'time': '10:00'
            }
        )
        self.assertEqual(response.status_code, 302)

    def test_can_show_message_if_date_exists_when_user_edit_bookings(self):
        """
        test for message when time/date exist
        """
        id = self.booking.id
        response = self.client.post(
            reverse('change_booking', args=[id]),
            {
                'user': self.user,
                'service': self.service.id,
                'name': 'test',
                'email': 'test@g.com',
                'phone': '+380553333333',
                'date':  datetime.date(2023, 4, 12),
                'time': '10:00'
            }
        )
        self.assertEqual(response.status_code, 302)

    def test_user_cannot_book(self):
        """
        test for book functionality
        """
        response = self.client.post(
            reverse('booknow'),
            {
                'user': self.user,
                'service': self.service.id,
                'name': 'test',
                'email': 'test@g.com',
                'phone': '+380553333333',
                'date':  datetime.date(2022, 4, 11),
                'time': '10:00'
            }
        )
        self.assertEquals(response.status_code, 200)

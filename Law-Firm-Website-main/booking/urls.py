from django.urls import path
from . import views

urlpatterns = [
    path('booknow/', views.booknow, name="booknow"),
    path('bookings/', views.bookings, name='bookings'),
    path('change/<int:booking_id>/', views.change_booking,
         name='change_booking'),
    path('delete-booking/<int:booking_id>/', views.delete_booking,
         name='delete_booking'),
    path('payment/<int:booking_id>/', views.payment, name='payment'),
    path('lawyer-dashboard/', views.lawyer_dashboard, name='lawyer_dashboard'),
    path('select-role/<str:role>/', views.select_role, name='select_role'),
]

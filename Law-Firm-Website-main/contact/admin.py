from django.contrib import admin
from daterangefilter.filters import DateRangeFilter
from .models import ContactModel


@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    """
    A class to show Contact Model in admin panel
    """
    list_filter = (
        'first_name',
        'last_name',
        'email',
        'phone_number',
        'created_date'
        )
    list_display = (
        'user',
        'first_name',
        'last_name',
        'email',
        'phone_number',
        'message',
        'created_date')

    search_fields = ['phone_number', ]
    list_filter = (('created_date', DateRangeFilter),)

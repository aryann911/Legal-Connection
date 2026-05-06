import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lawfirm.settings")
django.setup()

from booking.models import Service

legal_services = [
    {"service_name": "Personal Injury Consultation", "price": 1000.00},
    {"service_name": "Family Law Consultation", "price": 1500.00},
    {"service_name": "Criminal Defense Consultation", "price": 2000.00},
    {"service_name": "Business Law Consultation", "price": 1500.00},
    {"service_name": "General Legal Consultation", "price": 1000.00},
]

added_count = 0
updated_count = 0
for service_data in legal_services:
    service, created = Service.objects.update_or_create(
        service_name=service_data['service_name'],
        defaults={'price': service_data['price']}
    )
    if created:
        added_count += 1
        print(f"Added service: {service.service_name}")
    else:
        updated_count += 1
        print(f"Updated service: {service.service_name} to price {service.price}")

print(f"Total {added_count} services added, {updated_count} updated.")

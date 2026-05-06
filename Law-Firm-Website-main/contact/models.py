from django.db import models
from django.contrib.auth.models import User


class ContactModel(models.Model):
    """
    A class for the Contact model
    """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="contact_user",
        null=True
        )
    first_name = models.CharField(
        max_length=50,
        null=True
        )
    last_name = models.CharField(
        max_length=50,
        null=True
        )
    email = models.EmailField(
        max_length=254,
        default=""
        )
    phone_number = models.CharField(
        max_length=16,
        null=True,
        blank=True)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_date']

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.created_date}"

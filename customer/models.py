from django.db import models
from django.contrib.auth.models import User


# Model representing a menu item in the restaurant
class MenuItem(models.Model):
    name = models.CharField(max_length=100)  # The name of the menu item
    description = models.TextField(
        blank=True
    )  # A description of the menu item (optional)
    price = models.DecimalField(
        max_digits=8, decimal_places=2
    )  # The price of the menu item
    image_url = models.URLField(
        blank=True
    )  # URL of the image of the menu item (optional)

    def __str__(self):
        return self.name  # Return the name of the menu item for string representation


# Model representing the order address for a user
class OrderAddress(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True
    )  # Foreign key to the User model (null and blank allowed)
    area = models.CharField(max_length=255)  # The area part of the address
    city = models.CharField(max_length=100)  # The city part of the address
    pin_code = models.CharField(max_length=20)  # The pin code for the address
    phone_no = models.CharField(max_length=20)  # The phone number for the order address
    email = models.EmailField()  # The email address for the order
    payment_mode = models.CharField(
        max_length=50
    )  # The payment method chosen by the user
    created_at = models.DateTimeField(
        auto_now_add=True
    )  # Timestamp when the order address is created

    def __str__(self):
        return f"OrderAddress for {self.user} - {self.area}, {self.city}"  # String representation of the order address with user info

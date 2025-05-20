from django.db import models
from django.conf import settings
from customer.models import MenuItem  # Importing MenuItem model from the customer app


# Model representing a shopping cart
class Cart(models.Model):
    # Link the cart to a user (optional), cascade delete if user is deleted
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True
    )
    # Session key to identify a cart for anonymous users
    session_key = models.CharField(max_length=40, null=True, blank=True)
    # Timestamp when the cart is created
    created_at = models.DateTimeField(auto_now_add=True)
    # Timestamp when the cart is last updated
    updated_at = models.DateTimeField(auto_now=True, null=True)

    # String representation of the cart
    def __str__(self):
        return f"Cart ({self.id}) for user {self.user or self.session_key}"

    # Calculate total price of all items in the cart
    def total_price(self):
        return sum(item.subtotal() for item in self.items.all())


# Model representing an item inside the shopping cart
class CartItem(models.Model):
    # Each item is linked to a cart
    cart = models.ForeignKey(Cart, related_name="items", on_delete=models.CASCADE)
    # Each item is linked to a menu item
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    # Quantity of the menu item
    quantity = models.PositiveIntegerField(default=1)
    # Any additional price added to this item (optional)
    additional_price = models.DecimalField(
        max_digits=10, decimal_places=2, default=0, null=True
    )

    # String representation of the cart item
    def __str__(self):
        return f"{self.quantity} x {self.menu_item.name}"

    # Calculate subtotal for this cart item (price * quantity)
    def subtotal(self):
        return self.menu_item.price * self.quantity

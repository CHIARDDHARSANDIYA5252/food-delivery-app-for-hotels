# This file was made by Django on 2025-04-24 at 7:47 PM

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


# This class tells Django what changes to make in the database
class Migration(migrations.Migration):

    # This is the first version of the database for this app
    initial = True

    # Things this migration depends on (like other apps or users)
    dependencies = [
        ("customer", "0001_initial"),  # Wait for the customer app to be ready
        migrations.swappable_dependency(
            settings.AUTH_USER_MODEL
        ),  # Wait for the user model
    ]

    # These are the changes we are making (called operations)
    operations = [
        # We are creating a new table called "Cart"
        migrations.CreateModel(
            name="Cart",
            fields=[
                # Each cart has an ID (like a number tag)
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                # Each cart can have a session key (for users who are not logged in)
                ("session_key", models.CharField(blank=True, max_length=40, null=True)),
                # The time when the cart was made
                ("created_at", models.DateTimeField(auto_now_add=True)),
                # The cart can belong to a user (optional)
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        # We are creating another table called "CartItem"
        migrations.CreateModel(
            name="CartItem",
            fields=[
                # Each cart item has its own ID
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                # The number of this item in the cart
                ("quantity", models.PositiveIntegerField(default=1)),
                # The cart this item belongs to
                (
                    "cart",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="items",
                        to="cart.cart",
                    ),
                ),
                # The menu item (like pizza, burger, etc.)
                (
                    "menu_item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="customer.menuitem",
                    ),
                ),
            ],
        ),
    ]

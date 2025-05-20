# This file was made by Django on 2025-04-24 at 8:03 PM

from django.db import migrations, models


# This class tells Django what changes we want to make in the database
class Migration(migrations.Migration):

    # This change comes after we added "updated_at" to the cart
    dependencies = [
        ("cart", "0003_cart_updated_at"),
    ]

    # These are the changes we want to do now
    operations = [
        # We are adding a new field called "additional_price" to the CartItem table
        migrations.AddField(
            model_name="cartitem",  # We are changing the "CartItem" table
            name="additional_price",  # The new column is called "additional_price"
            field=models.DecimalField(  # This field will store extra money added to the item
                decimal_places=2,  # It can have 2 numbers after the dot (like 12.50)
                default=0,  # If we don’t add any extra price, it stays at 0
                max_digits=10,  # It can store big numbers (up to 10 digits total)
                null=True,  # It’s okay if we don’t fill this
            ),
        ),
    ]

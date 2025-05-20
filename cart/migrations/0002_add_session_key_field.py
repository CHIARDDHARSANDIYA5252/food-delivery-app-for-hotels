# This file was made by Django on 2025-04-24 at 7:56 PM

from django.db import migrations, models


# This class tells Django what changes to make in the database
class Migration(migrations.Migration):

    # This migration needs the first cart migration to be done first
    dependencies = [
        ("cart", "0001_initial"),
    ]

    # We are adding something new to the Cart table
    operations = [
        # Add a new field called "session_key" to the Cart
        migrations.AddField(
            model_name="cart",  # We're changing the "Cart" table
            name="session_key",  # We're adding a new column called "session_key"
            field=models.CharField(
                max_length=40, null=True, blank=True
            ),  # It's like a small code saved for guest users
        ),
    ]

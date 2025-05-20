# This file was made by Django on 2025-04-24 at 7:57 PM

from django.db import migrations, models


# This class tells Django what changes we want in the database
class Migration(migrations.Migration):

    # This change comes after the session_key was added
    dependencies = [
        ("cart", "0002_add_session_key_field"),
    ]

    # These are the changes we want to make now
    operations = [
        # We are adding a new field called "updated_at" to the Cart table
        migrations.AddField(
            model_name="cart",  # We're changing the "Cart" table
            name="updated_at",  # The new field is called "updated_at"
            field=models.DateTimeField(
                auto_now=True, null=True
            ),  # It saves the time when the cart was last changed
        ),
    ]

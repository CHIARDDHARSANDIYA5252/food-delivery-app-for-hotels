from django import forms
from .models import OrderAddress


class OrderAddressForm(forms.ModelForm):
    # Meta class to define the model and fields for the form
    class Meta:
        model = OrderAddress  # Model this form is based on
        fields = [
            "area",
            "city",
            "pin_code",
            "phone_no",
            "email",
            "payment_mode",
        ]  # Fields to be included in the form
        widgets = {
            # Custom widgets for each field to add placeholder and CSS classes
            "area": forms.TextInput(
                attrs={
                    "placeholder": "Enter your area",  # Placeholder text
                    "class": "form-control custom-input",  # CSS class for styling
                }
            ),
            "city": forms.TextInput(
                attrs={
                    "placeholder": "Enter your city",
                    "class": "form-control custom-input",
                }
            ),
            "pin_code": forms.TextInput(
                attrs={
                    "placeholder": "Enter your pin code",
                    "class": "form-control custom-input",
                }
            ),
            "phone_no": forms.TextInput(
                attrs={
                    "placeholder": "Enter your phone number",
                    "class": "form-control custom-input",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "placeholder": "Enter your email address",
                    "class": "form-control custom-input",
                }
            ),
            "payment_mode": forms.HiddenInput(),  # Payment mode is hidden in the form
        }

    # Custom initialization to set the initial value for payment_mode if available
    def __init__(self, *args, **kwargs):
        payment_mode = None
        # Check if "data" is available and extract payment_mode
        if "data" in kwargs:
            payment_mode = kwargs["data"].get("payment_mode")
        # Check if "initial" is available and extract payment_mode
        if not payment_mode and "initial" in kwargs:
            payment_mode = kwargs["initial"].get("payment_mode")

        # Call the parent class initialization method
        super().__init__(*args, **kwargs)

        # Set the initial value for the payment_mode field if it exists
        if payment_mode:
            self.fields["payment_mode"].initial = payment_mode

        # Optional: Add custom labels to make the form more user-friendly
        self.fields["area"].label = "Your Area"
        self.fields["city"].label = "City"
        self.fields["pin_code"].label = "Pin Code"
        self.fields["phone_no"].label = "Phone Number"
        self.fields["email"].label = "Email Address"

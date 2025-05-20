from django.shortcuts import render, redirect
from django.views import View
from .forms import OrderAddressForm
from .models import OrderAddress, MenuItem
from django.views.generic import TemplateView


# View to render the index page
class Index(View):
    def get(self, request):
        return render(request, "customer/index.html")  # Renders the index page template


# View to display the order success page
class OrderSuccessView(TemplateView):
    template_name = "customer/order_success.html"  # Template for order success


# View to render the About Us page
class About(View):
    def get(self, request):
        return render(request, "customer/about.html")  # Renders the About page template


# View to render the menu items
class Menu(View):
    def get(self, request):
        menu_items = MenuItem.objects.all()  # Fetch all menu items from the database
        return render(
            request, "customer/menu.html", {"menu_items": menu_items}
        )  # Renders the menu page with the menu items


# View to render the contact page
class Contact(View):
    def get(self, request):
        return render(
            request, "customer/contact.html"
        )  # Renders the contact page template


# View for placing an order (redirects to cart detail)
class OrderView(View):
    def get(self, request, item_id):
        # Placeholder for order view logic (for now, it redirects to the cart detail page)
        return redirect("cart:cart_detail")


# View for capturing the order address
class OrderAddressView(View):
    def get(self, request):
        # Fetch payment mode from URL parameters
        payment_mode = request.GET.get("payment_mode", "")

        # Check if the user is logged in
        if not request.user.is_authenticated:
            # If not logged in, show the login popup and provide the form with payment mode
            form = OrderAddressForm(initial={"payment_mode": payment_mode})
            return render(
                request,
                "customer/order_address.html",
                {"form": form, "show_login_popup": True},  # Display login popup
            )

        # If logged in, simply display the form
        form = OrderAddressForm(initial={"payment_mode": payment_mode})
        return render(request, "customer/order_address.html", {"form": form})

    def post(self, request):
        # Handle form submission when the user enters their address
        form = OrderAddressForm(request.POST)
        print("Form valid:", form.is_valid())  # Debug print for form validation status
        if form.is_valid():
            # If the form is valid, save the order address
            order_address = form.save(commit=False)
            if request.user.is_authenticated:
                order_address.user = (
                    request.user
                )  # Attach the logged-in user to the order
            order_address.save()  # Save the order address
            print(
                "Redirecting to order_success"
            )  # Debug print for successful redirection
            return redirect("order_success")  # Redirect to order success page
        else:
            # If form is invalid, show errors and re-render the form
            print("Form errors:", form.errors)  # Debug print for form errors
            return render(
                request, "customer/order_address.html", {"form": form}
            )  # Re-render form with errors

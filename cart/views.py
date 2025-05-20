from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Cart, CartItem
from customer.models import MenuItem
from django.contrib.auth.mixins import LoginRequiredMixin


# Utility function to get or create a cart for the current user or session
def get_cart(request):
    if request.user.is_authenticated:
        # If the user is logged in, retrieve or create a cart associated with the user
        cart, created = Cart.objects.get_or_create(user=request.user)
    else:
        # For anonymous users, use the session key to track the cart
        session_key = request.session.session_key
        if not session_key:
            request.session.create()  # Create a session if one doesn't exist
            session_key = request.session.session_key
        cart, created = Cart.objects.get_or_create(session_key=session_key)
    return cart


# View to add a menu item to the cart
class AddToCartView(View):
    def get(self, request, item_id, *args, **kwargs):
        cart = get_cart(request)  # Get the current user's or session's cart
        menu_item = get_object_or_404(MenuItem, id=item_id)  # Get the menu item
        # Try to get or create a cart item for the selected menu item
        cart_item, created = CartItem.objects.get_or_create(
            cart=cart, menu_item=menu_item
        )
        if not created:
            # If the item already exists in the cart, increase the quantity
            cart_item.quantity += 1
            cart_item.save()
        return redirect("cart:cart_detail")  # Redirect to cart detail view


# View to display the cart details
class CartDetailView(View):
    def get(self, request, *args, **kwargs):
        cart = get_cart(request)  # Get the cart
        # Fetch all items in the cart, using select_related to optimize DB access
        items = cart.items.select_related("menu_item").all()
        total_price = cart.total_price()  # Calculate total cart price
        # Render the cart page with cart details
        return render(
            request,
            "customer/cart.html",
            {"cart": cart, "items": items, "total_price": total_price},
        )


# View to update the quantity of a cart item
class UpdateCartItemView(View):
    def post(self, request, item_id, *args, **kwargs):
        cart = get_cart(request)  # Get the cart
        # Get the specific item in the cart
        cart_item = get_object_or_404(CartItem, cart=cart, menu_item_id=item_id)
        # Get the new quantity from the form data
        quantity = int(request.POST.get("quantity", 1))
        if quantity > 0:
            cart_item.quantity = quantity  # Update the quantity
            cart_item.save()
        else:
            cart_item.delete()  # Remove item if quantity is 0 or less
        return redirect("cart:cart_detail")  # Redirect to the cart detail view


# View to remove an item from the cart
class RemoveCartItemView(View):
    def post(self, request, item_id, *args, **kwargs):
        cart = get_cart(request)  # Get the cart
        # Get the item to remove
        cart_item = get_object_or_404(CartItem, cart=cart, menu_item_id=item_id)
        cart_item.delete()  # Delete the item from the cart
        return redirect("cart:cart_detail")  # Redirect back to the cart page

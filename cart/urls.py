from django.urls import path
from .views import AddToCartView, CartDetailView, UpdateCartItemView, RemoveCartItemView

# This is the name of the app (used for links)
app_name = "cart"

# These are the web addresses (URLs) for the cart
urlpatterns = [
    # When we go to the cart page, show all the items in the cart
    path("", CartDetailView.as_view(), name="cart_detail"),
    # When we go to this link, we add an item to the cart
    path("add/<int:item_id>/", AddToCartView.as_view(), name="add_to_cart"),
    # When we go to this link, we change how many items we want
    path(
        "update/<int:item_id>/", UpdateCartItemView.as_view(), name="update_cart_item"
    ),
    # When we go to this link, we remove an item from the cart
    path(
        "remove/<int:item_id>/", RemoveCartItemView.as_view(), name="remove_cart_item"
    ),
]

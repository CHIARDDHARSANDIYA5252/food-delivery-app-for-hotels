from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import MenuItem, OrderAddress
from cart.models import Cart, CartItem

# Unregister the original User admin.
admin.site.unregister(User)


# Register User with custom admin.
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = (
        "username",
        "email",
        "is_staff",
        "is_active",
        "last_login",
        "date_joined",
    )
    list_filter = ("is_staff", "is_active")
    search_fields = ("username", "email")


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "description")


@admin.register(OrderAddress)
class OrderAddressAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "area",
        "city",
        "pin_code",
        "phone_no",
        "email",
        "payment_mode",
        "created_at",
    )
    list_filter = ("city", "payment_mode", "created_at")
    search_fields = ("user__username", "area", "city", "email", "phone_no")


class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0
    readonly_fields = ("menu_item", "quantity", "additional_price", "subtotal")
    can_delete = False
    show_change_link = True


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "order_number",
        "total_price",
        "created_at",
        "updated_at",
    )
    list_filter = ("created_at", "updated_at")
    search_fields = ("user__username",)
    inlines = [CartItemInline]

    def order_number(self, obj):
        return f"ORDER-{obj.id}"

    order_number.short_description = "Order Number"


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ("cart", "menu_item", "quantity", "additional_price", "subtotal")
    search_fields = ("cart__user__username", "menu_item__name")

from django.urls import path
from .views import index, login_view, logout_view, signup_view

urlpatterns = [
    # Home page route, redirects to the home page if the user is authenticated
    path("", index, name="user_auth_home"),
    # Login page route
    path("login/", login_view, name="login"),
    # Logout page route, logs the user out
    path("logout/", logout_view, name="logout"),
    # Sign up page route for new users
    path("signup/", signup_view, name="signup"),
]

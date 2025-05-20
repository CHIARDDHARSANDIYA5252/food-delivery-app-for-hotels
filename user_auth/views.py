from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib import messages


# Home view, redirect to login if the user is not authenticated
def index(request):
    if request.user.is_authenticated:
        return render(request, "home/index.html")  # Home page if logged in
    return redirect("login")  # Redirect to login page if not logged in


# Login view, handles user login
def login_view(request):
    if request.user.is_authenticated:
        return redirect("index")  # Redirect to home if already logged in

    if request.method == "POST":
        # Get username and password from the form
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Try to authenticate the user
        user = authenticate(request, username=username, password=password)

        if user:
            auth_login(request, user)  # Log the user in
            return redirect("index")  # Redirect to home page
        else:
            return render(
                request,
                "home/login.html",
                {
                    "error_message": "Invalid username or password."
                },  # Show error if login fails
            )

    return render(request, "home/login.html")  # Render login page for GET request


# Logout view, logs the user out and redirects to home
def logout_view(request):
    auth_logout(request)  # Log the user out
    messages.info(request, "Goodbye! You have been logged out.")  # Show logout message
    return redirect("index")  # Redirect to home after logout


# Signup view, handles user registration
def signup_view(request):
    if request.method == "POST":
        # Get data from the form
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        # Check if passwords match
        if password != confirm_password:
            return render(
                request,
                "home/signup.html",
                {
                    "error_message": "Passwords do not match."
                },  # Show error if passwords don't match
            )

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            return render(
                request,
                "home/signup.html",
                {
                    "error_message": "Username already exists. Try another."
                },  # Show error if username is taken
            )

        # Create a new user
        user = User.objects.create_user(username=username, password=password)
        user.save()
        messages.success(
            request, "Account created successfully! Please log in."
        )  # Show success message
        return redirect("login")  # Redirect to login after successful signup

    return render(request, "home/signup.html")  # Render signup page for GET request

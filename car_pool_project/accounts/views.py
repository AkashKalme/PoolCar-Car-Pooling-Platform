from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RegisterUserForm

# Create your views here.


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            messages.success(request, ("You were logged in successfully."))
            login(request, user)
            return redirect('home-page')
        else:
            messages.success(request, ("You were logged in successfully."))
            return redirect('login-page')
    else:
        messages.success(request, ("You were logged in successfully."))
        return render(request, "registration/login.html")


def logout_user(request):
    messages.success(request, ("You were logged out successfully."))
    logout(request)
    return redirect('home-page')


def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Registration Successful!")
            return redirect('home-page')
    else:
        form = RegisterUserForm()
    return render(request, "registration/register.html", {'form': form})

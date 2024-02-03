from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def auth_test(request):
    return render (request, "base.html")

def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password1"]
        confirm_password = request.POST["password2"]
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username exists")
                return redirect("signup")
            user = User.objects.create_user(username=username, password=password)
            user.save()
            return redirect("signin")
        else:
            messages.info(request, "Password doesn't match")
            return redirect("signin")

    return render(request, "signup.html")

def signin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password1"]
        user = authenticate(request,username=username, password = password)
        if user is not None:
            login(request, user)
            
            
            return redirect("task_route")
        else:
            messages.info(request, "Invalid credentials")
            return redirect("signin")


    return render(request, "signin.html")

def loguser_out(request):
    logout(request)
    return redirect("signin")

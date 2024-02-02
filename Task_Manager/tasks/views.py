from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "base.html")

def home(request):
    return  render(request, "home.html")

def todo(request):
    return render(request, "todo.html")

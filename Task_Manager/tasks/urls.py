from django.contrib import admin
from django.urls import path
from .views import index, home, todo

urlpatterns = [
    path('test/', index, name="index"),
    path("",home, name="home_route"),
    path("tasks/", todo, name="task_route")
]

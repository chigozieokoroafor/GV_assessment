from django.contrib import admin
from django.urls import path
from .views import index, home, my_task, upload_view, spec_task, delete_task, mark_completed

urlpatterns = [
    path('test/', index, name="index"),
    path("myTasks/", my_task, name="task_route"),
    path("upload/", upload_view, name="upload_task"),
    path("myTasks/<int:pk>", spec_task, name="spec_task"),
    path("myTasks/<int:pk>/delete", delete_task, name="delete_task"),
    path("myTasks/<int:pk>/complete", mark_completed, name="completed"),
]

from django.urls import path
from .views import auth_test, signin, signup, loguser_out
urlpatterns = [
    path("test/", auth_test, name="auth_test"),
    path("signup/", signup, name = "signup"),
    path('signin/', signin, name = "signin"),
    path('logout/', loguser_out, name = "logout")

]
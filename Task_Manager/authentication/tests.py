from django.test import TestCase, Client
from django.urls import reverse, resolve

# Create your tests here.

class test_authentication(TestCase):
    def client(self):
        self.client:Client = Client()
    
    def test_login(self):
        url = reverse("signin")
        response = self.client.post(url, data={"username":"chigozie", "password":"password"}, follow=True)
        self.assertEquals(response.status_code, 200)
    
    def test_signup(self):
        url = reverse("signup")
        response = self.client.post(url, {
            "username":"TestDev",
            "password1":"chigozie",
            "password2":"chigozie"
        }, follow=True)
        self.assertEquals(response.status_code, 200)


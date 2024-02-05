from django.test import TestCase, SimpleTestCase, Client
from django.urls import reverse, resolve
from tasks.views import my_task, spec_task
from django.contrib.auth.models import User
from tasks.models import Task
from datetime import datetime
# Create your tests here.
class TaskTestUrl(TestCase):
    def test_my_task_url(self):
        # print(resolve(reverse("task_route")))
        url =  reverse("task_route")
        self.assertEquals(resolve(url).func, my_task)
    
    # def test_spec_task_url(self):
    #     url = reverse("spec_task", 1)

    #     self.assertEquals(resolve(url).func, spec_task)
        


class TaskTestView(TestCase):   
    def setUp(self):
        self.user = User.objects.create_user(username="testUser", password="password")
        self.task = Task.objects.create(
            title = 'Create Test case',
            description = "Create test cases for all routes and views being used",
            due_date = datetime.utcnow().date(),
            user = self.user
        )

    def client(self):
        self.client:Client = Client()

    def test_my_task_login_redirect(self):
        url =  reverse("task_route")
        response =  self.client.get(url)

        self.assertRedirects(response, "/accounts/login/?next=/myTasks/",target_status_code=200,status_code=302)
    
    def test_my_task_after_login(self):
        self.client.login(username="testUser", password="password")

        url = reverse("task_route")
        response = self.client.get(url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "my_tasks.html")
    
    def test_view_spec_task(self):
        self.client.login(username="testUser", password="password")
        
        url =  reverse("spec_task", args=[self.task.id])
        response = self.client.get(url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "update.html")

        
    def test_upload_tasks(self):
        url = reverse("upload_task")

        self.client.login(username="testUser", password="password")
        response = self.client.post(url, {"title":"new_test_title",
                               "description":"Finish up on creating test cases",
                               "due_date":datetime.utcnow().date()})
        

        self.assertRedirects(response, reverse("task_route"))


    def test_update_task(self):
        url  = reverse("spec_task", args=[self.task.id])

        self.client.login(username="testUser", password="password")
        response = self.client.post(url, {
            "title":"Updated Test case",
            "description":"former descrption updated",
            "due_date":datetime.utcnow().date()
        } )

        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, reverse("task_route"))
    
    def test_complete_task(self):
        url  = reverse("completed", args=[self.task.id])
        self.client.login(username="testUser", password="password")
        
        response = self.client.get(url)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("task_route"))



        

    
    # def test_my_task(self):
    #     url = reverse("signin")
    #     response = self.client.post(url, {"username":"chigozie", "password":"password"})
    #     self.assertEquals(response.status_code)

    # def test_spec_task_view(self):



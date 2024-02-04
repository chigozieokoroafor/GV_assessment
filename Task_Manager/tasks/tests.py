from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from tasks.views import my_task

# Create your tests here.
class TaskTestCase(TestCase):
    def test_list_resolve(self):
        # print(resolve(reverse("task_route")))
        url =  reverse("task_route")
        self.assertEquals(resolve(url).func, my_task)
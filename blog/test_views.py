# blog/tests/test_views.py

from django.test import TestCase
from django.urls import reverse

class BlogViewsTests(TestCase):

    def test_post_list_view(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)  # Check if the response is OK
        self.assertTemplateUsed(response, 'blog/post_list.html')  # Check if the correct template is used

    def test_hello_world_view(self):
        response = self.client.get(reverse('hello_world'))  # Adjust if necessary
        self.assertContains(response, "Hello, Blog!")  # Adjust the expected string

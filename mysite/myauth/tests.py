from django.test import TestCase
from django.urls import reverse

# class GetCookieViewTestCase(TestCase):
#     def test_get_cookie_view(self):
#         response = self.client.get(reverse('myauth:get-cookie'))
#         self.assertContains(response, 'Cookie')

class GetFoobarTestCase(TestCase):
    def test_foobar_view(self):
        response = self.client.get(reverse('myauth:foo-bar'))
        expected_data = {'foo': 123, 'bar': 456}
        self.assertJSONEqual(response, expected_data)
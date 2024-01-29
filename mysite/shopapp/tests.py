from django.test import TestCase
from django.urls import reverse

from .utils import add_two_numbers

class AddTwoNumbersTestCase(TestCase):
    def test_add_two_numbers(self):
        res = add_two_numbers(2,3)
        self.assertEqual(5, res)


class ProductCreateViewTestCase(TestCase):
    def test_create_product(self):
        response = self.client.post(reverse('shopapp:create-products'),{
            'name': 'Product from test',
            'price': '123.45',
            'description': 'Good product',
            'discount': '1',
        })

        self.assertRedirects(response, reverse('shopapp:shopapp:get-products'))

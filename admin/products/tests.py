import json
from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Product, User

# initialize the APIClient app
client = Client()

# Create your tests here.
class ProductsTestCase(TestCase):
    def setUp(self):
        self.valid_payload = {
            "id": 8,
            "title": "title",
            "image": "image",
            "likes": 2
        }

    def test_create_valid_product(self):
        response = client.post(
            reverse('products-view'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def add_products_setup(self):
        """
        Adds a test product into the database
        """
        Product.objects.create(id= 7, title= "title", image= 'image', likes= 0)
        # data.save()

    def test_urls(self):
        """
        Test the Application URLS.
        """
        url = reverse('products-view')
        self.assertEqual(url, '/api/products')


    def test_listing_products(self):
        """
        Test the listing of products
        """

        url = 'http://docker.for.mac.localhost:8000/api/products'
        response = client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_products(self):
        """
        Test Editing a product
        """

        url = 'http://docker.for.mac.localhost:8000/api/products/1'
        data = {
        "title": "new title",
        "image": "new image"
    }
        response = client.put(url, data, format='json')
        json = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    






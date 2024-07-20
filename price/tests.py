from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from price.models import Price
from users.models import User


class PriceTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            email="test@mail.com", password="1", is_superuser=True
        )
        self.price = Price.objects.create(price="25000")
        self.client.force_authenticate(user=self.user)

    def test_price_create(self):
        url = reverse("price:price_create")
        data = {"price": "50000"}
        response = self.client.post(url, data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Price.objects.all().count(), 2)

    def test_negative_price_create(self):
        url = reverse("price:price_create")
        data = {"price": "-50000"}
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_price_retrieve(self):
        url = reverse("price:price_detail", args=(self.price.pk,))
        response = self.client.get(url)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(float(data.get("taxes")), float(self.price.taxes))

    def test_price_update(self):
        url = reverse("price:price_update", args=(self.price.pk,))
        data = {"price": "60000"}
        response = self.client.patch(url, data)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("price"), "60000.00")

    def test_price_list(self):
        url = reverse("price:prices")
        response = self.client.get(url)
        data = response.json()
        result = [
            {
                "id": 5,
                "user": None,
                "goods": None,
                "taxes": "0.06",
                "bank_taxes": "0.02",
                "seller_taxes": "0.12",
                "self_profit": "0.20",
                "price": "25000.00",
                "total_price": None,
            }
        ]

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)

    def test_price_delete(self):
        url = reverse("price:price_delete", args=(self.price.pk,))
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Price.objects.all().count(), 0)

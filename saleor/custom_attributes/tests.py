import pytest
from django.test import TestCase
from django.urls import reverse
from .models import CustomAttribute

class CustomAttributeViewTest(TestCase):
    def setUp(self):
        # create some custom attributes
        self.attribute1 = CustomAttribute.objects.create(
            name="Color",
            slug="color",
            input_type="DROPDOWN",
            entity_type="PRODUCT",
        )
        self.attribute2 = CustomAttribute.objects.create(
            name="Size",
            slug="size",
            input_type="NUMERIC",
            entity_type="VARIANT",
            unit="cm",
        )

    def test_list_custom_attributes(self):
        # test the list_custom_attributes view function
        url = reverse("list-custom-attributes")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]["name"], "Color")
        self.assertEqual(data[0]["slug"], "color")
        self.assertEqual(data[0]["input_type"], "DROPDOWN")
        self.assertEqual(data[0]["entity_type"], "PRODUCT")
        self.assertIsNone(data[0]["unit"])
        self.assertEqual(data[1]["name"], "Size")
        self.assertEqual(data[1]["slug"], "size")
        self.assertEqual(data[1]["input_type"], "NUMERIC")
        self.assertEqual(data[1]["entity_type"], "VARIANT")
        self.assertEqual(data[1]["unit"], "cm")
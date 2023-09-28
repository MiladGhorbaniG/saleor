import json
import pytest
from django.test import TestCase
from django.urls import reverse
from graphene.test import Client
from graphql_jwt.testcases import JSONWebTokenTestCase
from .models import CustomAttribute

class CustomAttributeTests(JSONWebTokenTestCase):
    def setUp(self):
        self.client = Client(schema)  # Use your GraphQL schema here

        # Create some custom attributes
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

        # Create a user with appropriate permissions for testing security
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.user.user_permissions.add(Permission.objects.get(codename="delete_customattribute"))

    def test_list_custom_attributes(self):
        # Test the list_custom_attributes GraphQL query
        query = '''
        query {
            listCustomAttributes {
                id
                name
                slug
                inputType
                entityType
                unit
            }
        }
        '''
        response = self.client.execute(query)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(len(data['data']['listCustomAttributes']), 2)
        self.assertEqual(data['data']['listCustomAttributes'][0]['name'], "Color")
        self.assertEqual(data['data']['listCustomAttributes'][0]['slug'], "color")
        self.assertEqual(data['data']['listCustomAttributes'][0]['inputType'], "DROPDOWN")
        self.assertEqual(data['data']['listCustomAttributes'][0]['entityType'], "PRODUCT")
        self.assertIsNone(data['data']['listCustomAttributes'][0]['unit'])
        self.assertEqual(data['data']['listCustomAttributes'][1]['name'], "Size")
        self.assertEqual(data['data']['listCustomAttributes'][1]['slug'], "size")
        self.assertEqual(data['data']['listCustomAttributes'][1]['inputType'], "NUMERIC")
        self.assertEqual(data['data']['listCustomAttributes'][1]['entityType'], "VARIANT")
        self.assertEqual(data['data']['listCustomAttributes'][1]['unit'], "cm")

    def test_create_custom_attribute_mutation(self):
        # Test the createCustomAttribute GraphQL mutation
        mutation = '''
        mutation ($input: CustomAttributeInput!) {
            createCustomAttribute(input: $input) {
                customAttribute {
                    id
                    name
                    slug
                    inputType
                    entityType
                    unit
                }
            }
        }
        '''
        variables = {
            "input": {
                "name": "Material",
                "slug": "material",
                "inputType": "TEXT",
                "entityType": "VARIANT",
                "unit": None
            }
        }
        response = self.client.execute(mutation, variable_values=variables)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['data']['createCustomAttribute']['customAttribute']['name'], "Material")

    def test_update_custom_attribute_mutation(self):
        # Test the updateCustomAttribute GraphQL mutation
        mutation = '''
        mutation ($id: ID!, $input: CustomAttributeInput!) {
            updateCustomAttribute(id: $id, input: $input) {
                customAttribute {
                    id
                    name
                    slug
                    inputType
                    entityType
                    unit
                }
            }
        }
        '''
        variables = {
            "id": self.attribute1.id,
            "input": {
                "name": "New Color",
                "slug": "new-color",
                "inputType": "RADIO",
                "entityType": "VARIANT",
                "unit": None
            }
        }
        response = self.client.execute(mutation, variable_values=variables)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['data']['updateCustomAttribute']['customAttribute']['name'], "New Color")

    def test_delete_custom_attribute_mutation(self):
        # Test the deleteCustomAttribute GraphQL mutation
        mutation = '''
        mutation ($id: ID!) {
            deleteCustomAttribute(id: $id) {
                success
            }
        }
        '''
        variables = {
            "id": self.attribute1.id
        }
        # Ensure only authorized users with permission can delete attributes
        self.client.login(username="testuser", password="testpassword")
        response = self.client.execute(mutation, variable_values=variables)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data['data']['deleteCustomAttribute']['success'])

    def test_invalid_inputs(self):
        # Test mutations with invalid input data (e.g., missing required fields, incorrect data types)
        mutation = '''
        mutation ($input: CustomAttributeInput!) {
            createCustomAttribute(input: $input) {
                customAttribute {
                    id
                }
            }
        }
        '''
        variables = {
            "input": {
                "name": "",  # Missing required field
                "slug": "invalid-slug",  # Invalid slug
                "inputType": "INVALID_TYPE",  # Invalid input type
                "entityType": "VARIANT",
                "unit": None
            }
        }
        response = self.client.execute(mutation, variable_values=variables)
        self.assertEqual(response.status_code, 400)  # Expect a validation error

    def test_edge_cases(self):
        # Test edge cases, such as empty attribute lists, large data sets, etc.
        # Edge case: Test when there are no custom attributes
        CustomAttribute.objects.all().delete()
        query = '''
        query {
            listCustomAttributes {
                id
            }
        }
        '''
        response = self.client.execute(query)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(len(data['data']['listCustomAttributes']), 0)

    def test_performance(self):
        # Test performance of GraphQL queries and mutations under heavy load
        # Create a large number of custom attributes and measure response times
        pass  # Placeholder for performance testing

    # Add more test cases for various scenarios as needed


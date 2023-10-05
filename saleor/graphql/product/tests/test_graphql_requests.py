
import requests
import traceback
# Define the base URL of your GraphQL endpoint
BASE_URL = 'http://127.0.0.1:8000/graphql/'  # Update with your actual URL

def test_list_custom_attributes():
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
    response = requests.post(BASE_URL, json={'query': query})
    assert response.status_code == 200
    # Add your assertions to verify the data

def test_create_custom_attribute_mutation():
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
    response = requests.post(BASE_URL, json={'query': mutation, 'variables': variables})
    assert response.status_code == 200
    # Add your assertions to verify the data

def test_update_custom_attribute_mutation():
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
        "id": "REPLACE_WITH_ATTRIBUTE_ID",
        "input": {
            "name": "New Color",
            "slug": "new-color",
            "inputType": "RADIO",
            "entityType": "VARIANT",
            "unit": None
        }
    }
    response = requests.post(BASE_URL, json={'query': mutation, 'variables': variables})
    assert response.status_code == 200
    # Add your assertions to verify the data

def test_delete_custom_attribute_mutation():
    mutation = '''
    mutation ($id: ID!) {
        deleteCustomAttribute(id: $id) {
            success
        }
    }
    '''
    variables = {
        "id": "REPLACE_WITH_ATTRIBUTE_ID",
    }
    user = User.objects.create_user(username="testuser", password="testpassword")
    user.user_permissions.add(Permission.objects.get(codename="delete_customattribute"))
    client.login(username="testuser", password="testpassword")
    response = requests.post(BASE_URL, json={'query': mutation, 'variables': variables})
    assert response.status_code == 200
    # Add your assertions to verify the data

def test_invalid_inputs():
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
            "name": "",
            "slug": "invalid-slug",
            "inputType": "INVALID_TYPE",
            "entityType": "VARIANT",
            "unit": None
        }
    }
    response = requests.post(BASE_URL, json={'query': mutation, 'variables': variables})
    assert response.status_code == 400
    # Add your assertions to verify the data

def test_edge_cases():
    query = '''
    query {
        listCustomAttributes {
            id
        }
    }
    '''
    response = requests.post(BASE_URL, json={'query': query})
    assert response.status_code == 200
    # Add your assertions to verify the data

def test_performance():
    query = '''
    query {
        listCustomAttributes {
            id
            name
        }
    }
    '''
    import time
    start_time = time.time()
    response = requests.post(BASE_URL, json={'query': query})
    end_time = time.time()
    elapsed_time_ms = (end_time - start_time) * 1000
    assert response.status_code == 200
    print(f"Elapsed time for query: {elapsed_time_ms:.2f} ms")


def test_run_individual_tests():
    print('test_list_custom_attributes')
    try:
        test_list_custom_attributes()
    except:
        traceback.print_exc()
    print('test_create_custom_attribute_mutation')
    try:
        test_create_custom_attribute_mutation()
    except:
        traceback.print_exc()
    print('test_update_custom_attribute_mutation')
    try:
        test_update_custom_attribute_mutation()
    except:
        traceback.print_exc()
    print('test_delete_custom_attribute_mutation')
    try:
        test_delete_custom_attribute_mutation()
    except:
        traceback.print_exc()
    print('test_invalid_inputs')
    try:
        test_invalid_inputs()
    except:
        traceback.print_exc()
    print('test_edge_cases')
    try:
        test_edge_cases()
    except:
        traceback.print_exc()
    print('test_performance')
    try:
        test_performance()
    except:
        traceback.print_exc()
if __name__ == "__main__":
    test_run_individual_tests()
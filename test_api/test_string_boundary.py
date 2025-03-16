import pytest
import requests
import os
from fixtures.conftest import authenticated_headers
from config import BASE_URL, GITHUB_PAT

# Showcasing a boundary testing


# Defining fixture to test string boundary value
@pytest.fixture
def reset_name(authenticated_headers):
    # Resetting name to null
    yield
    requests.patch(f'{BASE_URL}/user', headers=authenticated_headers, json={"name":""})

@pytest.mark.parametrize('name, expected_status', [
        ('a', 200),
        ('a' * 255, 200), # Maximum value
        ('a' * 256, 422), # off limit (invalid)
        ("", 200), # minimum value
        ((" " * 127) + "a" + (" " * 127), 200), # white spaces are allowed
])

def test_name_boundary(name, expected_status, authenticated_headers):
    """Boundary test for name field """
    response = requests.patch(f'{BASE_URL}/user', headers=authenticated_headers, json={"name":name})

    assert response.status_code == expected_status, f'Failed for {name}: Expected {expected_status}, but got {response.status_code}'

    if response.status_code == 200:
        if name == "":
            assert response.json()['name'] is None, f'Failed for {name}: Expected null, but got {response.json()["name"]}'
        else:
            assert response.json()['name'] == name, f'Failed for {name}: Expected {name}, but got {response.json()["name"]}'


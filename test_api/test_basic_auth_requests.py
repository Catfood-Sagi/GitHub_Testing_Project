import pytest
import requests
import os
from fixtures.conftest import authenticated_headers
from config import BASE_URL, GITHUB_PAT


# Authenticated request
@pytest.mark.parametrize('auth_headers, expected_status', [
    ('valid', 200),
    (None, 401)
])

def test_authenticated_request(auth_headers, expected_status, authenticated_headers):
    """Test authenticated request"""
    headers = authenticated_headers if auth_headers == 'valid' else None

    url = f'{BASE_URL}/user'
    response = requests.get(url, headers=headers)
    assert response.status_code == expected_status
    # test that response is not empty
    if response.status_code == 200:
        assert 'id' in response.json()
        assert 'asdacxcsas' in response.json()



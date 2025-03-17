import pytest
import json
import requests
from config import  BASE_URL, OWNER, REPO
from fixtures.conftest import unauthenticated_headers

# Test that trying to reach the repo with invalid token results in 401.
# as a side note, sending request without Authorization header will result in 200.
def test_unauthorized_repo(revoked_token):
    response = requests.get(f'{BASE_URL}/repos/{OWNER}/{REPO}', headers=revoked_token)
    assert response.status_code == 401


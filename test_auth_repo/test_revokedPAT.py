import requests
import pytest
import json
from config import BASE_URL, OWNER, REPO
from fixtures.conftest import revoked_token, resetting_repo


# Testing a Revoked PAT cannot change the repository settings
def test_revoked_pat(revoked_token, resetting_repo):

    request_body = {
        "description": "This is your first repository",
     }
    response = requests.patch(f'{BASE_URL}/repos/{OWNER}/{REPO}', headers=revoked_token, json=request_body)
    assert response.status_code == 401
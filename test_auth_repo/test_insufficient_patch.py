import pytest
import json
import requests
from config import  BASE_URL, OWNER, REPO
from fixtures.conftest import *

# Since my repo is personal, I cannot change access right to collaborators. - they all have the proper access rights
# For testing purpose, I will write the tests and mark it as expected to fail.

@pytest.mark.xfail(allow_module_level=True)
def test_unauthorized_repo_settings(unauthenticated_headers, resetting_repo):
    # If I had a user with a read only permission, I would have used his credentials to test this

    request_body = {
        "name": "new_repo_name",
        "description": "This is your first repository",
        "private": True,
     }

    response = requests.patch(f'{BASE_URL}/repos/{OWNER}/{REPO}', headers=unauthenticated_headers, json=request_body)
    assert response.status_code == 403
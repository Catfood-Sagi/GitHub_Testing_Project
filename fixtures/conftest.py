import os
import pytest
from config import BASE_URL, GITHUB_PAT, REVOKED_PAT, OWNER, REPO
import requests



# Authenticated Headers
@pytest.fixture
def authenticated_headers():
    """Fixture to return authenticated headers"""
    return {
        'Authorization': f'Bearer {GITHUB_PAT}',
        'Accept': 'application/vnd.github.v3+json'
    }


@pytest.fixture
def unauthenticated_headers():
    """Fixture to return unauthenticated headers"""
    return {
        'Accept': 'application/vnd.github.v3+json'
    }


@pytest.fixture
def revoked_token():
    """Fixture to return revoked token"""
    return {
        'Authorization': f'Bearer {REVOKED_PAT}',
        'Accept': 'application/vnd.github.v3+json'
    }


@pytest.fixture
def resetting_repo():
    print("Starting fixture")
    auth_headers = {
        'Authorization': f'Bearer {GITHUB_PAT}',
        'Accept': 'application/vnd.github.v3+json'
    }
    response = requests.get(f'{BASE_URL}/repos/{OWNER}/{REPO}', headers=auth_headers)
    original_settings = response.json()
    yield

    # After the test runs, reset the repo settings back to the original
    requests.patch(f'{BASE_URL}/repos/{OWNER}/{REPO}', headers=auth_headers, json=original_settings)
    print("Resetting repo settings")
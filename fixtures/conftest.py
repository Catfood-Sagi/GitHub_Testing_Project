import os
import pytest
from config import BASE_URL, GITHUB_PAT


# Authenticated Headers
@pytest.fixture
def authenticated_headers():
    '''Fixture to return authenticated headers'''
    return {
        'Authorization': f'Bearer {GITHUB_PAT}',
        'Accept': 'application/vnd.github.v3+json'
    }
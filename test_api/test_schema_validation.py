import pytest
import requests
import os
from jsonschema import validate, ValidationError
from fixtures.conftest import authenticated_headers
from config import BASE_URL, GITHUB_PAT
import json

#Loading Response Schema
with open (r'C:\Users\sagig\PycharmProjects\GitHub_Testing_Project\schemas\github_response_schema_user.json', 'r') as f:
    schema = json.load(f)

def test_schema_validation(authenticated_headers):
    response = requests.get(f'{BASE_URL}/user', headers=authenticated_headers)
    response_body = response.json()
    validate(response_body, schema=schema)
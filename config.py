#config.py
import os
from dotenv import load_dotenv


load_dotenv()

# GitHub API Settings

BASE_URL = "https://api.github.com"
GITHUB_PAT = os.getenv('GITHUB_PAT')
REVOKED_PAT = os.getenv('REVOKED_PAT')
OWNER = "Catfood-Sagi"
REPO = "GitHub_Testing_Project"
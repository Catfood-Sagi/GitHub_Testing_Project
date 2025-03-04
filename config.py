#config.py
import os
from dotenv import load_dotenv


load_dotenv()

# GitHub API Settings

BASE_URL = "https://api.github.com"
GITHUB_PAT = os.getenv('GITHUB_PAT')
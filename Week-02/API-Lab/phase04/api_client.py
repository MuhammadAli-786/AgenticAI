"""Phase 04: demonstrate auth headers and read credentials from .env."""
import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

# Demonstrate construction safely; JSONPlaceholder does not require this key.
headers = {}
if API_KEY:
    headers["Authorization"] = f"Bearer {API_KEY}"
else:
    # Placeholder used only to show the expected header format; not a real secret.
    headers["Authorization"] = "Bearer <TOKEN_PLACEHOLDER>"

print("Request header configuration:")
print({"Authorization": "Bearer <REDACTED>" if API_KEY else "Bearer <TOKEN_PLACEHOLDER>"})

# This public demo endpoint does not validate the example token.
try:
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts/1",
        headers=headers,
        timeout=10,
    )
    print(f"HTTP status: {response.status_code}")
except requests.Timeout:
    print("Request timed out.")
except requests.RequestException as exc:
    print(f"Request failed: {exc}")

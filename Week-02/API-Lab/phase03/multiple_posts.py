"""Task 14: retrieve three posts without duplicating the program."""
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

for post_id in (1, 2, 3):
    try:
        response = requests.get(f"{BASE_URL}/posts/{post_id}", timeout=10)
        response.raise_for_status()
        post = response.json()
        print(f"Post {post_id}: {post['title']}")
    except requests.RequestException as exc:
        print(f"Post {post_id}: request failed ({exc})")

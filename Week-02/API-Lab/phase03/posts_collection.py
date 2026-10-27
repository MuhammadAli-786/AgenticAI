"""Task 15: retrieve the collection, count it, and print five titles."""
import requests

url = "https://jsonplaceholder.typicode.com/posts"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    posts = response.json()
    print(f"Total posts: {len(posts)}")
    print("First five titles:")
    for post in posts[:5]:
        print(f"- {post['title']}")
except requests.Timeout:
    print("Request timed out.")
except requests.RequestException as exc:
    print(f"API/network request failed: {exc}")
except (ValueError, KeyError) as exc:
    print(f"Could not process response JSON: {exc}")

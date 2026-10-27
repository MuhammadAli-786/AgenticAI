"""Week 02, Phase 03: simple JSONPlaceholder API client."""
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def get_post(post_id):
    url = f"{BASE_URL}/posts/{post_id}"
    try:
        response = requests.get(url, timeout=10)
        print(f"Status: {response.status_code}")
        response.raise_for_status()
        post = response.json()
        print(f"Post ID: {post['id']}")
        print(f"Title: {post['title']}")
        print(f"Body: {post['body']}")
    except requests.HTTPError as exc:
        print(f"Request failed with HTTP status {exc.response.status_code}.")
    except requests.Timeout:
        print("Request timed out.")
    except requests.RequestException as exc:
        print(f"Network/request failure: {exc}")
    except (ValueError, KeyError) as exc:
        print(f"Could not process JSON response: {exc}")

if __name__ == "__main__":
    get_post(1)

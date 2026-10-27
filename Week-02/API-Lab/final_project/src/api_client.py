"""Complete Week 02 API client for JSONPlaceholder."""
import argparse
import os
import requests
from dotenv import load_dotenv

BASE_URL = "https://jsonplaceholder.typicode.com"
load_dotenv()

def explain_status(code):
    return {
        200: "OK — request succeeded",
        201: "Created — resource creation accepted",
        400: "Bad Request — check request parameters/body",
        401: "Unauthorized — authentication is missing or invalid",
        403: "Forbidden — access is not allowed",
        404: "Not Found — resource does not exist",
        429: "Too Many Requests — rate limit exceeded",
        500: "Internal Server Error — server-side failure",
    }.get(code, f"HTTP status {code}")

def get_post(post_id):
    url = f"{BASE_URL}/posts/{post_id}"
    try:
        response = requests.get(url, timeout=10)
        print(f"Endpoint: {url}")
        print(f"Method: GET")
        print(f"Status: {response.status_code} ({explain_status(response.status_code)})")
        if response.status_code == 404:
            print("Request failed. Resource not found.")
            return
        response.raise_for_status()
        post = response.json()
        for field in ("userId", "id", "title", "body"):
            if field in post:
                print(f"{field}: {post[field]}")
    except requests.Timeout:
        print("Timeout: no response within 10 seconds.")
    except requests.ConnectionError:
        print("Network failure: unable to connect.")
    except requests.HTTPError as exc:
        print(f"API error: {exc}")
    except requests.RequestException as exc:
        print(f"Request failed: {exc}")
    except ValueError:
        print("API returned invalid JSON.")

def create_post(title, body, user_id):
    url = f"{BASE_URL}/posts"
    payload = {"title": title, "body": body, "userId": user_id}
    try:
        response = requests.post(url, json=payload, timeout=10)
        print(f"Endpoint: {url}\nMethod: POST\nStatus: {response.status_code}")
        print(response.json())
    except requests.Timeout:
        print("Request timed out.")
    except requests.RequestException as exc:
        print(f"Request failed: {exc}")

def update_post(post_id, title, body, user_id):
    url = f"{BASE_URL}/posts/{post_id}"
    payload = {"id": post_id, "title": title, "body": body, "userId": user_id}
    try:
        response = requests.put(url, json=payload, timeout=10)
        print(f"Endpoint: {url}\nMethod: PUT\nStatus: {response.status_code}")
        response.raise_for_status()
        print(response.json())
    except requests.Timeout:
        print("Request timed out.")
    except requests.RequestException as exc:
        print(f"Request failed: {exc}")

def delete_post(post_id):
    url = f"{BASE_URL}/posts/{post_id}"
    try:
        response = requests.delete(url, timeout=10)
        print(f"Endpoint: {url}\nMethod: DELETE\nStatus: {response.status_code}")
        if response.ok:
            print("Delete request succeeded (JSONPlaceholder simulates deletion).")
            print(response.text or "{}")
        else:
            print(explain_status(response.status_code))
    except requests.Timeout:
        print("Request timed out.")
    except requests.RequestException as exc:
        print(f"Request failed: {exc}")

def list_posts():
    try:
        response = requests.get(f"{BASE_URL}/posts", timeout=10)
        response.raise_for_status()
        posts = response.json()
        print(f"Total posts: {len(posts)}")
        for post in posts[:5]:
            print(f"{post['id']}: {post['title']}")
    except requests.Timeout:
        print("Request timed out.")
    except requests.RequestException as exc:
        print(f"Request failed: {exc}")
    except (ValueError, KeyError) as exc:
        print(f"Response processing error: {exc}")

def main():
    parser = argparse.ArgumentParser(description="Week 02 JSONPlaceholder API lab")
    sub = parser.add_subparsers(dest="command", required=True)
    get_parser = sub.add_parser("get", help="retrieve a post")
    get_parser.add_argument("post_id", type=int)
    sub.add_parser("list", help="retrieve collection and print first five titles")
    create_parser = sub.add_parser("create", help="create a simulated post")
    create_parser.add_argument("--title", default="My API Lab")
    create_parser.add_argument("--body", default="Testing POST request")
    create_parser.add_argument("--user-id", type=int, default=1)
    update_parser = sub.add_parser("update", help="update a simulated post")
    update_parser.add_argument("post_id", type=int)
    update_parser.add_argument("--title", default="Updated API Lab")
    update_parser.add_argument("--body", default="This post was updated using PUT")
    update_parser.add_argument("--user-id", type=int, default=1)
    delete_parser = sub.add_parser("delete", help="send a simulated DELETE")
    delete_parser.add_argument("post_id", type=int)
    args = parser.parse_args()

    if args.command == "get":
        get_post(args.post_id)
    elif args.command == "list":
        list_posts()
    elif args.command == "create":
        create_post(args.title, args.body, args.user_id)
    elif args.command == "update":
        update_post(args.post_id, args.title, args.body, args.user_id)
    elif args.command == "delete":
        delete_post(args.post_id)

if __name__ == "__main__":
    main()

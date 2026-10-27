"""Phase 05: robust API request handling, status messages and timeouts."""
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def status_message(code):
    messages = {
        200: "Success: request completed.",
        201: "Created: resource creation accepted.",
        400: "Bad request: check the request data.",
        401: "Unauthorized: valid authentication is required.",
        403: "Forbidden: access is not allowed.",
        404: "Resource not found.",
        429: "Rate limit exceeded: slow down and retry later.",
        500: "Internal server error: try again later.",
    }
    return messages.get(code, f"HTTP response: {code}")

def request_post(post_id=1):
    url = f"{BASE_URL}/posts/{post_id}"
    try:
        response = requests.get(url, timeout=10)
        print(f"Status Code: {response.status_code}")
        if response.ok:
            print(status_message(response.status_code))
            print(response.json())
        else:
            print("Request failed.")
            print(status_message(response.status_code))
    except requests.Timeout:
        print("Timeout: the API did not respond within 10 seconds.")
    except requests.ConnectionError:
        print("Network failure: could not connect to the API.")
    except requests.RequestException as exc:
        print(f"Request failure: {exc}")
    except ValueError:
        print("The response was not valid JSON.")

if __name__ == "__main__":
    # Use an invalid ID to demonstrate the 404 path.
    request_post(999999)

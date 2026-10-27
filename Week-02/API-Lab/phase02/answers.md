# Phase 02 — HTTP Requests, Responses & REST

## Task 04 — Analyze a URL

URL: `https://api.example.com/students/101`

| Item | Answer |
|---|---|
| Protocol | HTTPS |
| Host | `api.example.com` |
| Path | `/students/101` |
| Resource | `students` (student resource collection) |
| Resource identifier | `101` |

## Task 05 — REST API Operation Table

| Operation | HTTP method | Endpoint |
|---|---|---|
| Retrieve all students | GET | `/students` |
| Create a student | POST | `/students` |
| Retrieve student 101 | GET | `/students/101` |
| Update student 101 | PUT | `/students/101` |
| Delete student 101 | DELETE | `/students/101` |

Different HTTP methods communicate the intended operation: GET reads data, POST creates a resource, PUT replaces/updates a resource, and DELETE requests removal of a resource.

## Task 06 — Test GET Requests

| Endpoint | Method | Expected status | Response |
|---|---|---:|---|
| `https://jsonplaceholder.typicode.com/posts/1` | GET | 200 | JSON object for post 1 (`userId`, `id`, `title`, `body`) |
| `https://jsonplaceholder.typicode.com/posts/2` | GET | 200 | JSON object for post 2 |
| `https://jsonplaceholder.typicode.com/posts/3` | GET | 200 | JSON object for post 3 |

Run `python final_project/src/api_client.py get 1` (or use `phase03/api_client.py`) to see the live response and status. Save a screenshot of your actual terminal output as `evidence/task06.png`.

## Task 07 — Test POST

- **Method:** POST
- **Endpoint:** `https://jsonplaceholder.typicode.com/posts`
- **Request body:**
```json
{
  "title": "My API Lab",
  "body": "Testing POST request",
  "userId": 1
}
```
- **Expected status:** 201 Created
- **Response:** JSONPlaceholder typically returns the submitted fields plus a generated `id` (commonly `101`). This is a simulated API; it does not permanently save the post.

## Task 08 — Test PUT

- **Method:** PUT
- **Endpoint:** `https://jsonplaceholder.typicode.com/posts/1`
- **Example request body:**
```json
{
  "id": 1,
  "title": "Updated API Lab",
  "body": "This post was updated using PUT",
  "userId": 1
}
```
- **Expected status:** 200 OK
- **Response:** JSON representation of the submitted update. JSONPlaceholder simulates the update; it does not permanently modify its stored data.

## Task 09 — Test DELETE

- **Method:** DELETE
- **Endpoint:** `https://jsonplaceholder.typicode.com/posts/1`
- **Expected status:** 200 OK (JSONPlaceholder's typical response is an empty JSON object `{}`).
- **Purpose:** DELETE requests removal of the specified resource. JSONPlaceholder simulates deletion rather than permanently changing its dataset.

## Task 10 — HTTP Status Codes

| Status | Meaning | Example test |
|---|---|---|
| 200 | OK — request succeeded | GET `/posts/1` |
| 201 | Created — resource creation was accepted | POST `/posts` |
| 404 | Not Found — requested resource does not exist | GET `/posts/999999` |

A successful 2xx response means the server reports the request succeeded. A 404 response means the server could not find the requested resource.

# Phase 01 — API & Client-Server Fundamentals

## Task 01 — Explore an API Using a Browser

Open these endpoints in a browser:
- https://jsonplaceholder.typicode.com/posts/1
- https://jsonplaceholder.typicode.com/posts/2
- https://jsonplaceholder.typicode.com/posts/3

Each endpoint returns a JSON object with the fields `userId`, `id`, `title`, and `body`.
The exact title/body values are supplied by JSONPlaceholder and can be viewed at the endpoints above. The `id` is respectively 1, 2, and 3; the `userId` identifies the user who owns the post. Because this API is live, record the exact title/body text from the browser when taking your evidence screenshots.

**Why does the response change?** The final path segment is a resource identifier. `/posts/1`, `/posts/2`, and `/posts/3` request three different post records, so the returned JSON values differ.

**Evidence:** Take your own browser screenshots for each endpoint and save them as `evidence/task01.png`, `evidence/task01-post2.png`, and `evidence/task01-post3.png`. Screenshots are not fabricated or included in this solution.

## Task 02 — Identify the Client, API and Server

```text
[Browser / Client] -- GET /posts/1 --> [API endpoint on JSONPlaceholder server]
[Browser / Client] <-- HTTP 200 + JSON response -- [API endpoint / Server]
```

The browser is the client because it initiates the request. The API provides a defined interface for requesting post data. The server receives the HTTP request, finds the post with ID 1, and returns an HTTP response. The response contains a status code and a JSON body. The browser displays that JSON response.

## Task 03 — Identify API Resources

| Endpoint | Resource | Specific resource? |
|---|---|---|
| `/posts` | Collection of posts | No — collection endpoint |
| `/posts/1` | Post | Yes — post with ID 1 |
| `/posts/2` | Post | Yes — post with ID 2 |

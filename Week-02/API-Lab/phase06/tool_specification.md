# Phase 06 — Agent Tool Specification

## Task 24 — API Tool

- **Tool Name:** `get_post`
- **Description:** Retrieve one post from JSONPlaceholder using its numeric ID.
- **HTTP Method:** `GET`
- **Endpoint:** `https://jsonplaceholder.typicode.com/posts/{post_id}`
- **Required Inputs:** `post_id` (positive integer)
- **Optional Inputs:** request timeout (default 10 seconds)
- **Expected Output:** JSON object with `userId`, `id`, `title`, and `body`
- **Possible Errors:** 404 resource not found; 429 rate limit; 500 server error; timeout; network failure; invalid JSON
- **Authentication Required:** No for JSONPlaceholder

## Task 25 — Agent-oriented tool interface

**Tool:** `get_post`

**Purpose:** Retrieve a post by ID.

**Input schema:**
```json
{
  "post_id": {
    "type": "integer",
    "description": "ID of the post to retrieve",
    "minimum": 1
  }
}
```

**Output fields:** `id`, `userId`, `title`, `body`

**Possible errors:** 404, 429, 500, timeout, network/request failure.

The agent should validate `post_id`, call the tool with a timeout, return structured results, and avoid unbounded retries. No AI agent is built in this exercise; this file documents how an API operation could later be exposed as a tool.

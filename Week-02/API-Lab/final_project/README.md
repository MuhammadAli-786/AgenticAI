# Week 02 — API Lab

A beginner-friendly Python client that demonstrates API communication, HTTP methods, JSON processing, status-code handling, timeouts, safe configuration, and an agent-tool specification.

## Setup

Python 3.9+ recommended.

```bash
python -m venv .venv
# Linux/macOS:
source .venv/bin/activate
# Windows:
# .venv\Scripts\activate
pip install -r requirements.txt
```

If `requirements.txt` is in the project root, run commands from the `API-Lab` root.

## Commands

```bash
python final_project/src/api_client.py get 1
python final_project/src/api_client.py get 999999
python final_project/src/api_client.py list
python final_project/src/api_client.py create
python final_project/src/api_client.py update 1
python final_project/src/api_client.py delete 1
```

`JSONPlaceholder` is a demo API. POST/PUT/DELETE responses simulate changes; they do not persistently alter the dataset.

## Endpoint documentation

| Operation | Method | Endpoint | Inputs |
|---|---|---|---|
| Read one post | GET | `/posts/{post_id}` | positive integer `post_id` |
| Read all posts | GET | `/posts` | none |
| Create post | POST | `/posts` | JSON: `title`, `body`, `userId` |
| Update post | PUT | `/posts/{post_id}` | `post_id` plus JSON fields |
| Delete post | DELETE | `/posts/{post_id}` | `post_id` |

Base URL: `https://jsonplaceholder.typicode.com`

## Response structure

A post includes `userId` (owner), `id` (post identifier), `title` (title text), and `body` (post content).

## Error handling

The client uses a 10-second timeout and handles HTTP errors, 404, timeouts, connection failures, request exceptions, and invalid JSON. Status message mapping also documents 400, 401, 403, 429, and 500.

## Authentication and secrets

JSONPlaceholder does not require authentication. For protected APIs, read credentials from environment variables or a `.env` file and add `.env` to `.gitignore`. Never commit real credentials. See `phase04/.env.example`.

## How this can become an agent tool

`phase06/tool_specification.md` defines `get_post` with an input, output fields, and possible errors. An agent can call this tool when it needs a post, provided the system validates inputs, limits retries, and respects API rate limits.

## Evidence checklist

Take your own screenshots of live browser responses and terminal output, then save them in `evidence/`. Do not submit placeholder or fabricated screenshots.

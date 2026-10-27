# Phase 05 — Errors, Timeouts & Rate Limits

## Task 19 — Handle 404

Run `python phase05/api_client.py`. It requests `/posts/999999`, checks the response code, and prints a resource-not-found message without raising an unhandled exception.

Expected behavior:
```text
Status Code: 404
Request failed.
Resource not found.
```

## Task 20 — Different HTTP errors

The `status_message()` function maps 200, 201, 400, 401, 403, 404, 429 and 500 to distinct explanations. In brief: 2xx means success; 400 means invalid request; 401 means missing/invalid authentication; 404 means resource missing; 429 means too many requests; and 500 means server-side failure. The sample API does not necessarily produce every status on demand; the messages demonstrate how an API client should classify them.

## Task 21 — Timeout

A timeout prevents a program from waiting indefinitely when a server is slow or unreachable. The sample uses `timeout=10` and catches `requests.Timeout`.

## Task 22 — Network/API failures

The sample distinguishes successful HTTP responses, non-2xx API responses, timeouts, connection errors and other request failures. It handles invalid JSON separately.

## Task 23 — Rate limiting

1. **Rate limit:** a cap on how many requests a client may make in a time window.
2. **Why APIs use it:** to protect service capacity, prevent abuse, and share resources fairly.
3. **HTTP 429:** Too Many Requests; the client has exceeded a rate limit.
4. **Automated programs:** loops, retries, parallel workers, or bugs can send many requests quickly.
5. **Agentic systems:** an agent may call tools repeatedly or in loops; rate limits, bounded retries, backoff and request budgets help avoid overload and failed workflows.

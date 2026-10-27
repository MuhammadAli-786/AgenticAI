# Phase 04 — Authentication, API Keys & Secure Configuration

## Task 16 — Public vs Protected API

| Aspect | Public API | Protected API |
|---|---|---|
| Credentials | May not require credentials | Usually requires a key, token, or other authentication |
| Why authentication is used | Often open access with usage limits | Identifies/authorizes callers and protects data/resources |
| Example | JSONPlaceholder demo endpoint | API using `Authorization: Bearer <token>` |
| Invalid credentials | Not applicable if no credentials are required; access rules may still apply | Commonly returns 401 Unauthorized or 403 Forbidden |

## Task 17 — Authorization header

```python
headers = {"Authorization": "Bearer <TOKEN_PLACEHOLDER>"}
print({"Authorization": "Bearer <REDACTED>"})
```

Use a placeholder, never a real token in submitted code. The `phase04/api_client.py` file builds this header and masks secrets in printed output.

## Task 18 — .env configuration

1. Copy `.env.example` to `.env`.
2. Put your own API key in `.env` only if using an API that requires it.
3. Install dependencies: `pip install -r requirements.txt`.
4. Load it with `load_dotenv()` and `os.getenv("API_KEY")`.
5. Ensure `.env` is listed in `.gitignore` before committing.

JSONPlaceholder is public and does not require an API key, so the key is only a configuration demonstration here. Do not put a real key in GitHub or in screenshots.

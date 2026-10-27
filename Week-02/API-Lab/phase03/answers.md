# Phase 03 — JSON & Python API Integration

## Task 11 — JSON object and Python dictionary

JSON:
```json
{
  "name": "Ali",
  "marks": 85,
  "program": "BSCS"
}
```

Python:
```python
student = {
    "name": "Ali",
    "marks": 85,
    "program": "BSCS"
}
print(student["name"])
print(student["marks"])
print(student["program"])
```

Expected output:
```text
Ali
85
BSCS
```

## Task 12 — JSON array and Python list

```python
students = [
    {"id": 1, "name": "Ali"},
    {"id": 2, "name": "Sara"},
    {"id": 3, "name": "Ahmed"}
]
for student in students:
    print(f"ID: {student['id']}, Name: {student['name']}")
```

Expected output:
```text
ID: 1, Name: Ali
ID: 2, Name: Sara
ID: 3, Name: Ahmed
```

## Task 13 — First API client

Run `python phase03/api_client.py`. It sends GET `/posts/1`, prints the status, post ID, title and body, and handles common request failures.

## Task 14 — Multiple records

Run `python phase03/multiple_posts.py`. It loops through IDs 1, 2 and 3 and prints each post title.

## Task 15 — Collection

Run `python phase03/posts_collection.py`. It reports the count returned by the API (JSONPlaceholder typically has 100 posts) and prints the first five titles.

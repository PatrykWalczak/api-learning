import httpx

r = httpx.get("https://jsonplaceholder.typicode.com/posts/1")
print(r.status_code)
print(r.json()["title"])
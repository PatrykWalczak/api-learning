import httpx 

r = httpx.post("https://jsonplaceholder.typicode.com/posts", json= {"title": "test tytul", "body": "test body", "userId": 1})
print(r.status_code)
print(r.json())
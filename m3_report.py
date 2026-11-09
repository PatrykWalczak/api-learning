import httpx
import time
import json
import csv

posts = []
page = 1
try:
    while True:
        url = f"https://jsonplaceholder.typicode.com/posts"
        params = {"_page": page, "_limit": 10}
        r = httpx.get(url, params=params, timeout=5.0)
        r.raise_for_status()
        data = r.json()
        if not data:
            break
        posts.extend(data)
        page += 1
    with open("posts.json", "w", encoding="utf-8") as f:
        json.dump(posts, f, ensure_ascii=False, indent=2)
        
    with open ("posts.csv", "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["userId", "id", "title"], extrasaction="ignore")
            writer.writeheader()
            writer.writerows(posts)

    print(f"Zapisano {len(posts)} rekordów")
except httpx.HTTPStatusError as exc:
    print("Zły status: ", exc.response.status_code)
except httpx.RequestError:
    print("Problem z połączeniem lub timeout")
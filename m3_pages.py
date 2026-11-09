import httpx

wszystkie = []
strona = 1
try:
    while True:
        r = httpx.get(f"https://jsonplaceholder.typicode.com/posts", params={"_page": strona, "_limit": 10}, timeout=5.0)
        r.raise_for_status()
        if not r.json():
            break
        wszystkie += r.json()
        strona += 1
except httpx.HTTPStatusError as exc:
    print("Zły status: ", exc.response.status_code)
except httpx.RequestError:
    print("Problem z połączeniem lub timeout")

print(len(wszystkie))
        
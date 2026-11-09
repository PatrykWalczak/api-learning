import httpx 




try:
    url = "https://jsonplaceholder.typicode.com/posts/99999"
    r = httpx.get(url, timeout=5.0)
    r.raise_for_status()
except httpx.HTTPStatusError as exc:
    print("Zły status: ", exc.response.status_code)
except httpx.RequestError:
    print("Problem z połączeniem lub timeout")
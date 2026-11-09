import httpx
import time 

for i in range(3):
    to_wait = 2 ** i
    r = httpx.get("https://httpbin.org/status/503", timeout=5.0)
    if r.status_code == 200:
        break
    
    print(f"Próba {i+1}: Status code: {r.status_code}, czekam {to_wait} sekund przed kolejną próbą...")
    time.sleep(to_wait)
print("Ostateczny status code: ", r.status_code)
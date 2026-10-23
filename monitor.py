
import time
import requests

url = "https://www.google.com"

print(f"Checking website: {url}")

start_time = time.perf_counter()

try:
    response = requests.get(url, timeout=10)
    response_time = time.perf_counter() - start_time

    print(f"HTTP status: {response.status_code}")
    print(f"Response time: {response_time:.2f} seconds")

    if 200 <= response.status_code < 400:
        print("Website is UP")
    else:
        print("Website returned an error status")

except requests.exceptions.RequestException as error:
    print(f"Website check failed: {error}")

import requests
url = "http://www.google.com/"
response = requests.get(url)

print(f"your request to {url} come back w/ status code {response.status_code}")
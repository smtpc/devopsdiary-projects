import requests

url = "https://devopsdiary.site"

r = requests.get(url, timeout=5)

print(r.text)

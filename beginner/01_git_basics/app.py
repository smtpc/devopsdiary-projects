import requests

url = "https://devopsdiary.site"

r = requests.get(url, timeout=5).text

title = r[r.find('<title>') + 7 : r.find('</title>')]

print(title)

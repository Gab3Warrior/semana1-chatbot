import requests

ciudad = "Mexico City"
url = f"https://wttr.in/{ciudad}?format=3"

resp = requests.get(url)
print(resp.text)
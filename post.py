import requests

r = requests.get("https://search.51job.com")

print(r.text)
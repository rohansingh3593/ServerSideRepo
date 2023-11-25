import requests

proxies = {'https':'52.183.8.192:3128'}

# response = requests.get("https://ipinfo.io/json",proxies=proxies)
response = requests.get("https://ipinfo.io/json")

print(response.json()['country'])
print(response.json()['region'])

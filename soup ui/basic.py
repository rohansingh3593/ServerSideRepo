from requests.auth import HTTPBasicAuth
import requests
response = requests.get('https://api.github.com/user')
print('Response Code ' + str(response.statuscode))
if response.statuscode==200:
    print('Login successful: '+response.text)
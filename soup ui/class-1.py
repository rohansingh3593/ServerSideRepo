import requests
import xml.etree.ElementTree as ET
from base64 import b64encode

url = "https://caas.itron-systeam02-install.eng.ssnsgs.net:6343/"

url = "https://caas.itron-systeam02-install.eng.ssnsgs.net:6343/?WSDL"
# url = 'https://mt.itron-systeam02-install.eng.ssnsgs.net:3010/amm/home/daily?WSDL.'
# http://<hostname>:<port>/<webappname>/<servletEndpoint>?wsdl

url ='https://mt.itron-systeam02-install.eng.ssnsgs.net:3009/amm/webservice/v2_7_1/SystemInfoPort'
def basic_auth(username, password):
    token = b64encode(f"{username}: {password}".encode('utf-8')).decode("ascii")
    return f'Basic {token}'

SOAPEnvelope ='''
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:urn="urn:com:ssn:schema:service:v2.7.1:SystemInfo.xsd">
   <soapenv:Header/>
   <soapenv:Body>
      <urn:GetUIQVersion/>
   </soapenv:Body>
</soapenv:Envelope>'''

username = "aman.srivastava"
password = "Welcome@123"

options = {'Authentication' : basic_auth(username, password),"Content-Type": "text/xml; charset=utf-8"}  


response = requests.post(url, data = SOAPEnvelope, headers = options)
print(response.text)





response =  requests.get(url)
if response.status_code == 200:
    print(url + ' is 1 good! !')
    zipJson = response.json()
    print(zipJson)
else:
    print(url + ' is bad')
    print('Error code ' + str (response.status_code))
    exit(response.status_code)

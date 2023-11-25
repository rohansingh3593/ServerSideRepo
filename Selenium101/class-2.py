import requests
import xml.etree.ElementTree as ET
url = "https://caas.itron-systeam02-install.eng.ssnsgs.net:6343/"

url = "https://caas.itron-systeam02-install.eng.ssnsgs.net:6343/?WSDL"
# url = 'https://mt.itron-systeam02-install.eng.ssnsgs.net:3010/amm/home/daily?WSDL.'
# http://<hostname>:<port>/<webappname>/<servletEndpoint>?wsdl

SOAPEnvelope ='''
<soapenv:Envelope
xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
<soapenv:Body>
<s0:FindDevice xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xmlns:xs="http://www.w3.org/2001/XMLSchema"
xmlns:s0="urn:com:ssn:schema:service:DeviceManager.xsd">
<s0:CommonAttributes>
<s0:UtilDeviceID>NP-EO-METER-14</s0:UtilDeviceID>
</s0:CommonAttributes>
<s0:StartRow>1</s0:StartRow>
<s0:EndRow>2</s0:EndRow>
</s0:FindDevice>
</soapenv:Body>
</soapenv:Envelope>'''

options = {"Content-Type": "text/xml; charset=utf-8"}      
# response = requests.post(url, data = SOAPEnvelope, headers = options)
response = requests.post(url, headers = options)
print(response.text)

# root = ET.fromstring(response.text)
# for child in root.iter('*'):
#     print(child)


# response =  requests.get(url)
# if response.status_code == 200:
#     print(url + ' is 1 good! !')
#     zipJson = response.json()
#     print(zipJson)
# else:
#     print(url + ' is bad')
#     print('Error code ' + str (response.status_code))
#     exit(response.status_code)

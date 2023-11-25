import requests
# from requests_ntlm import HttpNtlmAuth
from requests import Session
from requests.auth import HTTPBasicAuth
import os

name = 'DeviceManager'
port_name = name + 'Port'
port = 3009

####################################################
username = "mohit_taneja"
password = "Crosslynx@12"
# username = "aman.srivastava"
# password = "Welcome@123"
####################################################
os.environ['UIQUSER'] = username
os.environ['UIQPSWD'] = password
os.environ['WSDL_REPO'] = 'localhost:8080'
os.environ['UIQAMMWSHOST'] = 'mt.itron-systeam02-install.eng.ssnsgs.net'

# print(os.getenv)
# print(os.environ['UIQUSER'])
# print(os.environ['UIQPSWD'])
# print(os.environ['WSDL_REPO'])
# print(os.environ['UIQAMMWSHOST'])
# ####################################################

username = "aman.srivastava"
password = "Welcome@123"

username = "mohit_taneja"
password = "Crosslynx@12"

# WSDL_URL = 'https://mt.itron-systeam02-install.eng.ssnsgs.net:3009/amm/webservice/v2_7/SystemInfoPort?WSDL'

# Replace these with your actual SOAP service URL and credentials


# SOAP request payload
soap_request = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:urn="urn:com:ssn:schema:service:v2.7:SystemInfo.xsd">
   <soapenv:Header/>
   <soapenv:Body>
      <urn:GetVersion/>
   </soapenv:Body>
</soapenv:Envelope>
"""

# Set SOAP headers
headers = {
    "Content-Type": "text/xml; charset=utf-8",
}

WSDL_URL = "https://" + os.environ['UIQAMMWSHOST'] + f":{port}/amm/webservice/2_7_1/{port_name}"

# session = Session()
# session.auth = HTTPBasicAuth(os.environ['UIQUSER'], os.environ['UIQPSWD'])
# session.trust_env = False

# session = requests.Session()
# session.auth = HttpNtlmAuth(username, password)
# # session.auth = requests.auth.HTTPDigestAuth(username, password)



session = Session()
session.auth = HTTPBasicAuth(os.environ['UIQUSER'], os.environ['UIQPSWD'])
session.trust_env = False




# Make the SOAP request
# response = session.get(WSDL_URL, data=soap_request, headers=headers)
response = requests.get(WSDL_URL,auth=session)
# print(response.content)

# Check the response
if response.status_code == 200:
    # Process the SOAP response here
    print(response.content)
else:
    print("Error:", response.status_code, response.text)
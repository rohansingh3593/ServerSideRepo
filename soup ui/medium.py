from zeep import Client
from zeep.transports import Transport
from requests import Session
from requests.auth import HTTPBasicAuth

url = 'https://mt.itron-systeam02-install.eng.ssnsgs.net:3009/amm/webservice/v2_7/SystemInfoPort'
# url = 'C:\Users\Crosslynx29\Desktop\vgs\files\wsdls\wsdls\2.7.1'
wsdl = url + '?WSDL'




# client = Client(wsdl)

# session = Session()
# session.auth = HTTPBasicAuth('aman.srivastava', 'Welcome@123')
# client=Client(wsdl,transport=Transport(session=session))

# print(client)
# print(client.__dir__)



from zeep import Client,Settings
from requests import Session
from requests.auth import HTTPBasicAuth
from zeep.transports import Transport
from base64 import b64encode

username = "aman.srivastava"
password = "Welcome@123"



def basic_auth(username, password):
    token = b64encode(f"{username}: {password}".encode('utf-8')).decode("ascii")
    return f'Basic {token}'




session = Session()
settings = Settings(extra_http_headers={'Authentication' : basic_auth(username, password)}) 
client = Client(wsdl=wsdl, settings=settings)


# session.auth = HTTPBasicAuth(username, password)
client = Client(wsdl, transport=Transport(session=session),settings=settings)
  
# resp = client.service.Payload()    
# print(resp.status_code) 


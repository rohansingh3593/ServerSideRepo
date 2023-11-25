# serviceInfo = WebServices.CreateWebServiceInfoFromItem("SampleWebService")


# url = 'file:///C:/Users/Crosslynx29/Desktop/vgs/files/wsdls/wsdls/2.7/SystemInfo.wsdl'
# url = 'https://mt.itron-systeam02-install.eng.ssnsgs.net:3009/amm/webservice/v2_7/SystemInfoPort'
url = 'http://mt.itron-systeam02-install.eng.ssnsgs.net:3009/amm/webservice/v2_7/SystemInfoPort.wsdl'

from zeep import Client
from requests import Session
from requests.auth import HTTPBasicAuth
from zeep.transports import Transport
from zeep.wsse.username import UsernameToken

# url = "https://WSDL URL"    
# username = "username"
# password = "password"
client = Client(url,wsse=UsernameToken('aman.srivastava', 'Welcome@123'))

session = Session()
# session.auth = HTTPBasicAuth('aman.srivastava', 'Welcome@123')
# client = Client(url, transport=Transport(session=session))
  
# resp = client.service.Payload()    
# print(resp.status_code)  
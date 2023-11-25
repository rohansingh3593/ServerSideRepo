


username = "aman.srivastava"
password = "Welcome@123"

username = "mohit_taneja"
password = "Crosslynx@12"

WSDL_URL = 'https://mt.itron-systeam02-install.eng.ssnsgs.net:3009/amm/webservice/v2_7/SystemInfoPort?wsdl'

from suds.client import Client

# client = Client(WSDL_URL,
#                 username=username,
#                 password=password)
# print('CLIENT INITIALIZED') # <-- This print command is executed
# result = client.service.getCopyrightYear()

# print(result)

# from requests.auth import HTTPBasicAuth  # or HTTPDigestAuth, or OAuth1, etc.
# from requests import Session
# from zeep import Client
# from zeep.transports import Transport


# session = Session()
# session.auth = HTTPBasicAuth(username, password)
# client = Client(WSDL_URL)
# client = Client(WSDL_URL,transport=Transport(session=session))
print('CLIENT INITIALIZED') # <-- This print command is executed

# from requests import Session
# from zeep import Client
# from zeep.transports import Transport

# # session = Session()

# # # session.verify = 'path/to/my/certificate.pem'
# # session.verify = False

# # transport = Transport(timeout=10)
# # client = Client(
# #     WSDL_URL,
# #     transport=transport)
# from base64 import b64encode

# def basic_auth(username, password):
#     token = b64encode(f"{username}: {password}".encode('utf-8')).decode("ascii")
#     return f'Basic {token}'

# # options = {'Authentication' : basic_auth(username, password),"Content-Type": "text/xml; charset=utf-8"}  

# session = Session()
# session.headers['Authorization'] = basic_auth(username, password)
# transport = Transport(session=session)
# client = Client(wsdl=WSDL_URL,transport=transport)

import requests
from suds.transport.http import HttpAuthenticated
from suds.transport import Reply, TransportError

class RequestsTransport(HttpAuthenticated):
    def __init__(self, **kwargs):
        self.cert = kwargs.pop('cert', None)
        HttpAuthenticated.__init__(self, **kwargs)

    def send(self, request):
        self.addcredentials(request)
        resp = requests.post(request.url, data=request.message,
                             headers=request.headers, cert=self.cert, verify=False)
        result = Reply(resp.status_code, resp.headers, resp.content)
        return result

t = RequestsTransport(cert='/path/to/mycertificate.pem')
headers = {"Content-Type" : "text/xml;charset=UTF-8", "SOAPAction" : ""}
client = Client(WSDL_URL,headers=headers,transport=t)
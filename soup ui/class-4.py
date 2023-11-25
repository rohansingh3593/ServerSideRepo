

url ='http://mt.itron-systeam02-install.eng.ssnsgs.net:3009/amm/'

from zeep import Client
from zeep.wsse.username import UsernameToken
import time

# url = 'http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL'
# url ='http://mt.itron-systeam02-install.eng.ssnsgs.net:3009?WSDL'

# url = 'https://mt.itron-systeam02-install.eng.ssnsgs.net:3009/amm/webservice/v2_7/SystemInfoPort'

# WSDL_url = url + '?WSDL'
# # client = Client(wsdl = url)
# # result = client.service.ListOfCountryNamesGroupedByContinent()
# # print(result)

# client = Client(WSDL_url,wsse=UsernameToken('aman.srivastava', 'Welcome@123'))

# time_out=time.time() + 5*60
# while time_out>time.time():
#     try:
#         pass
#     except:
#         pass

    # time.sleep(2)


from zeep import Client
# from zeep.wsse.signature import Signature
from zeep.transports import Transport
# from requests import Session
# session = Session()
# session.cert = '/path/to/ssl.pem'
# transport = Transport(session=session)
# client = Client('http://www.webservicex.net/ConvertSpeed.asmx?WSDL',transport=transport)

url = 'https://mt.itron-systeam02-install.eng.ssnsgs.net:3009/amm/webservice/v2_7/SystemInfoPort'

import requests
session = requests.session()
session.trust_env = False
client_location = url + '?wsdl'
transport = Transport(session=session)
client = Client(wsdl=client_location, wsse=UsernameToken('aman.srivastava', 'Welcome@123', use_digest=True), transport=transport)





# session = requests.session()
# session.auth = requests.auth.HTTPDigestAuth('aman.srivastava', 'Welcome@123')
# client = Client(wsdl=url + "?wsdl",transport=Transport(session=session))
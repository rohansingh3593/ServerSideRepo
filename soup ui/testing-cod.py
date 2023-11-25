# from zeep import Client
# from zeep.wsse.signature import Signature
# client = Client(
# 'http://www.webservicex.net/ConvertSpeed.asmx?WSDL',
# wsse=Signature(private_key_filename, public_key_filename,optional_password))



# --------------------------------------------------------------------------------

# import datetime
# from zeep import Client
# from zeep.wsse.username import UsernameToken
# from zeep.wsse.utils import WSU
# from zeep.plugins import HistoryPlugin
# from lxml import etree

# def print_history(h):
#     print(etree.tostring(h.last_sent["envelope"], encoding = "unicode", pretty_print = True))
#     print(etree.tostring(h.last_received["envelope"], encoding = "unicode", pretty_print = True))

# timestamp_token = WSU.Timestamp()
# today_datetime = datetime.datetime.today()
# expires_datetime = today_datetime + datetime.timedelta(minutes = 10)

# timestamp_elements = [
#     WSU.Created(today_datetime.strftime("%Y-%m-%dT%H:%M:%SZ")),
#     WSU.Expires(expires_datetime.strftime("%Y-%m-%dT%H:%M:%SZ"))
# ]

# timestamp_token.extend(timestamp_elements)
# user_name_token = UsernameToken('aman.srivastava', 'Welcome@123', timestamp_token = timestamp_token)

# history = HistoryPlugin()
# client = Client(
#      'file:///C:/Users/Crosslynx29/Desktop/vgs/files/wsdls/wsdls/2.7/SystemInfo.wsdl', 
#      wsse = user_name_token,
#      plugins = [history]
# )
# print(client)
# response = client.service.getUIQVersion()

# # print_history(history)

##333####################################################################################################

# python -mzeep https://mt.itron-systeam02-install.eng.ssnsgs.net:3009/amm/webservice/v2_7/SystemInfoPort.WSDL

import datetime
from zeep import Client
from zeep.wsse.username import UsernameToken
from zeep.wsse.utils import WSU
timestamp_token = WSU.Timestamp()
today_datetime = datetime.datetime.today()
expires_datetime = today_datetime + datetime.timedelta(minutes=10)
timestamp_elements = [WSU.Created(today_datetime.strftime("%Y-%m-%dT%H:%M:%SZ")),
                      WSU.Expires(expires_datetime.strftime("%Y-%m-%dT%H:%M:%SZ"))]
timestamp_token.extend(timestamp_elements)
user_name_token = UsernameToken('username', 'password', timestamp_token=timestamp_token)
client = Client(
     'https://mt.itron-systeam02-install.eng.ssnsgs.net:3009/amm/webservice/v2_7/SystemInfoPort.WSDL', 
    wsse=user_name_token)

print(client)
response = client.service

print(dir(response))
print(response.getCopyrightYear())



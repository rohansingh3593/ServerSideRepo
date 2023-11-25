#!/bin/python
#The purpose of this script is reading the wsdl file 
#creating requesting dictionary data
#calling service with request data
#printing the response

import sys
import os
from requests import Session
from requests.auth import HTTPBasicAuth
from zeep import Client
from zeep.transports import Transport
from zeep import xsd

# python3 -m pip install zeep
# python3 -m zeep <wsdl url>

username = "mohit_taneja"
password = "Crosslynx@12"


directory = os.path.dirname(__file__)
print(directory)
###########################################################
name = 'DeviceManager'
port_name = name + 'Port'
port = 3009

os.environ['UIQUSER'] = username
os.environ['UIQPSWD'] = password
# os.environ['WSDL_REPO'] = 'localhost:8080'
os.environ['UIQAMMWSHOST'] = 'mt.itron-systeam02-install.eng.ssnsgs.net'

# print(os.getenv)
# print(os.environ['UIQUSER'])
# print(os.environ['UIQPSWD'])
# print(os.environ['WSDL_REPO'])
# print(os.environ['UIQAMMWSHOST'])
# # ####################################################

session = Session()
session.auth = HTTPBasicAuth(os.environ['UIQUSER'], os.environ['UIQPSWD'])
session.trust_env = False

roh_sys_wsdl = 'file:///C:/Users/Crosslynx29/Desktop/vgs/files/wsdls/amm/2_7_1/DeviceManager.wsdl'
roh_sys_client = Client(roh_sys_wsdl, transport=Transport(session=session))

# print("https://" + os.environ['UIQAMMWSHOST'] + f":3009/amm/webservice/2_7_1/{port_name}")
# roh_sys_client.service._binding_options["address"] = "https://" + os.environ['UIQAMMWSHOST'] + f":{port}/amm/webservice/2_7_1/{port_name}"
# request_data={
#     'SearchParameters':{
#         'CommonAttributes':{
#             # 'Name':sys.argv[1],
#             'Name':'RA',

#         },
#     },
#     'NumberRows':'100',
# }

# res= roh_sys_client.service.FindDevice(**request_data)
# print("response="),
# print(res)



print(roh_sys_client._get_all_operations)

# roh_sys_client.service._get_operation_by_name

# roh_sys_client.service._get_binding_infos

# roh_sys_client.service._get_fault_types
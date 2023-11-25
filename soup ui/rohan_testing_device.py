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
name = 'DeviceManager'
port_name = name + 'Port'
port = 3009

latest_version = '2.7.1'
latest_version = latest_version.replace('.','_')
print(latest_version)
session = Session()
session.auth = HTTPBasicAuth(os.environ['UIQUSER'], os.environ['UIQPSWD'])
session.trust_env = False

roh_sys_wsdl = f'file:///C:/Users/Crosslynx29/Desktop/vgs/files/wsdls/wsdls/2.7.1/{name}.wsdl'
roh_sys_client = Client(roh_sys_wsdl, transport=Transport(session=session))
roh_sys_client.service._binding_options["address"] = "https://" + os.environ['UIQAMMWSHOST'] + f":{port}/amm/webservice/v{latest_version}/{port_name}"

full_list = roh_sys_client.service
print("Operation :", full_list)

full_list = roh_sys_client.service.__dir__()
print("Operation :", full_list)

print(roh_sys_client.service.GetMeterTypeConfigs())


print(roh_sys_client.service.GetDeviceStateHistory())
import requests
# from requests_ntlm import HttpNtlmAuth
from requests import Session
from requests.auth import HTTPBasicAuth
import os


name = 'SystemInfo'
port_name = name + 'Port'
port = 3009
####################################################
username = "mohit_taneja"
password = "Crosslynx@12"
# username = "aman.srivastava"
# password = "Welcome@123"
####################################################
roh_wsdl = "https://" + 'mt.itron-systeam02-install.eng.ssnsgs.net' + ":3009/amm/webservice/v2_7_1/SystemInfoPort"

roh_wsdl = requests.get(roh_wsdl ,verify=False, auth = (username,password))

print(roh_wsdl.content)

 

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

# username = "aman.srivastava"
# password = "Welcome@123"
username = "mohit_taneja"
password = "Crosslynx@12"

####################################################
os.environ['UIQUSER'] = username
os.environ['UIQPSWD'] = password
os.environ['WSDL_REPO'] = 'localhost:8080'
os.environ['UIQAMMWSHOST'] = 'mt.itron-systeam02-install.eng.ssnsgs.net'

# print(os.getenv)
print(os.environ['UIQUSER'])
print(os.environ['UIQPSWD'])
print(os.environ['WSDL_REPO'])
print(os.environ['UIQAMMWSHOST'])
# ####################################################

session = Session()
session.auth = HTTPBasicAuth(os.environ['UIQUSER'], os.environ['UIQPSWD'])
session.trust_env = False


# # wsdl file path
# DevMgrwsdl = os.environ['WSDL_REPO']+"/amm/2_10/DeviceManager.wsdl"
# DevResultswsdl = os.environ['WSDL_REPO']+"/amm/2_10/DeviceResults.wsdl"
# JobMgrwsdl = os.environ['WSDL_REPO']+"/amm/2_10/JobManager.wsdl"
# JobResultswsdl = os.environ['WSDL_REPO']+"/amm/2_10/JobResults.wsdl"

#############################################################
# wsdl file path Modified
# DevMgrwsdl = 'file:///C:/Users/Crosslynx29/Desktop/vgs/files/wsdls/wsdls/2.7.1/DeviceManager.wsdl'
# DevResultswsdl = 'file:///C:/Users/Crosslynx29/Desktop/vgs/files/wsdls/wsdls/2.7.1/DeviceResults.wsdl'
# JobMgrwsdl = 'file:///C:/Users/Crosslynx29/Desktop/vgs/files/wsdls/wsdls/2.7.1/JobManager.wsdl'
# JobResultswsdl = 'file:///C:/Users/Crosslynx29/Desktop/vgs/files/wsdls/wsdls/2.7.1/JobResults.wsdl'
#############################################################

# https://localhost:8080/amm/webservice/v2_7_1/SystemInfoPort
# DevMgrwsdl = os.environ['WSDL_REPO']+"/amm/2_10/DeviceManager.wsdl"
# DevResultswsdl = os.environ['WSDL_REPO']+"/amm/2_10/DeviceResults.wsdl"
# JobMgrwsdl = os.environ['WSDL_REPO']+"/amm/2_10/JobManager.wsdl"
# JobResultswsdl = os.environ['WSDL_REPO']+"/amm/2_10/JobResults.wsdl"

###################################################################################
roh_sys_wsdl = 'file:///C:/Users/Crosslynx29/Desktop/vgs/files/wsdls/wsdls/2.7.1/SystemInfo.wsdl'
roh_sys_client = Client(roh_sys_wsdl, transport=Transport(session=session))
roh_sys_client.service._binding_options["address"] = "https://" + os.environ['UIQAMMWSHOST'] + ":3009/amm/webservice/v2_7_1/SystemInfoPort"
print("Operation :", roh_sys_client.service.getVersion())
###################################################################################

# DevMgrclient = Client(DevMgrwsdl, transport=Transport(session=session))
# DevResultsclient = Client(DevResultswsdl, transport=Transport(session=session))
# JobMgrclient = Client(JobMgrwsdl, transport=Transport(session=session))
# JobResultsclient = Client(JobResultswsdl, transport=Transport(session=session))


#wsdl file consist some default properties . Overriding some of it
#DevMgrclient.service._binding_options["address"] = "https://" + os.environ['UIQHOST'] + ":3009/amm/webservice/v2.8/DeviceManagerPort"
#DevResultsclient.service._binding_options["address"] = "https://" + os.environ['UIQHOST'] + ":3009/amm/webservice/v2.8/DeviceResults"
#JobMgrclient.service._binding_options["address"] = "https://" + os.environ['UIQHOST'] + ":3009/amm/webservice/v2.8/JobManagerPort"
#JobResultsclient.service._binding_options["address"] = "https://" + os.environ['UIQHOST'] + ":3009/amm/webservice/v2.8/JobResultsPort"

#workaround due to SSL error in updraded AMM. Need to be removed and changes above need to be uncommented after the problem
#is fixed on UIQ server
# DevMgrclient.service._binding_options["address"] = "https://" + os.environ['UIQAMMWSHOST'] + ":3009/amm/webservice/v2.10/DeviceManagerPort"
# DevResultsclient.service._binding_options["address"] = "https://" + os.environ['UIQAMMWSHOST'] + ":3009/amm/webservice/v2.10/DeviceResults"
# JobMgrclient.service._binding_options["address"] = "https://" + os.environ['UIQAMMWSHOST'] + ":3009/amm/webservice/v2.10/JobManagerPort"
# JobResultsclient.service._binding_options["address"] = "https://" + os.environ['UIQAMMWSHOST'] + ":3009/amm/webservice/v2.10/JobResultsPort"

# operation=sys.argv[1]
# print(operation)

print("This is the name of the program:", sys.argv[0])
print("Argument List:", str(sys.argv))


# if operation == "AddNote":
#     request_data={
#         'MacID':sys.argv[2],
#         'Note':sys.argv[3],
#     }
#     #calling AddNote service 
#     res= DevMgrclient.service.AddNote(**request_data)    

# elif operation == "FindDevice":
#     request_data={
#         'SearchParameters':{
#                 'CommonAttributes':{
#                     'Name':sys.argv[2],
#                 },
#         },
#         'NumberRows':sys.argv[3],
#     }
#     #calling FindDevice service
#     res= DevMgrclient.service.FindDevice(**request_data)

# elif operation == "AddMeterReadJob":
#     request_data={
#             'JobInfo':{
#                 'Name':sys.argv[2],
#              },
#              'MeterReadJob':{
#                  'DeviceMacID':sys.argv[3],
#                  'MeterReadType':'JOB_OP_LP_READ',
#                  'NumberRetries':sys.argv[4],
#                  'Priority':'JOB_PRIORITY_HIGH',
#                  'OneTimeIntervalParameters':{
#                      'SinceLastReadPoint':'true',
#                  },
#              },
#             'Schedule':{
#                 'Immediate':xsd.Nil,
#              },   
#             'AutoActivate':'true',
#     }
#     #calling AddMeterReadJob service
#     res= JobMgrclient.service.addMeterReadJob(**request_data)
#     print("My JobID="),

# elif operation == "GetJobStatus":
#     request_data={
#             'JobID': sys.argv[2],
#     }
#     res= JobMgrclient.service.getJobStatus(**request_data)

# elif operation == "getMeterReadResultsByDeviceID":
#     print ("Get Meter ReadResults By DeviceID called")
#     request_data={
#         'SearchParameters':{
#             'DeviceMacID':sys.argv[2],
#             'FromTime':sys.argv[3],
#             'ToTime':sys.argv[4],
#             'MeterDataType':'METER_DATA_TYPE_INTERVAL',
#             'LPSetId':sys.argv[5],
#         },
#         'NumberRows':'100',
#     }
#     #calling IntervalRead service
#     res = DevResultsclient.service.getMeterReadResultsByDeviceID(**request_data)

# print(res)

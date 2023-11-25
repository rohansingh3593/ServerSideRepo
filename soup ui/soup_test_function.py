from zeep import Client
import operator
import os

# read in wsdl mode
# roh_sys_wsdl = f'file:///C:/Users/Crosslynx29/Desktop/vgs/files/wsdls/amm/2_10/DeviceManager.wsdl'

# Noraml mode
# roh_sys_wsdl = f'/Users/Crosslynx29/Desktop/vgs/files/wsdls/amm/2_10/JobManager.wsdl'
# roh_sys_wsdl = f'/Users/Crosslynx29/Desktop/vgs/files/wsdls/amm/2_10/JobResults.wsdl'
# roh_sys_wsdl = f'/Users/Crosslynx29/Desktop/vgs/files/wsdls/amm/2_10/SystemInfo.wsdl'
# roh_sys_wsdl = f'/Users/Crosslynx29/Desktop/vgs/files/wsdls/amm/2_10/DataAggregation.wsdl'
# roh_sys_wsdl = f'/Users/Crosslynx29/Desktop/vgs/files/wsdls/amm/2_10/DeviceManager.wsdl'
# roh_sys_wsdl = f'/Users/Crosslynx29/Desktop/vgs/files/wsdls/amm/2_10/EventManager.wsdl'
# roh_sys_wsdl = f'/Users/Crosslynx29/Desktop/vgs/files/wsdls/amm/2_10/GroupManager.wsdl'
# roh_sys_wsdl = f'/Users/Crosslynx29/Desktop/vgs/files/wsdls/amm/2_10/Route.wsdl'
# roh_sys_wsdl = f'/Users/Crosslynx29/Desktop/vgs/files/wsdls/amm/2_10/SystemInfo.wsdl'

print(os.path.dirname(__file__))
path = '/Users/Crosslynx29/Desktop/vgs/files/wsdls/amm/2_10'


list1 = os.listdir(path)
wsdl_list1 = [i for i in list1 if i.endswith('.wsdl')]
print(wsdl_list1)

for wsdl in wsdl_list1:
    roh_sys_wsdl = 'file:///C:' + path + '/' + wsdl
    print(roh_sys_wsdl)

    client = Client(roh_sys_wsdl)
    for service in client.wsdl.services.values():
        for port in service.ports.values():
            operations = sorted(port.binding._operations.values(),key=operator.attrgetter('name'))
            for operation in operations:
                print("Method :", operation.name)
                print(" Input :", operation.input.signature())
                print("#"*30)
    print("#"*90)


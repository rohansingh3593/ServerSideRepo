from zeep import Client
import operator

# wsdl = 'file:///C:/Users/Crosslynx29/Desktop/vgs/files/wsdls/wsdls/2.7.1/SystemInfo.wsdl'
wsdl = 'file:///C:/Users/Crosslynx29/Desktop/vgs/files/wsdls/amm/2_10/DeviceManager.wsdl'
client = Client(wsdl)

# print(dir(client))
# print(client.__doc__)

print("#"*30)
'''
['__annotations__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', 
'__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__',
 '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 
 '_default_port_name', '_default_service', '_default_service_name', '_default_soapheaders', '_default_transport', '_get_port',
   '_get_service', 'bind', 'create_message', 'create_service', 'get_element', 'get_type', 'namespaces', 'plugins', 'service',
     'set_default_soapheaders', 'set_ns_prefix', 'settings', 'transport', 'type_factory', 'wsdl', 'wsse'] 

'''
# print(dir(client.wsdl))
# print(client.wsdl.__doc__)

# print("#"*30)
'''
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', 
'__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', 
'__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_add_definition', '_definitions', '_get_xml_document', 'bindings', 'dump', 
'load', 'location', 'messages', 'port_types', 'services', 'settings', 'transport', 'types']
'''
# print(dir(client.service))

# print("#"*30)

'''
['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__gt__',
'__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', 
'__self__', '__self_class__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__thisclass__', 'getCopyrightYear',
 'getUIQVersion', 'getVersion']
'''

# client._get_port(client.wsdl.service,'SystemInfoPort')

# print(client.wsdl.services.values())
# odict_values([<Service(name='SystemInfoService', ports=OrderedDict([('SystemInfoPort', <Port(name='SystemInfoPort', binding=<Soap11Binding(name='{urn:com:ssn:schema:service:v2.7.1:SystemInfo}SystemInfoSoapBinding', port_type=<PortType(name='{urn:com:ssn:schema:service:v2.7.1:SystemInfo}SystemInfoPortType')>)>, {'address': 'https://localhost:8080/amm/webservice/v2_7_1/SystemInfoPort'})>)]))>])

# print(type(client.wsdl.services.values()))

# get each operation signature
for service in client.wsdl.services.values():

    # print("Full Service:", service)
    # print("#"*30)
    # print( service.name)
    # print(type(service.name))

    # print("#"*30)
    # print("Port:", service.ports)
    # print("Port:", type(service.ports))

    print("#"*30)
    # print(service.ports.values())
    # ([<Port(name='SystemInfoPort', 
    #         binding=<Soap11Binding(name='{urn:com:ssn:schema:service:v2.7.1:SystemInfo}SystemInfoSoapBinding', port_type=<PortType(name='{urn:com:ssn:schema:service:v2.7.1:SystemInfo}SystemInfoPortType')>)>, {'address': 'https://localhost:8080/amm/webservice/v2_7_1/SystemInfoPort'})>])

    print("#"*30)
    for port in service.ports.values():
        # print(port)
        # print(port.name)
        # print(port.binding)
        # print("rohan////"*30)

        operations = sorted(port.binding._operations.values(),key=operator.attrgetter('name'))
        # operations = port.binding._operations.values()

        # print(operations)
        for operation in operations:
            print("Method :", operation.name)
            print(" Input :", operation.input.signature())
            # print(" Style :", operation.style)
            print("#"*30)




        

# # # service: SystemInfoService
# # # method : getCopyrightYear
# # #   input :

# # # method : getUIQVersion
# # #   input :

# # # method : getVersion
# # #   input :

# # # get a specific type signature by name
# # complextype = client.get_type('ns0:CartGetRequest')
# # print(complextype.name)
# # print(complextype.signature())
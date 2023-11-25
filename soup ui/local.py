url = 'file:///C:/Users/Crosslynx29/Desktop/vgs/files/wsdls/wsdls/2.7.1/SystemInfo.wsdl'

from zeep import Client
from zeep.wsse.username import UsernameToken

# client = Client(wsdl = url,wsse=UsernameToken('aman.srivastava', 'Welcome@123'))

client = Client(wsdl = url)
result = client.service.getCopyrightYear()
print(result)

# print(client.service.getUIQVersion())
# print(client.service.getVersion())

# getCopyrightYear() -> CopyrightYear: xsd:string
# getUIQVersion() -> VersionNumber: xsd:string, BuildID: xsd:string
# getVersion() -> VersionInfo: ns0:VersionInfoType[]



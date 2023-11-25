
# pip install zeep
# python -mzeep file:///C:/Users/Crosslynx29/Desktop/vgs/files/wsdls/wsdls/2.7.1/SystemInfo.wsdl


# python -mzeep /home/rohan1/new_project/AppSW.EsbWsdl/amm/2_10/SystemInfo.wsdl
# python -mzeep http://www.dneonline.com/calculator.asmx?wsdl
"""
Bindings:
     Soap11Binding: {http://tempuri.org/}CalculatorSoap
     Soap12Binding: {http://tempuri.org/}CalculatorSoap12

Service: Calculator
     Port: CalculatorSoap (Soap11Binding: {http://tempuri.org/}CalculatorSoap)
         Operations:
            Add(intA: xsd:int, intB: xsd:int) -> AddResult: xsd:int
            Divide(intA: xsd:int, intB: xsd:int) -> DivideResult: xsd:int
            Multiply(intA: xsd:int, intB: xsd:int) -> MultiplyResult: xsd:int
            Subtract(intA: xsd:int, intB: xsd:int) -> SubtractResult: xsd:int

     Port: CalculatorSoap12 (Soap12Binding: {http://tempuri.org/}CalculatorSoap12)
         Operations:
            Add(intA: xsd:int, intB: xsd:int) -> AddResult: xsd:int
            Divide(intA: xsd:int, intB: xsd:int) -> DivideResult: xsd:int
            Multiply(intA: xsd:int, intB: xsd:int) -> MultiplyResult: xsd:int
            Subtract(intA: xsd:int, intB: xsd:int) -> SubtractResult: xsd:int


"""

from zeep import Client
wsdl= 'http://www.dneonline.com/calculator.asmx?wsdl'
client = Client(wsdl=wsdl)

print(client.service.Add(23,22))
print(client.service.Multiply(23,22))

add = getattr(client.service, 'Add')
print('addition =', add(10, 12))


from zeep import Client

# client = Client(wsdl = 'http://www.webservicex.net/ConvertSpeed.asmx?WSDL')
# result = client.service.ConvertSpeed(
#     100, 'kilometersPerhour', 'milesPerhour')

# assert result == 62.137





url = 'http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL'

client = Client(wsdl = url)
result = client.service.ListOfCountryNamesGroupedByContinent()
# print(result)


 
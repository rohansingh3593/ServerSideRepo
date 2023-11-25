# pip3 install suds-jurko==0.6 (when it is not working use this 'pip install suds' )

from suds.client import Client
client = Client('http://www.dneonline.com/calculator.asmx?WSDL')
add = getattr(client.service, 'Add')
print('addition =', add(10, 12))
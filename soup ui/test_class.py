import requests
import zeep
 
class ServiceNow:
 
    def __init__(self, instance, username, password):
        self.instance = instance
        self.session = requests.Session()
        self.session.auth = requests.auth.HTTPBasicAuth(username, password)
        self.transport = zeep.transports.Transport(session=self.session)
 
    def client(self, tablename):
        wsdl_url = 'https://%s.service-now.com/%s.do?WSDL' % (
            self.instance, tablename)
        return zeep.CachingClient(wsdl_url, transport=self.transport)
    




sn = ServiceNow('dev00000', 'soap.test', 'password')
incident = sn.client('incident')
response = incident.service.insert(
    short_description = 'Lorem ipsum dolor sit amet',
    caller_id = 'Fred Luddy',
    urgency = '1'
)
print('inserted number=%s sys_id=%s' % (response['number'], response['sys_id']))
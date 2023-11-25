
import requests
xml = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:urn="urn:com:ssn:schema:service:v2.7:SystemInfo.xsd">
   <soapenv:Header/>
   <soapenv:Body>
      <urn:GetUIQVersion/>
   </soapenv:Body>
</soapenv:Envelope>"""
# url = 'file:///C:/Users/Crosslynx29/Desktop/vgs/files/wsdls/wsdls/2.7/SystemInfo'

url = 'https://mt.itron-systeam02-install.eng.ssnsgs.net:3009/amm/webservice/v2_7/SystemInfoPort'

# url = 'http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso'
headers = {'Content-Type': 'application/soap+xml; charset=utf-8'}

with requests.Session() as session:
    r = session.post(url, headers=headers, data=xml)
    r.raise_for_status()
    print(r.status_code)
    print(r.text)
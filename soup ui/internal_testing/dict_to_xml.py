request_data = {
    'merchantID': '1234abc',
    'billTo': {
        'street1': '400 Broad Street',
        'city': 'Seattle',
        'state': 'WA',
        'postalCode': '98109',
        'country': 'US',
    },
    'item': [{
        'id': '0',
        'unitPrice': '12.34',
        'quantity': '1',
    }],
    'taxService': {
        'run': "true",
        'nexus': "WA, CA" 
    },
}


request_data = {'FindNic': {'CachedResults': {'urn3:SearchKey': '?', 'urn3:StartRow': '?'},
             'MaxResultCount': '?',
             'NumberRows': '?',
             'ReturnNetworkInfrastructure': '?',
             'SearchParameters': {'CommonAttributes': {'BackboneDevice': '?',
                                                       'BatteryInfo': {'BatteryExpirationTime': {'End': '?',
                                                                                                 'Start': '?'},
                                                                       'BatteryID': '?',
                                                                       'BatteryInstalledTime': {'End': '?',
                                                                                                'Start': '?'},
                                                                       'BatteryLastTestedTime': {'End': '?',
                                                                                                 'Start': '?'},
                                                                       'BatteryLotNumber': '?',
                                                                       'BatteryManufacturer': '?',
                                                                       'BatteryManufacturerTime': {'End': '?',
                                                                                                   'Start': '?'},
                                                                       'BatteryModel': '?',
                                                                       'BatterySerialNumber': '?'},
                                                       'CatalogNumber': '?',
                                                       'Description': '?',
                                                       'DeviceAttribute1': '?',
                                                       'DeviceAttribute2': '?',
                                                       'DeviceAttribute3': '?',
                                                       'DeviceAttribute4': '?',
                                                       'DeviceAttribute5': '?',
                                                       'DeviceConfig': {'HardwareConfig': '?',
                                                                        'HardwarePatch': '?',
                                                                        'HardwareRev': '?',
                                                                        'HardwareVersion': '?',
                                                                        'MacID': '?',
                                                                        'MfgCode': '?',
                                                                        'MfgDate': {'End': '?',
                                                                                    'Start': '?'},
                                                                        'MfgModel': '?',
                                                                        'MfgName': '?',
                                                                        'NicArchitecture': {'LocalizedValue': '?',
                                                                                            'Name': '?'},
                                                                        'NicAttribute1': '?',
                                                                        'NicAttribute2': '?',
                                                                        'NicAttribute3': '?',
                                                                        'NicAttribute4': '?',
                                                                        'NicAttribute5': '?',
                                                                        'NicHardwareConfig': '?',
                                                                        'NicHardwarePatch': '?',
                                                                        'NicHardwareRev': '?',
                                                                        'NicHardwareVersion': '?',
                                                                        'NicMfgCode': '?',
                                                                        'NicMfgModel': '?',
                                                                        'NicMfgName': '?',
                                                                        'NicSerialNumber': '?',
                                                                        'NicSoftwareConfig': '?',
                                                                        'NicSoftwareDesc': '?',
                                                                        'NicSoftwarePatch': '?',
                                                                        'NicSoftwareReleasedTime': {'End': '?',
                                                                                                    'Start': '?'},
                                                                        'NicSoftwareRev': '?',
                                                                        'NicSoftwareTypeName': '?',
                                                                        'NicSoftwareVersion': '?',
                                                                        'NicTypeDesc': '?',
                                                                        'NicTypeName': '?',
                                                                        'SoftwareConfig': '?',
                                                                        'SoftwarePatch': '?',
                                                                        'SoftwareRev': '?',
                                                                        'SoftwareVersion': '?'},
                                                       'DidSubtype': {'urn2:LocalizedValue': '?',
                                                                      'urn2:Name': '?'},
                                                       'DidType': {'urn1:LocalizedValue': '?',
                                                                   'urn1:Name': '?'},
                                                       'IPAddress': '?',
                                                       'InsertTime': {'End': '?',
                                                                      'Start': '?'},
                                                       'InstallTime': {'End': '?',
                                                                       'Start': '?'},
                                                       'JobID': '?',
                                                       'LastCommTime': {'End': '?',
                                                                        'Start': '?'},
                                                       'LastReadByCROC': '?',
                                                       'ManufacturerESN': '?',
                                                       'Name': '?',
                                                       'NetworkID': '?',
                                                       'ParentDeviceMacID': '?',
                                                       'ParentDeviceName': '?',
                                                       'ParentDeviceSerialNumber': '?',
                                                       'RFChannel': '?',
                                                       'RemoveTime': {'End': '?',
                                                                      'Start': '?'},
                                                       'RetiredTime': {'End': '?',
                                                                       'Start': '?'},
                                                       'SerialNumber': '?',
                                                       'Suspect': '?',
                                                       'SuspectReason': '?',
                                                       'TimeZoneID': {'urn1:LocalizedValue': '?',
                                                                      'urn1:Name': '?',
                                                                      'urn1:StandardizedName': '?'},
                                                       'UIQDeviceStateTransition': {'End': '?',
                                                                                    'EnteredUIQDeviceState': {'urn1:LocalizedValue': '?',
                                                                                                              'urn1:Name': '?'},
                                                                                    'ExitedUIQDeviceState': {'urn1:LocalizedValue': '?',
                                                                                                             'urn1:Name': '?'},
                                                                                    'Start': '?'},
                                                       'UiqDeviceState': {'@Operator': 'SQL_EQUAL_TO',
                                                                          'LocalizedValue': '?',
                                                                          'Name': '?'},
                                                       'UpdateTime': {'End': '?',
                                                                      'Start': '?'},
                                                       'UtilDeviceID': '?',
                                                       'UtilDeviceState': {'urn1:LocalizedValue': '?',
                                                                           'urn1:Name': '?'},
                                                       'UtilNmState': {'LocalizedValue': '?',
                                                                       'Name': '?'}}}}}}}

"""
<merchantID>1234abc</merchantID>
<billTo>
  <street1>400 Broad Street</street1>
  <city>Seattle</city>
  <state>WA</state>
  <postalCode>98109</postalCode>
  <country>US</country>
</billTo>
<item id="0">
  <unitPrice>12.34</unitPrice>
  <quantity>1</unitPrice>
</item>
<taxService run="true">
  <nexus>WA, CA</nexus>
</taxService>
"""
# Converting Python Dictionary to XML
# pip install dict2xml
from dict2xml import dict2xml
print('#'*150)
xml = dict2xml(request_data,indent =" ")
print(xml)
print('#'*150)
xml = dict2xml(request_data, wrap ='root', indent =" ")
print(xml)
print('#'*150)



# # pip install dicttoxml 
# Pretty printing XML after parsing
# it from dictionary
from xml.dom.minidom import parseString
from dicttoxml import dicttoxml


# Data to be parsed


xml = dicttoxml(request_data)
dom = parseString(xml)

print(dom.toprettyxml())



# Converting Python Dictionary to
# XML and saving to a file
from dicttoxml import dicttoxml
from xml.dom.minidom import parseString
 
 
# Variable name of Dictionary is data
xml = dicttoxml(request_data)
 
# Obtain decode string by decode()
# function
xml_decode = xml.decode()
 
xmlfile = open("dict.xml", "w")
xmlfile.write(xml_decode)
xmlfile.close()
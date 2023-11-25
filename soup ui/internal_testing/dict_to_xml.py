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


request_data = {
    'JobInfo':{
        'Name':'Job_1',
    },
    'MeterReadJob':{
        'DeviceMacID':'08:68:71:10:60:45:79:94',
        'MeterReadType':'JOB_OP_NEW_DATA_READ',
        'NumberRetries':'3',
        'Priority':'JOB_PRIORITY_HIGH',
    },
    'Schedule':{
        'Immediate':'xsd.Nil',
    },   
    'AutoActivate':'true',
}

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
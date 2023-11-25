# import xmltodict
# import pprint
# import json

# my_xml = """
#     <audience>
#       <id what="attribute">123</id>
#       <name>Shubham</name>
#     </audience>
# """

# xml_content = """<merchantID>1234abc</merchantID>
# <billTo>
# 	<street1>400 Broad Street</street1>
# 	<city>Seattle</city>
# 	<state>WA</state>
# 	<postalCode>98109</postalCode>
# 	<country>US</country>
# </billTo>
# <item id="0">
# 	<unitPrice>12.34</unitPrice>
# 	<quantity>1
# 	</unitPrice>
# </item>
# <taxService run="true">
# 	<nexus>WA, CA</nexus>
# </taxService>"""

# xml_content = xml_content.replace('\n','')
# xml_content = xml_content.replace(' ','')

# print(xml_content)

# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(json.dumps(xmltodict.parse(my_xml)))



import xml.etree.ElementTree as ET


# def xml_to_dict(xml_string):
#     root = ET.fromstring(xml_string)
#     result = {}
#     for child in root:
#         if len(child) == 0:
#             result[child.tag] = child.text
#         else:
#             result[child.tag] = xml_to_dict(ET.tostring(child))
#     return result
# print("The XML string is:")
# print(xml_content)
# # python_dict = xml_to_dict(xml_content)
# # print("The python dictionary is:")
# # print(python_dict)


print('#'*150)

# import xml.dom.minidom
# temp = xml.dom.minidom.parseString(xml_content)
# new_xml = temp.toprettyxml()
# print(new_xml)


import xmltodict
import pprint
import re
  

# Open the file and read the contents
with open('example.xml', 'r', encoding='utf-8') as file:
    my_xml = file.read()
  


# Use xmltodict to parse and convert the 
# XML document
my_dict = xmltodict.parse(my_xml)
# Print the dictionary
pprint.pprint(my_dict)


'''

PS C:\rk\crosslynx\soup ui> & C:/Users/Crosslynx29/AppData/Local/Programs/Python/Python310/python.exe "c:/rk/crosslynx/soup ui/internal_testing/xml_to_dict.py"
'''

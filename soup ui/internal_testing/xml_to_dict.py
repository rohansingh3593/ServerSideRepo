
import xmltodict
import pprint
  

# Open the file and read the contents
with open('example.xml', 'r', encoding='utf-8') as file:
    my_xml = file.read()
  
# Use xmltodict to parse and convert the 
# XML document
my_dict = xmltodict.parse(my_xml)
# Print the dictionary
# pprint.pprint(my_dict)
print(my_dict)

def filter_keys_nested_item(data, to_delete):
    if isinstance(data, dict):
        for key,value in list(data.items()):
            if to_delete == value:
                del data[key]
        for key,value in data.items():
            filter_keys_nested_item(value, to_delete)

    elif isinstance(data, list):
        for i in data:
            filter_keys_nested_item(i, to_delete)

    
responce = my_dict

print(f'before : {responce}')
filter_keys_nested_item(responce,'?') # inplace deletion 
print(f'after : {responce}')


'''

PS C:\rk\crosslynx\soup ui> & C:/Users/Crosslynx29/AppData/Local/Programs/Python/Python310/python.exe "c:/rk/crosslynx/soup ui/internal_testing/xml_to_dict.py"
'''


def filter_keys_nested_item(data, to_delete):
    if isinstance(data, dict):
        if len(data) > 0:
            for key,value in list(data.items()):
                # print(key,' : ',value)
                if to_delete == value or value == {} :
                    del data[key]
            for key,value in data.items():
                filter_keys_nested_item(value, to_delete)

    elif isinstance(data, list):
        for i in data:
            filter_keys_nested_item(i, to_delete)


responce = {'FindNic': {'SearchParameters': {'CommonAttributes': {'DidType': {}, 'DidSubtype': {}, 'UiqDeviceState': {'@Operator': 'SQL_EQUAL_TO'}, 'UtilDeviceState': {}, 'UtilNmState': {}, 'RetiredTime': {}, 'InsertTime': {}, 'UpdateTime': {}, 'InstallTime': {}, 'RemoveTime': {}, 'LastCommTime': {}, 'DeviceConfig': {'MfgDate': {}, 'NicArchitecture': {}, 'NicSoftwareReleasedTime': {}}, 'BatteryInfo': {'BatteryManufacturerTime': {}, 'BatteryExpirationTime': {}, 'BatteryInstalledTime': {}, 'BatteryLastTestedTime': {}}, 'TimeZoneID': {}, 'UIQDeviceStateTransition': {'EnteredUIQDeviceState': {}, 'ExitedUIQDeviceState': {}}}, 'Gateway': {'WAN': {'WANCommType': {}}, 'IsSocketAP': 'false'}, 'Meter': {'Mode': {}, 'ModeFunc': {}, 'UnscheduledMeters': None, 'PrePayModeStatus': {}, 'DemandLimitModeStatus': {}, 'SwitchLockoutStatus': {}, 'ESCCActivationStatus': {}, 'ESCCEnableStatus': {}, 'LC1ConnectionStatus': {}, 'LC2ConnectionStatus': {}, 'IgnoreTamperDetectionStatus': {}, 'DoorSensorStatus': {}, 'TamperStatus': {}}, 'IMU': {'MechanismType': {}, 'ServiceRate': {}}, 'WaterModule': {'MechanismType': {}, 'ServiceRate': {}}, 'Bridge': {}, 'Location': {'LocationType': {}, 'TimeZoneID': {}, 'DistNetwork': {}, 'ServicePoint': {'Account': {}, 'ServicePtTransformer': {}}, 'Proximity': {'Distance': {}}}, 'Contacts': {'Contact': {'ContactType': {}}}}, 'CachedResults': {}, 'SortMap': {}}}

print(f'before : {responce} {len(responce)}')
filter_keys_nested_item(responce,'?') # inplace deletion 
print(f'after : {responce} {len(responce)}')

print(f'before : {responce} {len(responce)}')
filter_keys_nested_item(responce,'?') # inplace deletion 
print(f'after : {responce} {len(responce)}')


#         with open(filename, 'w') as f:
#             seps='\\\n    '
#             f.write(f"""
# #!/bin/bash

# scriptdir=$(dirname,$0)
# cd $scriptdir/{os.path.relpath(os.path.curdir, session_dir)}
# mypy \
#     {seps.join(directory)}
# """)
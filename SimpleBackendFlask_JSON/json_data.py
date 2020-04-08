import json, urllib.request

def GetData_JSON_URL(self):
    if self == '' or self == None:
        return None
    else:
        try:
            JSON_DATA = urllib.request.urlopen(self)
            JSON_GET_DATA = json.loads(JSON_DATA.read().decode())
            return JSON_GET_DATA
        except ValueError:
            return None

def HolidayData_List(self):
    return GetData_JSON_URL('https://raw.githubusercontent.com/naruenrtkhomut/SimpleJsonData/master/SimpleHoliday.json')

def HostestOrderData_List(self):
    return GetData_JSON_URL('https://raw.githubusercontent.com/naruenrtkhomut/SimpleJsonData/master/SimpleHotestOrder.json')

def LatestOrderData_List(self):
    return GetData_JSON_URL('https://raw.githubusercontent.com/naruenrtkhomut/SimpleJsonData/master/SimpleLatestOrder.json')

def ModelNameValueData_List(self):
    return GetData_JSON_URL('https://raw.githubusercontent.com/naruenrtkhomut/SimpleJsonData/master/SimpleModelNameList.json')

def ModelTypeKeyData_ist(self):
    return GetData_JSON_URL('https://raw.githubusercontent.com/naruenrtkhomut/SimpleJsonData/master/SimpleModelTypeList.json')

def ModelTypeValueData_List(self):
    return GetData_JSON_URL('https://raw.githubusercontent.com/naruenrtkhomut/SimpleJsonData/master/SimpleModelTypeValue.json')

def OrderNameData_List(self):
    return GetData_JSON_URL('https://raw.githubusercontent.com/naruenrtkhomut/SimpleJsonData/master/SimpleOrderName_Value.json')

def PaymentData_List(self):
    return GetData_JSON_URL('https://raw.githubusercontent.com/naruenrtkhomut/SimpleJsonData/master/SimplePayment.json')

def PhoneNumberData_List(self):
    return GetData_JSON_URL('https://raw.githubusercontent.com/naruenrtkhomut/SimpleJsonData/master/SimplePhoneNumber.json')

def SocialData_List(self):
    return GetData_JSON_URL('https://raw.githubusercontent.com/naruenrtkhomut/SimpleJsonData/master/SimpleSocial.json')

def TimeData_List(self):
    return GetData_JSON_URL('https://raw.githubusercontent.com/naruenrtkhomut/SimpleJsonData/master/SimpleTime.json')
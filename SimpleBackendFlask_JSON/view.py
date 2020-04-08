from flask import render_template
from SimpleBackendFlask_JSON import app
from SimpleBackendFlask_JSON import json_data as JSON_DATA
import json

#GET DATA FROM JSON
HolidayData = JSON_DATA.HolidayData_List(None)
HotestOrderData = JSON_DATA.HostestOrderData_List(None)
LatestOrderData = JSON_DATA.LatestOrderData_List(None)
ModelNameValueData = JSON_DATA.ModelNameValueData_List(None)
ModelGroupData = JSON_DATA.ModelTypeKeyData_ist(None)
ModelTypeValueData = JSON_DATA.ModelTypeValueData_List(None)
OrderNameData = JSON_DATA.OrderNameData_List(None)
PaymentData = JSON_DATA.PaymentData_List(None)
PhoneNumberData = JSON_DATA.PhoneNumberData_List(None)
SocialData = JSON_DATA.SocialData_List(None)
TimeData = JSON_DATA.TimeData_List(None)



@app.route('/')
def index():
    return render_template('index.html')

#Simple for hotest order in json data
@app.route('/HostestOrder/')
def hostestorder():
    return json.dumps(HotestOrderData)
@app.route('/HostestOrder/<key>')
def hotestorder_getkey(key = None):
    try:
        return json.dumps(HotestOrderData[key])
    except KeyError:
        return render_template('data.html',
                                TitlePage='Hotest order list not found',
                                HeaderData='Sorry your key is incorrect',
                                comm='This is resualt key : ' + key,
                                dataList=HotestOrderData)
@app.route('/HostestOrder/Key/')
def hotestorder_key():
    data_key = []
    for tmp in HotestOrderData:
        data_key.append(tmp)
    return json.dumps(data_key)
@app.route('/HostestOrder/<key>/<value>')
def hotestorder_getkey_getvalue(key = None, value = None):
    try:
        return json.dumps(HotestOrderData[key][value])
    except KeyError:
        try:
            data_getting = HotestOrderData[key]
            return render_template('data.html',
                                TitlePage='Hotest order not found',
                                HeaderData='Sorry your value is incorrect',
                                comm='This is resualt value : ' + value,
                                dataList=HotestOrderData[key])
        except KeyError:
            return render_template('data.html',
                                TitlePage='Hotest order not found',
                                HeaderData='Sorry your key is incorrect',
                                comm='This is resualt key : ' + key,
                                dataList=HotestOrderData)
@app.route('/HostestOrder/<key>/Value/')
def hotestorder_value(key = None):
    data_value = []
    try:
        for tmp in HotestOrderData[key]:
            data_value.append(tmp)
        return json.dumps(data_value)
    except KeyError:
        return render_template('data.html',
                                TitlePage='Hotest order not found',
                                HeaderData='Sorry your key is incorrect',
                                comm='This is resualt key : ' + key,
                                dataList=HotestOrderData)

#Simple data for latest order from json data
@app.route('/LatestOrder/')
def latestorder():
    return json.dumps(LatestOrderData)
@app.route('/LatestOrder/<key>')
def latestorder_getkey(key = None):
    try:
        return json.dumps(LatestOrderData[key])
    except KeyError:
        return render_template('data.html',
                                TitlePage='Latest order not found',
                                HeaderData='Sorry your key is incorrect',
                                comm='This is resualt key : ' + key,
                                dataList=LatestOrderData)
@app.route('/LatestOrder/Key/')
def latestorder_key():
    data_key = []
    for tmp in LatestOrderData:
        data_key.append(tmp)
    return json.dumps(data_key)
@app.route('/LatestOrder/<key>/<value>')
def latestorder_getkey_getvalue(key = None, value = None):
    data_value = []
    for tmp_x in LatestOrderData:
        data_value = []
        for tmp_y in LatestOrderData[tmp_x]:
            data_value.append(tmp_y)
    try:
        return json.dumps(LatestOrderData[key][value])
    except KeyError:
        try:
            data_getting = LatestOrderData[key]
            return render_template('data.html',
                                TitlePage='Latest order list not found',
                                HeaderData='Sorry your value is incorrect',
                                comm='This is resualt value : ' + value,
                                dataList=LatestOrderData[key])
        except KeyError:
            return render_template('data.html',
                                TitlePage='Latest order list not found',
                                HeaderData='Sorry your key is incorrect',
                                comm='This is resualt key : ' + key,
                                dataList=LatestOrderData)
@app.route('/LatestOrder/<key>/Value/')
def latestorder_getkey_value(key = None):
    try:
        data_value = []
        for tmp in LatestOrderData[key]:
            data_value.append(tmp)
        return json.dumps(data_value)
    except KeyError:
        return render_template('data.html',
                                TitlePage='Order list not found',
                                HeaderData='Sorry your key is incorrect',
                                comm='This is resualt key : ' + key,
                                dataList=LatestOrderData)

#Simple api link data get from json data
@app.route('/Order/')
def order():
    return json.dumps(OrderNameData)
@app.route('/Order/<key>')
def order_getkey(key = None):
    try:
        return json.dumps(OrderNameData[key])
    except KeyError:
        return render_template('data.html',
                                TitlePage='Order list not found',
                                HeaderData='Sorry your key is incorrect',
                                comm='This is resualt key : ' + key,
                                dataList=OrderNameData)
@app.route('/Order/Key/')
def order_key():
    data_key = []
    for tmp in OrderNameData:
        data_key.append(tmp)
    return json.dumps(data_key)
@app.route('/Order/<key>/<value>')
def order_getkey_getvalue(key = None, value = None):
    try:
        return json.dumps(OrderNameData[key][value])
    except KeyError:
        try:
            data_getting = OrderNameData[key]
            return render_template('data.html',
                                TitlePage='Order list not found',
                                HeaderData='Sorry your value is incorrect',
                                comm='This is resualt value : ' + value,
                                dataList=data_getting)
        except KeyError:
            return render_template('data.html',
                                TitlePage='Order list not found',
                                HeaderData='Sorry your key is incorrect',
                                comm='This is resualt key : ' + key,
                                dataList=OrderNameData)
@app.route('/Order/<key>/Value/')
def order_getkey_value(key = None):
    data_value = []
    try:
        for tmp in OrderNameData[key]:
            data_value.append(tmp)
        return json.dumps(data_value)
    except KeyError:
         return render_template('data.html',
                                TitlePage='Order list not found',
                                HeaderData='Sorry your key is incorrect',
                                comm='This is resualt key : ' + key,
                                dataList=OrderNameData)
        
#Simple api link data get from json data Time
@app.route('/Time/')
def time():
    return json.dumps(TimeData)
@app.route('/Time/<key>')
def time_getkey(key = None):
    try:
        return json.dumps(TimeData[key])
    except KeyError:
        return render_template('data.html',
                                TitlePage='Time list not found',
                                HeaderData='Sorry your key is incorrect',
                                comm='This is resualt key : ' + key,
                                dataList=TimeData)
@app.route('/Time/Key/')
def time_key():
    data_key = []
    for tmp in TimeData:
        data_key.append(tmp)
    return json.dumps(data_key)
@app.route('/Time/<key>/<value>')
def time_getkey_getvalue(key = None, value = None):
    try:
        return json.dumps(TimeData[key][value])
    except KeyError:
        try:
            data_getting = TimeData[key]
            return render_template('data.html',
                                TitlePage='Time list not found',
                                HeaderData='Sorry your value is incorrect',
                                comm='This is resualt value : ' + value,
                                dataList=TimeData[key])
        except KeyError:
            return render_template('data.html',
                                TitlePage='Time list not found',
                                HeaderData='Sorry your key is incorrect',
                                comm='This is resualt key : ' + key,
                                dataList=TimeData)
@app.route('/Time/<key>/Value/')
def time_getkey_value(key = None):
    data_value = []
    try:
        for tmp in TimeData[key]:
            data_value.append(tmp)
        return json.dumps(data_value)
    except KeyError:
        return render_template('data.html',
                                TitlePage='Time list not found',
                                HeaderData='Sorry your key is incorrect',
                                comm='This is resualt key : ' + key,
                                dataList=TimeData)
@app.route('/Time/<key>/<value1>/<value2>')
def time_getkey_value_2(key = None, value1 = None, value2 = None):
    try:
        return json.dumps(TimeData[key][value1][value2])
    except KeyError:
        try:
            data_getting = TimeData[key][value1]
            return render_template('data.html',
                                TitlePage='Time list not found',
                                HeaderData='Sorry your value2 is incorrect',
                                comm='This is resualt value2 : ' + value2,
                                dataList=data_getting)
        except KeyError:
            try:
                data_getting = TimeData[key]
                return render_template('data.html',
                                TitlePage='Time list not found',
                                HeaderData='Sorry your value1 is incorrect',
                                comm='This is resualt value1 : ' + value1,
                                dataList=data_getting)
            except KeyError:
                return render_template('data.html',
                                TitlePage='Time list not found',
                                HeaderData='Sorry your key is incorrect',
                                comm='This is resualt key : ' + key,
                                dataList=TimeData)
@app.route('/Time/<key>/<value1>/Value/')
def time_getkey_getvalue1_value(key = None, value1 = None):
    try:
        data_value = []
        for tmp in TimeData[key][value1]:
            data_value.append(tmp)
        return json.dumps(data_value)
    except KeyError:
        try:
            data_value = TimeData[key]
            return render_template('data.html',
                                TitlePage='Time list not found',
                                HeaderData='Sorry your value is incorrect',
                                comm='This is resualt value : ' + value1,
                                dataList=data_value)
        except KeyError:
            return render_template('data.html',
                                TitlePage='Time list not found',
                                HeaderData='Sorry your key is incorrect',
                                comm='This is resualt key : ' + key,
                                dataList=TimeData)


#Holiday json data
@app.route('/Holiday/')
def holiday():
    return json.dumps(HolidayData)
@app.route('/Holiday/Key/')
def holiday_key():
    data_key = []
    for tmp in HolidayData:
        data_key.append(tmp)
    return json.dumps(data_key)
@app.route('/Holiday/<key>')
def holiday_getkey(key = None):
    try:
        return json.dumps(HolidayData[key])
    except KeyError:
        return render_template('data.html',
                                TitlePage='Holiday list not found',
                                HeaderData='Sorry your key is incorrect',
                                comm='This is resualt key : ' + key,
                                dataList=HolidayData)
@app.route('/Holiday/<key>/Value/')
def holiday_getkey_value(key = None):
    try:
        data_value = []
        for tmp in HolidayData[key]:
            data_value.append(tmp)
        return json.dumps(data_value)
    except KeyError:
        return render_template('data.html',
                                TitlePage='Holiday list not found',
                                HeaderData='Sorry your key is incorrect',
                                comm='This is resualt key : ' + key,
                                dataList=HolidayData)
@app.route('/Holiday/<key>/<value>')
def holiday_getkey_getvalue(key = None, value = None):
    try:
        return json.dumps(HolidayData[key][value])
    except KeyError:
        try:
            data_getting = HolidayData[key]
            return render_template('data.html',
                                TitlePage='Holiday list not found',
                                HeaderData='Sorry your value is incorrect',
                                comm='This is resualt value : ' + value,
                                dataList=data_getting)
        except KeyError:
            return render_template('data.html',
                                TitlePage='Holiday list not found',
                                HeaderData='Sorry your key is incorrect',
                                comm='This is resualt key : ' + key,
                                dataList=HolidayData)
@app.route('/Holiday/<key>/<value>/Value/')
def holiday_getkey_getvalue_value(key = None, value = None):
    try:
        data_value = []
        for tmp in HolidayData[key][value]:
            data_value.append(tmp)
        return json.dumps(data_value)
    except KeyError:
        try:
            data_getting = HolidayData[key]
            return render_template('data.html',
                                TitlePage='Holiday list not found',
                                HeaderData='Sorry your value is incorrect',
                                comm='This is resualt value : ' + value,
                                dataList=data_getting)
        except KeyError:
            return render_template('data.html',
                                TitlePage='Holiday list not found',
                                HeaderData='Sorry your key is incorrect',
                                comm='This is resualt key : ' + key,
                                dataList=HolidayData)
@app.route('/Holiday/<key>/<value1>/<value2>')
def holiday_getkey_getvalue1_and_getvalue2(key = None, value1 = None, value2 = None):
    try:
        return json.dumps(HolidayData[key][value1][value2])
    except KeyError:
        try:
            data_getting = HolidayData[key][value1]
            return render_template('data.html',
                                TitlePage='Holiday list not found',
                                HeaderData='Sorry your value2 is incorrect',
                                comm='This is resualt value2 : ' + value2,
                                dataList=data_getting)
        except KeyError:
            try:
                dat_getting = HolidayData[key]
                return render_template('data.html',
                                TitlePage='Holiday list not found',
                                HeaderData='Sorry your value1 is incorrect',
                                comm='This is resualt value1 : ' + value1,
                                dataList=data_getting)
            except KeyError:
                return render_template('data.html',
                                TitlePage='Holiday list not found',
                                HeaderData='Sorry your key is incorrect',
                                comm='This is resualt key : ' + key,
                                dataList=HolidayData)


#Phone number
@app.route('/PhoneNumber/')
def phonenumber():
    return json.dumps(PhoneNumberData)
@app.route('/PhoneNumber/Key/')
def phonenumber_key():
    data_key = []
    for tmp in PhoneNumberData:
        data_key.append(tmp)
    return json.dumps(data_key)
@app.route('/PhoneNumber/<key>')
def phonenumber_getkey(key = None):
    try:
        return json.dumps(PhoneNumberData[key])
    except KeyError:
        return render_template('data.html',
                                TitlePage='Phone number list not found',
                                HeaderData='Sorry your key is incorrect',
                                comm='This is resualt key : ' + key,
                                dataList=PhoneNumberData)
@app.route('/PhoneNumber/<key>/Value/')
def phonenumber_getkey_value(key = None):
    try:
        data_value = []
        for tmp in PhoneNumberData[key]:
            data_value.append(tmp)
        return json.dumps(data_value)
    except KeyError:
        return render_template('data.html',
                                TitlePage='Phone number list not found',
                                HeaderData='Sorry your key is incorrect',
                                comm='This is resualt key : ' + key,
                                dataList=PhoneNumberData)
@app.route('/PhoneNumber/<key>/<value>')
def phonenumber_getkey_getvalue(key = None, value = None):
    try:
        return json.dumps(PhoneNumberData[key][value])
    except KeyError:
        try:
            data_getting = PhoneNumberData[key]
            return render_template('data.html',
                                TitlePage='Phone number list not found',
                                HeaderData='Sorry your value is incorrect',
                                comm='This is resualt value : ' + value,
                                dataList=data_getting)
        except KeyError:
            return render_template('data.html',
                                TitlePage='Phone number list not found',
                                HeaderData='Sorry your key is incorrect',
                                comm='This is resualt key : ' + key,
                                dataList=PhoneNumberData)

#Social data
@app.route('/Social/')
def social():
    return SocialData
@app.route('/Social/Key/')
def social_key():
    data_key = []
    for tmp in SocialData:
        data_key.append(tmp)
    return json.dumps(data_key)
@app.route('/Social/<key>')
def social_getkey(key = None):
    try:
        return json.dumps(SocialData[key])
    except KeyError:
        return render_template('data.html',
                                TitlePage='Social list not found',
                                HeaderData='Sorry your key is incorrect',
                                comm='This is resualt key : ' + key,
                                dataList=SocialData)
@app.route('/Social/<key>/Value/')
def social_getkey_value(key = None):
    try:
        data_value = []
        for tmp in SocialData[key]:
            data_value.append(tmp)
        return json.dumps(data_value)
    except KeyError:
        return render_template('data.html',
                                TitlePage='Social list not found',
                                HeaderData='Sorry your key is incorrect',
                                comm='This is resualt key : ' + key,
                                dataList=SocialData)
@app.route('/Social/<key>/<value>')
def social_getkey_getvalue(key = None, value = None):
    try:
        return json.dumps(SocialData[key][value])
    except KeyError:
        try:
            data_getting = SocialData[key]
            return render_template('data.html',
                                TitlePage='Social list not found',
                                HeaderData='Sorry your value is incorrect',
                                comm='This is resualt value : ' + value,
                                dataList=data_getting)
        except KeyError:
            return render_template('data.html',
                                TitlePage='Social list not found',
                                HeaderData='Sorry your key is incorrect',
                                comm='This is resualt key : ' + key,
                                dataList=SocialData)

#Payment data
@app.route('/Payment/')
def payment():
    return PaymentData
@app.route('/Payment/Key/')
def payment_key():
    data_key = []
    for tmp in PaymentData:
        data_key.append(tmp)
    return json.dumps(data_key)
@app.route('/Payment/<key>')
def payment_getkey(key = None):
    try:
        return json.dumps(PaymentData[key])
    except KeyError:
        return render_template('data.html',
                                TitlePage='Payment list not found',
                                HeaderData='Sorry your key is incorrect',
                                comm='This is resualt key : ' + key,
                                dataList=PaymentData)
@app.route('/Payment/<key>/Value/')
def payment_getkey_value(key = None):
    try:
        data_value = []
        for tmp in PaymentData[key]:
            data_value.append(tmp)
        return json.dumps(data_value)
    except KeyError:
        return render_template('data.html',
                                TitlePage='Payment list not found',
                                HeaderData='Sorry your key is incorrect',
                                comm='This is resualt key : ' + key,
                                dataList=PaymentData)
@app.route('/Payment/<key>/<value>')
def payment_getkey_getvalue(key = None, value = None):
    try:
        return json.dumps(PaymentData[key][value])
    except KeyError:
        try:
            data_getting = PaymentData[key]
            return render_template('data.html',
                                TitlePage='Payment list not found',
                                HeaderData='Sorry your value is incorrect',
                                comm='This is resualt value : ' + value,
                                dataList=data_getting)
        except KeyError:
            return render_template('data.html',
                                TitlePage='Payment list not found',
                                HeaderData='Sorry your key is incorrect',
                                comm='This is resualt key : ' + key,
                                dataList=PaymentData)

#Modeltype data
@app.route('/Model/')
def model():
    return ModelTypeValueData
@app.route('/Model/<key>')
def model_getmodeltype(key = None):
    try:
        return json.dumps(ModelGroupData[key])
    except KeyError:
        return render_template('data.html',
                                TitlePage='Model list not found',
                                HeaderData='Sorry your key is incorrect',
                                comm='This is resualt key : ' + key,
                                dataList=ModelTypeValueData)
@app.route('/Model/<key>/Value/')
def model_modeltype_check_value(key = None):
    try:
        return json.dumps(ModelTypeValueData[key])
    except KeyError:
        return render_template('data.html',
                                TitlePage='Model list not found',
                                HeaderData='Sorry your key is incorrect',
                                comm='This is resualt key : ' + key,
                                dataList=ModelTypeValueData)
@app.route('/Model/<key>/<modelname_key>')
def model_modeltype_getkey_modelname_key(key = None, modelname_key = None):
    try:
        data_check = False
        for tmp in ModelGroupData[key]:
            if modelname_key == tmp:
                data_check = True
        if data_check:
            return json.dumps(ModelNameValueData[modelname_key])
        else:
            return render_template('data.html',
                                TitlePage='Model list not found',
                                HeaderData='Sorry your modelname_key is incorrect',
                                comm='This is resualt modelname_key : ' + modelname_key,
                                dataList=ModelGroupData[key])
    except KeyError:
        return render_template('data.html',
                                TitlePage='Model list not found',
                                HeaderData='Sorry your modelname_key is incorrect',
                                comm='This is resualt modelname_key : ' + modelname_key,
                                dataList=ModelTypeValueData)
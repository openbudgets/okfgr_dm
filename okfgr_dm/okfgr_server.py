import http.client
import subprocess

def dm_okfgr(endpoint, OKFGR_SERVER="okfnrg.math.auth.gr", **kwargs):
    """
    :param endpoint: data-mining service endpoint
    :param kwargs: parameters for a data-mining function
    :return: the string-format of a json structure
    """
    conn = http.client.HTTPConnection(OKFGR_SERVER)

    if('dimession' in kwargs):
        json_data = kwargs['json_data']
        amount = kwargs['amount']
        time = kwargs['time']
        prediction_steps = kwargs['prediction_steps']

        payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"json_data\"\r\n\r\n'"+\
                  json_data+"'\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"time\"\r\n\r\n'"+\
                  time+"'\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"amount\"\r\n\r\n'"+\
                  amount+"'\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"prediction_steps\"\r\n\r\n"+ \
                  str(prediction_steps)+"\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"



    else:
        json_data = kwargs['json_data']
        dimension= kwargs['dimensions']
        amount = kwargs['amount']
        #coef.outl_value": coef_outl']
        #coef.outl_sample =  1.5
        #box.outliers_value = kwargs['box_outliers']
        #box.wdth_value = kwargs['box_wdth']
        #cor.method_value = kwargs['cor_method']

        payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"json_data\"\r\n\r\n'"+ \
                  json_data+"'\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"dimensions\"\r\n\r\n'"+ \
                  dimension+"'\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"amount\"\r\n\r\n'"+ \
                  amount+"'\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
        #print(payload)
        headers = {
            'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
            'cache-control': "no-cache",
        }


    headers = {
        'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
        'cache-control': "no-cache",
    }

    conn.request("POST", endpoint+"/print", payload, headers)
    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

    return data.decode("utf-8")





def dm_okfgr(endpoint, OKFGR_SERVER="okfnrg.math.auth.gr", **kwargs):
    """
    :param endpoint: data-mining service endpoint
    :param kwargs: parameters for a data-mining function
    :return: the string-format of a json structure
    """

    json_data = kwargs['json_data']
    amount = kwargs['amount']
    time = kwargs['time']
    prediction_steps = kwargs['prediction_steps']


    import http.client

    conn = http.client.HTTPConnection(OKFGR_SERVER)

    payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"json_data\"\r\n\r\n'"+\
              json_data+"'\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"time\"\r\n\r\n'"+\
              time+"'\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"amount\"\r\n\r\n'"+\
              amount+"'\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"prediction_steps\"\r\n\r\n"+ \
              str(prediction_steps)+"\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"

    headers = {
        'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
        'cache-control': "no-cache",
    }

    conn.request("POST", endpoint, payload, headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

    return data.decode("utf-8")


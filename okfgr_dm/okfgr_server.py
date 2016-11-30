import subprocess


def dm_okfgr(endpoint, OK_GREECE_ROOT="http://okfnrg.math.auth.gr", **kwargs):
    """
    :param endpoint: data-mining service endpoint
    :param kwargs: parameters for a data-mining function
    :return: the string-format of a json structure
    """
    arglst = []
    for k in kwargs.keys():
        arglst += ["-d", str(k)+"="+str(kwargs[k])]
    cmd = ['curl'] + arglst + [OK_GREECE_ROOT+endpoint]
    print(cmd)
    res = subprocess.check_output(cmd).decode("utf-8")
    result_endpoint = res.split('\n')[0]
    result = subprocess.check_output(['curl', OK_GREECE_ROOT+result_endpoint+'/print']).decode("utf-8")
    print(result)
    return result


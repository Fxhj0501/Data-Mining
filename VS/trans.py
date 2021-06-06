import requests

def geocode(location):
    """
    将文字转为经纬度，方便以后在地图上标记
    :param location: 想要转换的中文地址
    :return:中文地址对应的经纬度
    """
    parameters = {'address': location, 'key': '5d9923538490295330f2afd2321ffa86'}
    base = 'https://restapi.amap.com/v3/geocode/geo'
    response = requests.get(base, parameters)
    answer = response.json()
    return (answer['geocodes'][0]['location'])



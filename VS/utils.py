import folium
import linecache
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

def add_point(in_location,label,map):
    #def add_point(in_location, label, color, map):
    """
    :param in_location: 经纬度
    :param label: 日期
    :param color: k-means聚类的颜色
    :param map: 地图本体
    """
    folium.Marker(
        location=in_location,
        popup=label,
        #icon=folium.Icon(color=color)
    ).add_to(map)

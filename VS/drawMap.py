import folium
from loadFile import data_num
from loadFile import id_loc
from loadFile import num_data
from utils import *
from kmeans import centers
from kmeans import id_label
def save_map(map):
    '''
    作图，并最终保存为本地网页
    :return:
    '''
    map.save('./map.html')
def create_map():
    map = folium.Map(location=[37.8957, 114.9042], zoom_start=12)
    colors =['purple','black','blue','green']
    for id,loc in id_loc.items():
        try:
            day = num_data[id]
        except KeyError:
            day = '无日期'
        color = colors[int(id_label[id])]
        add_point(loc,day,color,map)

    i = 0
    for item in centers:
        temp = []
        temp.append(item[0])
        temp.append(item[1])
        add_center(temp,colors[i],map)
        i += 1
    save_map(map)




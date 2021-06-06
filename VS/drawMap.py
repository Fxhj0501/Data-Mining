import folium
from loadFile import data_num
from loadFile import id_loc
from loadFile import num_data
from utils import *
map = folium.Map(location=[37.8957, 114.9042], zoom_start=12)
def save_map(map):
    '''
    作图，并最终保存为本地网页
    :return:
    '''
    map.save('./map.html')

for id,loc in id_loc.items():
    day = num_data[id]
    add_point(loc,day,map)
save_map(map)




import folium

def create_map():
    '''
    作图，并最终保存为本地网页
    :return:
    '''
    map = folium.Map()
    map.save('./map.html')
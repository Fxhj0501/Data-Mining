import folium

def create_map():
    map = folium.Map()
    map.save('./map.html')
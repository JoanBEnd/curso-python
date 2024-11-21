#primer paso instalar pip install folium

import folium

map = folium.Map(
    location=[-8.003658, -78.602840], 
    zoom_start=15, 
    tiles="OpenStreetMap"
)
fg = folium.FeatureGroup(name="My app")
fg.add_child(folium.Marker(location=[-8.0, -78.6], popup="Hola, soy el marcador", icon=folium.Icon(color="green")))
map.add_child(fg)

fg.save("Soft_Proyectos_python/App_1_Web_Map/mi_mapa.html")



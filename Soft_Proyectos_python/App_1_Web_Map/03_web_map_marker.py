import pandas as pd
import folium as fl

mi_frame = pd.read_csv("Sof-Proyectos_python/App_1_Web_Map/Volcanoes.txt")
lat = mi_frame["LAT"]
lon = mi_frame["LON"]
name = mi_frame["NAME"]
altura = mi_frame["ELEV"]

mi_map = fl.Map(
    location=[39.82, -104.36],
    zoom_start=5,
    tiles="OpenStreetMap"
)

fg = fl.FeatureGroup(name=="Mi app Volcano")

color_list= ["green","orange", "red"]

def devolver_color(elevacion):
    if elevacion <= 1000:
        return color_list[0]
    elif elevacion <3000:
        return color_list[1]
    else:
        return color_list[2]


for la, lo, nombre, alt in zip(lat, lon, name, altura):
    popup_html = f"""
    
        <h4 style="margin:5px; color:#d62728;">Información del Volcán</h4>
        <p>Nombre: {nombre}</p>
        <p>Altura: {alt}</p>
        <p>Latitud: {la}<br>Longitud: {lo}</p>
    
    """    

    formato_popup = fl.IFrame(html=popup_html, width=200, height=250)

    fg.add_child(fl.Circle(
                        location=[la, lo], 
                        radius=25000,
                        popup= fl.Popup(formato_popup),                         
                        color=devolver_color(alt),
                        fill_color=devolver_color(alt),
                        fill_opacity =0.65
                 #icon=fl.Icon(color=devolver_color(alt))
                 )
                )

mi_map.add_child(fg)
mi_map.save("Sof-Proyectos_python/App_1_Web_Map/volcanes_EEUU.html")
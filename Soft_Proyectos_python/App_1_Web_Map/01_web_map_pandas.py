import pandas as pd
import folium as fl

mi_frame = pd.read_csv("Soft_Proyectos_python/App_1_Web_Map/Volcanoes.txt")
lat = mi_frame["LAT"]
lon = mi_frame["LON"]
name = mi_frame["NAME"]
altura = mi_frame["ELEV"]

mi_map = fl.Map(
    location= [31.776285, -30.223925],
    #location=[39.82, -104.36], 
    zoom_start=3, 
    tiles="OpenStreetMap"
)
fgv = fl.FeatureGroup(name = "Volcanes EEUU")

color_lista= ["green","orange","red"]

def devolver_color(elevacion):
    if elevacion <= 1000:
        return color_lista[0]
    elif elevacion < 3000:
        return color_lista[1]
    else:
        return color_lista[2]


for latitud, longitud, name, alt in zip(lat, lon, name, altura):
    popup_html = f"""
    
        <h4 style="margin:5px; color:#d62728;">Información del Volcán</h4>
        <p>Nombre: {name}</p>
        <p>Altura: {alt}</p>
        <p>Latitud: {latitud}<br>Longitud: {longitud}</p>
    
    """

    formato_popup = fl.IFrame(html=popup_html, width=200, height=200)



    fgv.add_child( fl.Marker(
                        location=[latitud, longitud],
                        popup=fl.Popup(formato_popup),
                        icon=fl.Icon(color=devolver_color(alt))
    )
    )

fgp = fl.FeatureGroup(name ="Población")

fgp.add_child(fl.GeoJson(data=open("Soft_Proyectos_python/App_1_Web_Map/world.json", 
                                   "r", encoding="utf-8-sig").read(),
                            style_function= lambda x: {"fillColor": "#86f999" if x["properties"]["POP2005"] < 10000000
                                                       else "#05ee2c" if 10000000 <= x["properties"]["POP2005"] < 20000000 else "#027815"}
                            
                        )
             )


fgpe = fl.FeatureGroup(name="Volcanes Perú")

volcan_peru = pd.read_json("Soft_Proyectos_python/App_1_Web_Map/volcanes_peru.json")

lat_pe = volcan_peru["latitud"]
lon_pe = volcan_peru["longitud"]
nombre_pe = volcan_peru["nombre"]
altura_pe = volcan_peru["altura"]

for la, lo, al, nm in zip(lat_pe, lon_pe, altura_pe, nombre_pe):
    popup_pe_html = f"""
    
        <h4 style="margin:5px; color:#d62728;">Información del Volcán</h4>
        <p>Nombre: {nm}</p>
        <p>Altura: {al}</p>
        <p>Latitud: {la}<br>Longitud: {lo}</p>
    
    """    
    popup_peru = fl.IFrame(html=popup_pe_html, width=200, height=200)
    fgpe.add_child(fl.Marker(
                            popup=fl.Popup(popup_peru),
                            location= [la, lo],
                            icon=fl.Icon(color=devolver_color(al))
                            )
                   )


mi_map.add_child(fgp)
mi_map.add_child(fgv)
mi_map.add_child(fgpe)

mi_map.add_child(fl.LayerControl())
mi_map.save("Soft_Proyectos_python/App_1_Web_Map/mapa_volcanes.html")

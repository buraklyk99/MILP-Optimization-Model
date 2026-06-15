import folium
from folium.features import DivIcon

m = folium.Map(
    location=[39.5, 40.5],
    zoom_start=6,
    tiles="CartoDB positron"
)

istanbul = [41.0082, 28.9784]
gurbulak = [39.5200, 44.3400]
bazargan = [39.3900, 44.3900]
tabriz = [38.0800, 46.2919]

route1 = [istanbul, gurbulak, bazargan, tabriz]

folium.PolyLine(
    route1,
    color="darkred",
    weight=4,
    opacity=0.9,
    tooltip="Route 1"
).add_to(m)

folium.Marker(
    istanbul,
    tooltip="Istanbul",
    icon=folium.Icon(color="green", icon="play")
).add_to(m)

folium.Marker(
    gurbulak,
    tooltip="Gurbulak Border Gate",
    icon=folium.Icon(color="orange", icon="info-sign")
).add_to(m)

folium.Marker(
    bazargan,
    tooltip="Bazargan Border Gate",
    icon=folium.Icon(color="orange", icon="info-sign")
).add_to(m)

folium.Marker(
    tabriz,
    tooltip="Tabriz",
    icon=folium.Icon(color="red", icon="flag")
).add_to(m)

folium.Marker(
    [40.96, 29.70],
    tooltip="Truck Model 1",
    icon=folium.Icon(color="red", icon="truck", prefix="fa")
).add_to(m)

folium.Marker(
    [40.92, 30.15],
    tooltip="Truck Model 2",
    icon=folium.Icon(color="blue", icon="truck", prefix="fa")
).add_to(m)

route_label = """
<div style="
background-color: white;
border: 2px solid darkred;
border-radius: 8px;
padding: 7px;
font-size: 11px;
line-height: 1.25;
width: 235px;
box-shadow: 2px 2px 6px rgba(0,0,0,0.25);
">
<b style="color:darkred;">Route 1</b><br>
Risk Score: <b>3.50</b><br>
M1: 6 trucks | 84 m³ | $3200<br>
M2: 3 truck | 43 m³ | $2600
</div>
"""

folium.Marker(
    [41.70, 36.80],
    icon=DivIcon(
        icon_size=(240, 90),
        icon_anchor=(0, 0),
        html=route_label
    )
).add_to(m)

m.save("route1_professional_map.html")

print("Route 1 map created.")
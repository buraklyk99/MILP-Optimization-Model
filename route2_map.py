import folium
from folium.features import DivIcon

m = folium.Map(
    location=[39.5, 40.5],
    zoom_start=6,
    tiles="CartoDB positron"
)

istanbul = [41.0082, 28.9784]
dilucu = [39.6500, 44.8000]
nakhchivan = [39.2089, 45.4122]
culfa = [38.9400, 45.6300]
tabriz = [38.0800, 46.2919]

route2 = [istanbul, dilucu, nakhchivan, culfa, tabriz]

folium.PolyLine(
    route2,
    color="darkblue",
    weight=4,
    opacity=0.9,
    tooltip="Route 2"
).add_to(m)

folium.Marker(
    istanbul,
    tooltip="Istanbul",
    icon=folium.Icon(color="green", icon="play")
).add_to(m)

folium.Marker(
    dilucu,
    tooltip="Dilucu Border Gate",
    icon=folium.Icon(color="orange", icon="info-sign")
).add_to(m)

folium.Marker(
    nakhchivan,
    tooltip="Nakhchivan Transit Point",
    icon=folium.Icon(color="orange", icon="info-sign")
).add_to(m)

folium.Marker(
    culfa,
    tooltip="Culfa Border Gate",
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
border: 2px solid darkblue;
border-radius: 8px;
padding: 7px;
font-size: 11px;
line-height: 1.25;
width: 235px;
box-shadow: 2px 2px 6px rgba(0,0,0,0.25);
">
<b style="color:darkblue;">Route 2</b><br>
Risk Score: <b>3.55</b><br>
M1: 5 trucks | 84 m³ | $3150<br>
M2: 2 truck | 43 m³ | $2550
</div>
"""

folium.Marker(
    [42.20, 42.50],
    icon=DivIcon(
        icon_size=(240, 90),
        icon_anchor=(0, 0),
        html=route_label
    )
).add_to(m)

m.save("route2_professional_map.html")

print("Route 2 map created.")
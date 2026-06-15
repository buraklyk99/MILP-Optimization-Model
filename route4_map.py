import folium
from folium.features import DivIcon

m = folium.Map(
    location=[39.5, 41.5],
    zoom_start=6,
    tiles="CartoDB positron"
)

istanbul = [41.0082, 28.9784]
van = [38.5012, 43.3729]
kapikoy = [38.4750, 44.3000]
razi = [38.4700, 44.4000]
tabriz = [38.0800, 46.2919]

route4 = [
    istanbul,
    van,
    kapikoy,
    razi,
    tabriz
]

folium.PolyLine(
    route4,
    color="darkgreen",
    weight=4,
    opacity=0.9,
    tooltip="Route 4"
).add_to(m)

folium.Marker(
    istanbul,
    tooltip="Istanbul",
    icon=folium.Icon(color="green", icon="play")
).add_to(m)

folium.Marker(
    kapikoy,
    tooltip="Kapikoy Border Gate",
    icon=folium.Icon(color="orange", icon="info-sign")
).add_to(m)

folium.Marker(
    razi,
    tooltip="Razi Border Gate",
    icon=folium.Icon(color="orange", icon="info-sign")
).add_to(m)

folium.Marker(
    tabriz,
    tooltip="Tabriz",
    icon=folium.Icon(color="red", icon="flag")
).add_to(m)

# Trucks near Istanbul

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

# Route information

route_label = """
<div style="
background-color: white;
border: 2px solid darkgreen;
border-radius: 8px;
padding: 7px;
font-size: 11px;
line-height: 1.25;
width: 210px;
box-shadow: 2px 2px 6px rgba(0,0,0,0.25);
">
<b style="color:darkgreen;">Route 4</b><br>
Risk Score: <b>3.65</b><br>
M1: 4 trucks | 84 m³ | $3500<br>
M2: 2 truck | 43 m³ | $2850
</div>
"""

# Kutu Karadeniz tarafında boş alanda

folium.Marker(
    [42.20, 39.50],
    icon=DivIcon(
        icon_size=(220, 90),
        icon_anchor=(0, 0),
        html=route_label
    )
).add_to(m)

m.save("route4_professional_map.html")

print("Route 4 map created.")
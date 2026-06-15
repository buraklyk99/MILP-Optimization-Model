import folium
from folium.features import DivIcon

m = folium.Map(
    location=[39.0, 42.5],
    zoom_start=6,
    tiles="CartoDB positron"
)

istanbul = [41.0082, 28.9784]
hakkari = [37.5744, 43.7408]
esendere = [37.7150, 44.6200]
serow = [37.7300, 44.6500]
urmia = [37.5527, 45.0761]
tabriz = [38.0800, 46.2919]

route5 = [
    istanbul,
    hakkari,
    esendere,
    serow,
    urmia,
    tabriz
]

folium.PolyLine(
    route5,
    color="purple",
    weight=4,
    opacity=0.9,
    tooltip="Route 5"
).add_to(m)

folium.Marker(
    istanbul,
    tooltip="Istanbul",
    icon=folium.Icon(color="green", icon="play")
).add_to(m)

folium.Marker(
    esendere,
    tooltip="Esendere Border Gate",
    icon=folium.Icon(color="orange", icon="info-sign")
).add_to(m)

folium.Marker(
    serow,
    tooltip="Serow Border Gate",
    icon=folium.Icon(color="orange", icon="info-sign")
).add_to(m)

folium.Marker(
    urmia,
    tooltip="Urmia",
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
border: 2px solid purple;
border-radius: 8px;
padding: 7px;
font-size: 11px;
line-height: 1.25;
width: 210px;
box-shadow: 2px 2px 6px rgba(0,0,0,0.25);
">
<b style="color:purple;">Route 5</b><br>
Risk Score: <b>3.90</b><br>
M1: 2 trucks | 84 m³ | $3900<br>
M2: 1 truck | 43 m³ | $3200
</div>
"""

# Kutu haritanın boş alanında

folium.Marker(
    [42.00, 39.50],
    icon=DivIcon(
        icon_size=(220, 90),
        icon_anchor=(0, 0),
        html=route_label
    )
).add_to(m)

m.save("route5_professional_map.html")

print("Route 5 map created.")
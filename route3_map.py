import folium
from folium.features import DivIcon

m = folium.Map(
    location=[40.5, 45.0],
    zoom_start=5,
    tiles="CartoDB positron"
)

istanbul = [41.0082, 28.9784]
sarp = [41.3900, 41.4200]
tbilisi = [41.7151, 44.8271]
baku = [40.4093, 49.8671]
astara = [38.4550, 48.8750]
tabriz = [38.0800, 46.2919]

route3 = [
    istanbul,
    sarp,
    tbilisi,
    baku,
    astara,
    tabriz
]

folium.PolyLine(
    route3,
    color="darkorange",
    weight=4,
    opacity=0.9,
    tooltip="Route 3"
).add_to(m)

folium.Marker(
    istanbul,
    tooltip="Istanbul",
    icon=folium.Icon(color="green", icon="play")
).add_to(m)

folium.Marker(
    sarp,
    tooltip="Sarp Border Gate",
    icon=folium.Icon(color="orange", icon="info-sign")
).add_to(m)

folium.Marker(
    tbilisi,
    tooltip="Tbilisi",
    icon=folium.Icon(color="orange", icon="info-sign")
).add_to(m)

folium.Marker(
    baku,
    tooltip="Baku",
    icon=folium.Icon(color="orange", icon="info-sign")
).add_to(m)

folium.Marker(
    astara,
    tooltip="Astara Border Gate",
    icon=folium.Icon(color="orange", icon="info-sign")
).add_to(m)

folium.Marker(
    tabriz,
    tooltip="Tabriz",
    icon=folium.Icon(color="red", icon="flag")
).add_to(m)

# Truck markers
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
border: 2px solid darkorange;
border-radius: 8px;
padding: 7px;
font-size: 11px;
line-height: 1.25;
width: 210px;
box-shadow: 2px 2px 6px rgba(0,0,0,0.25);
">
<b style="color:darkorange;">Route 3</b><br>
Risk Score: <b>4.05</b><br>
M1: 4 trucks | 84 m³ | $4600<br>
M2: 2 truck | 43 m³ | $3750
</div>
"""

# Kutuyu haritanın boş kısmına koyuyoruz
folium.Marker(
    [43.20, 46.50],
    icon=DivIcon(
        icon_size=(220, 90),
        icon_anchor=(0, 0),
        html=route_label
    )
).add_to(m)

m.save("route3_professional_map.html")

print("Route 3 map created.")
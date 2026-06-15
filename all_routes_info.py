import folium
from folium.features import DivIcon

# =====================================================
# IRAN ROUTES MAP WITH RISK, TRUCKS, CAPACITY AND COST
# =====================================================

m = folium.Map(
    location=[39.5, 42.5],
    zoom_start=5,
    tiles="CartoDB positron"
)

routes = {
    1: {
        "name": "Route 1",
        "path": "Istanbul → Gurbulak → Bazargan → Tabriz",
        "color": "darkred",
        "risk": 3.50,
        "coords": [
            [41.0082, 28.9784],
            [39.5200, 44.3400],
            [39.3900, 44.3900],
            [38.0800, 46.2919]
        ],
        "label_pos": [40.30, 36.50],
        "m1_trucks": 6,
        "m2_trucks": 3,
        "m1_cost": 3200,
        "m2_cost": 2600
    },
    2: {
        "name": "Route 2",
        "path": "Istanbul → Dilucu → Nakhchivan → Culfa → Tabriz",
        "color": "darkblue",
        "risk": 3.55,
        "coords": [
            [41.0082, 28.9784],
            [39.6500, 44.8000],
            [39.2089, 45.4122],
            [38.9400, 45.6300],
            [38.0800, 46.2919]
        ],
        "label_pos": [39.55, 40.20],
        "m1_trucks": 5,
        "m2_trucks": 2,
        "m1_cost": 3150,
        "m2_cost": 2550
    },
    3: {
        "name": "Route 3",
        "path": "Istanbul → Sarp → Tbilisi → Baku → Astara → Tabriz",
        "color": "darkorange",
        "risk": 4.05,
        "coords": [
            [41.0082, 28.9784],
            [41.5200, 41.5500],
            [41.7151, 44.8271],
            [40.4093, 49.8671],
            [38.4550, 48.8750],
            [38.0800, 46.2919]
        ],
        "label_pos": [42.10, 45.30],
        "m1_trucks": 4,
        "m2_trucks": 2,
        "m1_cost": 4600,
        "m2_cost": 3750
    },
    4: {
        "name": "Route 4",
        "path": "Istanbul → Van → Kapikoy → Razi → Tabriz",
        "color": "darkgreen",
        "risk": 3.65,
        "coords": [
            [41.0082, 28.9784],
            [38.5012, 43.3729],
            [38.4750, 44.3000],
            [38.4700, 44.4000],
            [38.0800, 46.2919]
        ],
        "label_pos": [37.60, 39.20],
        "m1_trucks": 4,
        "m2_trucks": 1,
        "m1_cost": 3500,
        "m2_cost": 2850
    },
    5: {
        "name": "Route 5",
        "path": "Istanbul → Hakkari → Esendere → Serow → Urmia → Tabriz",
        "color": "purple",
        "risk": 3.90,
        "coords": [
            [41.0082, 28.9784],
            [37.5744, 43.7408],
            [37.7150, 44.6200],
            [37.7300, 44.6500],
            [37.5527, 45.0761],
            [38.0800, 46.2919]
        ],
        "label_pos": [36.80, 42.80],
        "m1_trucks": 2,
        "m2_trucks": 1,
        "m1_cost": 3900,
        "m2_cost": 3200
    }
}

# =====================================================
# DRAW ROUTES AND LABELS
# =====================================================

for route_id, r in routes.items():

    folium.PolyLine(
        r["coords"],
        color=r["color"],
        weight=3,
        opacity=0.85
    ).add_to(m)

    label_html = f"""
    <div style="
        background-color: white;
        border: 2px solid {r['color']};
        border-radius: 8px;
        padding: 6px;
        font-size: 11px;
        width: 230px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.25);
    ">
        <b style="color:{r['color']};">{r['name']}</b><br>
        Risk Score: <b>{r['risk']}</b><br>
        M1: {r['m1_trucks']} trucks | 84 m³ | ${r['m1_cost']}<br>
        M2: {r['m2_trucks']} truck | 43 m³ | ${r['m2_cost']}
    </div>
    """

    folium.Marker(
        location=r["label_pos"],
        icon=DivIcon(
            icon_size=(240, 90),
            icon_anchor=(0, 0),
            html=label_html
        )
    ).add_to(m)

# =====================================================
# MAIN LOCATION MARKERS
# =====================================================

folium.Marker(
    [41.0082, 28.9784],
    popup="Origin: Istanbul",
    tooltip="Istanbul",
    icon=folium.Icon(color="green", icon="play")
).add_to(m)

folium.Marker(
    [38.0800, 46.2919],
    popup="Destination: Tabriz",
    tooltip="Tabriz",
    icon=folium.Icon(color="darkred", icon="flag")
).add_to(m)

# =====================================================
# TRUCK MARKERS NEAR ISTANBUL
# =====================================================

folium.Marker(
    [40.9300, 30.2500],
    tooltip="Truck Model 1",
    icon=folium.Icon(color="red", icon="truck", prefix="fa")
).add_to(m)

folium.Marker(
    [40.9700, 29.7000],
    tooltip="Truck Model 2",
    icon=folium.Icon(color="blue", icon="truck", prefix="fa")
).add_to(m)

# =====================================================
# GENERAL LEGEND
# =====================================================

legend_html = """
<div style="
position: fixed;
bottom: 40px;
left: 40px;
width: 280px;
height: 120px;
background-color: white;
border: 2px solid grey;
z-index: 9999;
font-size: 13px;
padding: 10px;
border-radius: 8px;
box-shadow: 2px 2px 6px rgba(0,0,0,0.3);
">
<b>Iran Route Alternatives</b><br><br>
🚛 Truck Model 1: 84 m³<br>
🚛 Truck Model 2: 43 m³<br>
Risk and cost values are shown on each route label.
</div>
"""

m.get_root().html.add_child(folium.Element(legend_html))

# =====================================================
# SAVE MAP
# =====================================================

m.save("iran_routes_risk_cost_map.html")

print("IRAN ROUTES RISK AND COST MAP CREATED")

import pydeck as pdk
import pandas as pd
import webbrowser
import os

# Set Mapbox access token as an environment variable
os.environ["MAPBOX_API_KEY"] = "pk.eyJ1IjoidXNlZmNtaSIsImEiOiJjazJvaTFhYngwMm96M2NtYjN4MTVqYnk4In0.QyTpRlf1_i5n_d-uOkdoDg"

# Sample data
data = pd.DataFrame({
    'latitude': [-6.905458],
    'longitude': [108.7387585],
    'radius': [100]
})

# Create a scatterplot layer
layer = pdk.Layer(
    "ScatterplotLayer",
    data=data,
    get_position="[longitude, latitude]",
    get_color="[200, 30, 0, 160]",
    get_radius="radius",
    radius_scale=0.05,
)

# Create a Deck.gl map with Mapbox provider
view = pdk.ViewState(latitude=-6.905458, longitude=108.7387585, zoom=15, bearing=0, pitch=0)
r = pdk.Deck(layers=[layer], initial_view_state=view, map_provider="mapbox", map_style="satellite")

# Add a marker
marker_layer = pdk.Layer(
    "ScatterplotLayer",
    data=data,
    get_position="[longitude, latitude]",
    #get_color="[0, 255, 0, 255]",
    #get_radius="radius",
    #radius_scale=0.05,
    
    get_color="[255, 0, 0, 255]",
    get_radius="radius",
    radius_scale=20,  # Increase the radius scale for a larger marker
    pickable=True
)
r.layers.append(marker_layer)

# Create a text layer for the place names
text_layer = pdk.Layer(
    "TextLayer",
    data=data,
    get_position="[longitude, latitude]",
    get_text="name",
    get_color="[255, 255, 255, 200]",
    get_size=16,
    get_alignment_baseline="'bottom'",
)
r.layers.append(text_layer)

# Save the map as HTML
html_path = "my_map.html"
r.to_html(html_path)

# Open the HTML file in a web browser
webbrowser.open(html_path)


import pydeck as pdk
import pandas as pd
import webbrowser

# Sample data
data = pd.DataFrame({
    'latitude': [37.7749, 37.7742, 37.7737],
    'longitude': [-122.4194, -122.4183, -122.4191],
    'radius': [100, 200, 150]
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

# Create a Deck.gl map
view = pdk.ViewState(latitude=-6.905458, longitude=108.7387585, zoom=11)
r = pdk.Deck(layers=[layer], initial_view_state=view)

# Save the map as HTML
html_path = "my_map.html"
r.to_html(html_path)

# Open the HTML file in a web browser
webbrowser.open(html_path)
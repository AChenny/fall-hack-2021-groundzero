import gmaps
from ipywidgets.embed import embed_minimal_html

gmaps.configure(api_key="AIzaSyBCezsABWlWkGzswTzlrnjiW24MfJE1BTQ")

fig = gmaps.figure()
# locations = [(49.23757, -122.99703), (49.22087, -123.00913)]
# locations = [(46.1, 5.2), (46.2, 5.3), (46.3, 5.4)]
# fig.add_layer(gmaps.heatmap_layer(locations))
# fig = gmaps.figure(center=(49, -122.0), zoom_level=8)

locations = [(46.1, 5.2), (46.2, 5.3), (46.3, 5.4)]
weights = [0.5, 0.2, 0.8]
heatmap = gmaps.heatmap_layer(locations, weights=weights)
heatmap.max_intensity = 3.5
heatmap.weights = [3, 3, 3]
fig.add_layer(heatmap)
embed_minimal_html('export.html', views=[fig])


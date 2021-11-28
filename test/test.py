import gmaps
from ipywidgets.embed import embed_minimal_html

# gmaps.configure(api_key="AIzaSyBCezsABWlWkGzswTzlrnjiW24MfJE1BTQ")
input =[[49.1863889, -122.8444444], [49.1875983, -122.8459183], [49.198558, -122.8511518], [49.1899738, -122.8468036], [49.18460779999999, -122.8436785], [49.1934714, -122.8457022], [49.1981686, -122.842133], [49.18902310000001, -122.8474488], [49.18641179999999, -122.8475174], [49.1876492, -122.8436099], [49.1864171, -122.8502822], [49.17660549999999, -122.8463193], [49.19143800000001, -122.8570928], [49.1870525, -122.8499398], [49.1963574, -122.8456972], [49.1879814, -122.8465375], [49.186238, -122.847956], [49.18711099999999, -122.8494954], [49.18710099999999, -122.849192], [49.1871057, -122.8494145]]
lat, lng = [49.1880494, -122.8493724]

# fig = gmaps.figure(center=(lat, lng), zoom_level=15, layout={
#         'width': '1200px',
#         'height': '1200px',
#         'padding': '3px',
#         'border': '1px solid black'})
# # locations = [(49.23757, -122.99703), (49.22087, -123.00913)]
# # locations = [(46.1, 5.2), (46.2, 5.3), (46.3, 5.4)]
# # fig.add_layer(gmaps.heatmap_layer(locations))
# # fig = gmaps.figure(center=(49, -122.0), zoom_level=8)

# locations = input
# weights = [3] * len(input)
# heatmap = gmaps.heatmap_layer(locations, weights=weights)
# heatmap.max_intensity = 3.5
# heatmap.weights = [3] * len(input)
# heatmap.point_radius = 30
# fig.add_layer(heatmap)
# embed_minimal_html('export.html', views=[fig])



def heatmap(restaruants, lat, lng):
    gmaps.configure(api_key="GMAPKEY")
    input = restaruants
    

    fig = gmaps.figure(center=(lat, lng), zoom_level=15, layout={
            'width': '1200px',
            'height': '1200px',
            'padding': '3px',
            'border': '1px solid black'})
    # locations = [(49.23757, -122.99703), (49.22087, -123.00913)]
    # locations = [(46.1, 5.2), (46.2, 5.3), (46.3, 5.4)]
    # fig.add_layer(gmaps.heatmap_layer(locations))
    # fig = gmaps.figure(center=(49, -122.0), zoom_level=8)

    locations = input
    weights = [3] * len(input)
    heatmap = gmaps.heatmap_layer(locations, weights=weights)
    heatmap.max_intensity = 3.5
    heatmap.weights = [3] * len(input)
    heatmap.point_radius = 30
    fig.add_layer(heatmap)
    embed_minimal_html(lat+"&" + lng + '.html', views=[fig])


heatmap(input, lat, lng)
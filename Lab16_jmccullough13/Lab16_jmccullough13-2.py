#From the Book: 16-9
#Jeffrey McCullough
#April 16, 2023


import csv
from plotly.graph_objects import Scattergeo, Layout
from plotly import offline

# Explore the structure of the data.
filename = 'data\world_fires_1_day.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    lats, lons, brights, hover_texts = [], [], [], []
    for row in reader:
        try:
            lat = float(row[0])
            lon = float(row[1])
            bright = float(row[2])
            title = row[5]
        except ValueError:
            print(f"No data at {title}")
        else:
            lats.append(lat)
            lons.append(lon)
            brights.append(bright)
            hover_texts.append(title)
#Map the earthquakes
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
    'color': brights,
    'colorscale': 'Greens',
    'reversescale': False,
    'colorbar': {'title': 'Magnitude'},
    },
}]
my_layout = Layout(title='Global Fires')
fig = {'data':data, 'layout': my_layout}
offline.plot(fig, filename='global_fires.html')

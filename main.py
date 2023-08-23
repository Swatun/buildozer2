import plotly.express as px
import webbrowser
import tempfile

# Ustawienia mapy 
mapbox_access_token = 'your_mapbox_token'

# Dane punktowe (koordynaty)
lats = [45.5236, 46.9424, 47.5234] 
lons = [15.6454, 16.4532, 17.2341]

# Rysowanie punktow na mapie
fig = px.scatter_mapbox(
    lat=lats,
    lon=lons,
    zoom=5,
    height=300
)

# Dodanie tokenu do mapy
fig.update_layout(
    mapbox_style="open-street-map", 
    mapbox_accesstoken=mapbox_access_token
)

# Zapisanie mapy do pliku HTML tymczasowego z kodowaniem utf-8
temp_html_file = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.html', encoding='utf-8')
temp_html_file.write(fig.to_html())
temp_html_file.close()

# Otwarcie pliku HTML w przeglądarce
webbrowser.open_new_tab(temp_html_file.name)

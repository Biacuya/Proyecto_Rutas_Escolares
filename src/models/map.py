import folium
from geopy.distance import geodesic
from geopy.geocoders import Nominatim

# Crear un mapa centrado en una ubicación específica
latitude = 5.540278
longitude = -73.361389
mapa = folium.Map(location=[latitude, longitude], zoom_start=14)

# Agregar marcadores


def obtener_coordenadas(direccion):
    geolocalizador = Nominatim(
        user_agent="mi_aplicacion"
    )  # Reemplaza "mi_aplicacion" con un nombre significativo para tu aplicación
    ubicacion = geolocalizador.geocode(direccion)
    if ubicacion:
        return (ubicacion.latitude, ubicacion.longitude)
    else:
        return None


location_one = (5.54953, -73.35989)
location_two = (5.55123, -73.35521)
location_two = (5.55123, -73.38421)

coord = obtener_coordenadas("Los Hongos, Tunja, Boyaca, Colombia")
distance = geodesic(location_one, location_two).kilometers
print(distance)

folium.Marker(location_one, popup="Ubicación 1").add_to(mapa)
folium.Marker(location_two, popup="Ubicación 2").add_to(mapa)


# Guardar el mapa en un archivo HTML
print(coord)
mapa.save("mapa.html")

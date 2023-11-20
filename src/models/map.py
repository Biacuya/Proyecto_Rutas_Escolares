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


def get_distance(address_one, address_two):
    distance = geodesic(address_one, address_two).kilometers
    return distance


# coord = obtener_coordenadas("Los Hongos, Tunja, Boyaca, Colombia")
address_scholl = 5.557898, -73.35421
location_two = 5.51629555, -73.36856103385719
distance = geodesic(address_scholl, location_two).kilometers


# folium.Marker(location_one, popup="Ubicación 1").add_to(mapa)
# folium.Marker(location_two, popup="Ubicación 2").add_to(mapa)


# Guardar el mapa en un archivo HTML
mapa.save("mapa.html")

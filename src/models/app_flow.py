from address import Address
from map import obtener_coordenadas, get_distance


class AppFlow:
    list_address = []
    list_coordinates = []
    list_distances = ()
    address_scholl = 5.557898, -73.35421

    def create_address(self, name):
        address = Address(name)
        self.list_address.append(address.get_name_address())
        print(self.list_address)

    def get_coordinates(self):
        print("AQUI")
        for name in self.list_address:
            self.list_coordinates.append(obtener_coordenadas(name))
            print(self.list_coordinates)

    def get_distance_between_addresses(self):
        app.get_coordinates()
        for coordinates in self.list_coordinates:
            print(f"coordenadas {coordinates}")
            self.list_distances = get_distance(self.address_scholl, coordinates)
            print(self.list_distances)


app = AppFlow()
name = input("Ingresa una dirección ") + ", Tunja, Boyaca, Colombia"
app.create_address(name)
name = input("Ingresa una dirección ") + ", Tunja, Boyaca, Colombia"
app.create_address(name)
name = input("Ingresa una dirección ") + ", Tunja, Boyaca, Colombia"
app.create_address(name)
print(name)
print(app.get_distance_between_addresses())

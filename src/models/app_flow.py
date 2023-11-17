from address import Address
from map import obtener_coordenadas, get_distance


class AppFlow:
    list_address = []
    list_coordinates = []
    list_distances = []
    list_completed_address = []
    address = ""
    address_scholl = 5.557898, -73.35421
    SPEED = 30  # Km/h

    def create_address(self, name):
        self.address = Address(name)
        self.list_address.append(self.address.get_name_address())
        print(self.list_address)

    def get_coordinates(self):
        for name in self.list_address:
            self.list_coordinates.append(obtener_coordenadas(name))
            print(self.list_coordinates)

    def get_distance_between_addresses(self):
        app.get_coordinates()
        for coordinates in self.list_coordinates:
            self.list_distances.append(get_distance(self.address_scholl, coordinates))
            print(self.list_distances)

    def calculate_time(self):
        for distance in self.list_distances:
            raw_time = distance / self.SPEED
            time_in_minutes = round((raw_time * 60), 2)
            # print(f"Tiempo: {round((time * 60),2)}")
            return time_in_minutes

    def create_completed_address(self, distance, time):
        for name_address in self.list_address:
            completed_address = Address(name_address, distance, time)
            self.list_completed_address.append(completed_address)


app = AppFlow()
name = input("Ingresa una dirección ") + ", Tunja, Boyaca, Colombia"
app.create_address(name)
name = input("Ingresa una dirección ") + ", Tunja, Boyaca, Colombia"
app.create_address(name)
name = input("Ingresa una dirección ") + ", Tunja, Boyaca, Colombia"
app.create_address(name)
app.get_distance_between_addresses()
app.calculate_time()

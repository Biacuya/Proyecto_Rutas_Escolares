from address import Address
from map import obtener_coordenadas, get_distance


class AppFlow:
    list_address = []
    list_coordinates = []
    list_distances = []
    list_completed_address = []
    list_time_between_scholl = []
    address = ""
    address_scholl = 5.557898, -73.35421
    SPEED = 30  # Km/h

    def create_address(self, name):
        self.address = Address(name)
        self.list_address.append(self.address)

    def get_coordinates(self):
        for i, address_name in enumerate(self.list_address):
            self.list_coordinates.append(
                obtener_coordenadas(address_name.get_name_address())
            )
            print(self.list_coordinates)

    def get_distance_between_addresses(self):
        app.get_coordinates()
        for coordinates in self.list_coordinates:
            self.list_distances.append(get_distance(self.address_scholl, coordinates))

    def calculate_time(self):
        for distance in self.list_distances:
            raw_time = distance / self.SPEED
            time_in_minutes = round((raw_time * 60), 2)
            self.list_time_between_scholl.append(time_in_minutes)
            print(self.list_time_between_scholl)

    def create_completed_address(self):
        count = 0
        for j, address_time in enumerate(self.list_time_between_scholl):
            for k, address_name in enumerate(self.list_address):
                if address_name.get_distance_address() == None:
                    new_address = Address(
                        address_name.get_name_address(),
                        self.list_distances[count],
                        self.list_time_between_scholl[count],
                    )
                    if address_name.get_distance_address() == None:
                        del self.list_address[k]
                    self.list_address.append(new_address)
                    self.list_completed_address.append(new_address)
                    count += 1
                else:
                    print("Ya tiene una distancia", address_name.get_name_address())

    def print_aux(self):
        for aux in self.list_completed_address:
            print(
                aux.get_name_address(),
                aux.get_distance_address(),
                aux.get_time_list_address(),
            )


app = AppFlow()
# name = input("Ingresa una dirección ") + ", Tunja, Boyaca, Colombia"
app.create_address("Calle 17, Tunja, Boyaca, Colombia")
# name = input("Ingresa una dirección ") + ", Tunja, Boyaca, Colombia"
app.create_address("Calle 27, Tunja, Boyaca, Colombia")
# name = input("Ingresa una dirección ") + ", Tunja, Boyaca, Colombia"
app.create_address("Calle 13, Tunja, Boyaca, Colombia")
app.get_distance_between_addresses()
app.calculate_time()
app.create_completed_address()
app.print_aux()

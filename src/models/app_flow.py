from address import Address
from map import obtener_coordenadas, get_distance


class AppFlow:
    list_address = []
    list_coordinates = []
    list_distances = []
    list_distances_between_addresses = []
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
            address_name.set_coordinates(
                obtener_coordenadas(address_name.get_name_address())
            )
            print(self.list_coordinates)

    def get_distance_between_addresses_and_scholl_address(self):
        app.get_coordinates()
        for coordinates in self.list_coordinates:
            self.list_distances.append(get_distance(self.address_scholl, coordinates))

    def get_distance_between_addresses(self):
        count_leng_list = 0
        count_actual_position = 0
        while count_actual_position < len(self.list_address):
            print(f"Count posición actual:{count_actual_position}")
            dictionary_distances = {
                self.list_address[count_actual_position].get_name_address(): {}
            }
            for address_coordinates in self.list_address:
                print(f"Count: {count_actual_position}")
                print(f"Count2: {count_leng_list}")
                if count_leng_list < len(self.list_address):
                    aux = get_distance(
                        self.list_address[count_actual_position].get_coordinates(),
                        address_coordinates.get_coordinates(),
                    )
                    raw_time_between_address = aux / self.SPEED
                    time_in_minutes_between_address = round(
                        (raw_time_between_address * 60), 2
                    )
                    count_leng_list += 1
                    dictionary_distances[
                        self.list_address[count_actual_position].get_name_address()
                    ][
                        address_coordinates.get_name_address()
                    ] = time_in_minutes_between_address
                    self.list_address[count_actual_position].set_dictionary_of_address(
                        dictionary_distances
                    )
                    print(
                        self.list_address[
                            count_actual_position
                        ].get_dictionary_of_address()
                    )
                    print("Metodo direcciones: ", dictionary_distances)
                else:
                    print("Acabo y se reinicia")
                    count_leng_list = 0
            count_actual_position += 1

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
                if address_name.get_distance_between_address_scholl_address() == None:
                    new_address = Address(
                        address_name.get_name_address(),
                        self.list_distances[count],
                        self.list_time_between_scholl[count],
                        address_name.get_coordinates(),
                        address_name.get_dictionary_of_address(),
                    )
                    if (
                        address_name.get_distance_between_address_scholl_address()
                        == None
                    ):
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
                aux.get_distance_between_address_scholl_address(),
                aux.get_time_list_address(),
            )

    def dictionary_graph(self):
        graph = {"scholl": {}}
        for name_test in self.list_completed_address:
            graph["scholl"][
                name_test.get_name_address()
            ] = name_test.get_time_list_address()
        print(graph)


app = AppFlow()
# name = input("Ingresa una dirección ") + ", Tunja, Boyaca, Colombia"
app.create_address("Calle 17, Tunja, Boyaca, Colombia")
# name = input("Ingresa una dirección ") + ", Tunja, Boyaca, Colombia"
app.create_address("Calle 27, Tunja, Boyaca, Colombia")
# name = input("Ingresa una dirección ") + ", Tunja, Boyaca, Colombia"
app.create_address("Calle 13, Tunja, Boyaca, Colombia")

app.create_address("Los Hongos, Tunja, Boyaca, Colombia")
# app.create_address("Centro Comercial Unicentro Tunja, Tunja, Boyaca, Colombia")
app.get_distance_between_addresses_and_scholl_address()
app.get_distance_between_addresses()
app.calculate_time()
app.create_completed_address()
app.print_aux()
app.dictionary_graph()

from address import Address
from map import obtain_coordinates, get_distance
from graph import tsp


class AppFlow:
    list_address = []
    list_coordinates = []
    list_distances = []
    list_distances_between_addresses = []
    list_completed_address = []
    list_time_between_school = []
    address = ""
    SPEED = 30  # Km/h

    def create_address(self, name):
        self.address = Address(name)
        self.list_address.append(self.address)

    def get_coordinates(self):
        for i, address_name in enumerate(self.list_address):
            self.list_coordinates.append(
                obtain_coordinates(address_name.get_name_address())
            )
            address_name.set_coordinates(
                obtain_coordinates(address_name.get_name_address())
            )
            print(self.list_coordinates)

    def get_distance_between_addresses_and_school_address(self, address_school):
        self.get_coordinates()
        for coordinates in self.list_coordinates:
            coordinates_school = obtain_coordinates(address_school)
            self.list_distances.append(get_distance(coordinates_school, coordinates))

    def get_distance_between_addresses(self):
        count_leng_list = 0
        count_actual_position = 0
        while count_actual_position < len(self.list_address):
            dictionary_distances = {
                self.list_address[count_actual_position].get_name_address(): {}
            }
            for j, address_time in enumerate(self.list_time_between_school):
                for address_coordinates in self.list_address:
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
                        dictionary_distances[
                            self.list_address[count_actual_position].get_name_address()
                        ]["school"] = self.list_time_between_school[
                            count_actual_position
                        ]
                        self.list_address[count_actual_position].set_address_dictionary(
                            dictionary_distances
                        )

                        # print("Metodo direcciones: ", dictionary_distances)
                    else:
                        print("Acabo y se reinicia")
                        count_leng_list = 0
            count_actual_position += 1

    def calculate_time(self):
        for distance in self.list_distances:
            raw_time = distance / self.SPEED
            time_in_minutes = round((raw_time * 60), 2)
            self.list_time_between_school.append(time_in_minutes)

    def create_completed_address(self):
        count = 0
        for j, address_time in enumerate(self.list_time_between_school):
            for k, address_name in enumerate(self.list_address):
                if address_name.get_distance_between_address_school_address() == None:
                    new_address = Address(
                        address_name.get_name_address(),
                        self.list_distances[count],
                        self.list_time_between_school[count],
                        address_name.get_coordinates(),
                        address_name.get_address_dictionary(),
                    )
                    if (
                        address_name.get_distance_between_address_school_address()
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
                aux.get_distance_between_address_school_address(),
                aux.get_list_of_times_address(),
            )

    def dictionary_graph(self):
        graph_school = {"school": {}}

        for name_address_graph in self.list_completed_address:
            graph_school["school"][
                name_address_graph.get_name_address()
            ] = name_address_graph.get_list_of_times_address()
            graph = name_address_graph.get_address_dictionary()

            for key, value in graph.items():
                if key not in graph_school:
                    graph_school[key] = {}
                graph_school[key].update(value)

        # print(graph_school)
        return graph_school

    def creation_tsp(self, graph):
        route = tsp(graph)
        return route
        # print(f"ruta optima{route}")

    def reset_values(self):
        self.list_completed_address.clear()
        self.list_address = []
        self.list_coordinates = []
        self.list_distances = []
        self.list_distances_between_addresses = []
        self.list_completed_address = []
        self.list_time_between_school = []

    # reset_address.set_name_address("")
    # reset_address.set_distance_between_address_school_address(None)
    # reset_address.set_list_of_times_address(None)
    # reset_address.set_coordinates(None)
    # reset_address.set_address_dictionary(None)
    # self.get_distance_between_addresses_and_school_address(None)


# app = AppFlow()
# # # name = input("Ingresa una dirección ") + ", Tunja, Boyaca, Colombia"
# app.create_address("Calle 17, Tunja, Boyaca, Colombia")
# # # name = input("Ingresa una dirección ") + ", Tunja, Boyaca, Colombia"
# app.create_address("Calle 27, Tunja, Boyaca, Colombia")
# # # name = input("Ingresa una dirección ") + ", Tunja, Boyaca, Colombia"
# app.create_address("Calle 13, Tunja, Boyaca, Colombia")
# aux_school = 5.551296812426012, -73.35511603422759
# app.create_address("Los Hongos, Tunja, Boyaca, Colombia")
# app.get_distance_between_addresses_and_school_address(aux_school)
# app.calculate_time()
# app.get_distance_between_addresses()
# app.create_completed_address()
# app.print_aux()
# # # app.dictionary_graph()
# print(app.creation_tsp(app.dictionary_graph()))

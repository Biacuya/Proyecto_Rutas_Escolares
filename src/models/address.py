class Address:
    def __init__(
        self,
        name,
        distance_between_address_scholl=None,
        time_list=None,
        coordinates=None,
        dictionary_of_address=None,
    ):
        self.name = name
        self.distance_between_address_scholl = distance_between_address_scholl
        self.time_list = time_list
        self.coordinates = coordinates
        self.dictionary_of_address = dictionary_of_address

    def get_name_address(self):
        return self.name

    def get_distance_between_address_scholl_address(self):
        return self.distance_between_address_scholl

    def set_name_address(self, name):
        self.name = name

    def set_distance_between_address_scholl_address(
        self, distance_between_address_scholl
    ):
        self.distance_between_address_scholl = distance_between_address_scholl

    def get_time_list_address(self):
        return self.time_list

    def set_time_list_address(self, time_list):
        self.time_list = time_list

    def get_coordinates(self):
        return self.coordinate

    def set_coordinates(self, coordinate):
        self.coordinate = coordinate

    def get_dictionary_of_address(self):
        return self.dictionary_of_address

    def set_dictionary_of_address(self, dictionary_of_address):
        self.dictionary_of_address = dictionary_of_address

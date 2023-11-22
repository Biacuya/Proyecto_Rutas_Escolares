class Address:
    def __init__(
        self,
        name,
        distance_between_address_school=None,
        list_of_times=None,
        coordinates=None,
        address_dictionary=None,
    ):
        self.name = name
        self.distance_between_address_school = distance_between_address_school
        self.list_of_times = list_of_times
        self.coordinates = coordinates
        self.address_dictionary = address_dictionary

    def get_name_address(self):
        return self.name

    def get_distance_between_address_school_address(self):
        return self.distance_between_address_school

    def set_name_address(self, name):
        self.name = name

    def set_distance_between_address_school_address(
        self, distance_between_address_school
    ):
        self.distance_between_address_school = distance_between_address_school

    def get_list_of_times_address(self):
        return self.list_of_times

    def set_list_of_times_address(self, list_of_times):
        self.list_of_times = list_of_times

    def get_coordinates(self):
        return self.coordinate

    def set_coordinates(self, coordinate):
        self.coordinate = coordinate

    def get_address_dictionary(self):
        return self.address_dictionary

    def set_address_dictionary(self, address_dictionary):
        self.address_dictionary = address_dictionary

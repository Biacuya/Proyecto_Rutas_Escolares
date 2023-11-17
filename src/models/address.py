class Address:
    def __init__(self, name, distance):
        self.name = name
        self.distance = distance

    def get_name_address(self):
        return self.name

    def get_distance_address(self):
        return self.distance

    def set_name_address(self, name):
        self.name = name

    def set_distance_address(self, distance):
        self.distance = distance

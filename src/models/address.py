class Address:
    distance = 0

    def __init__(self, name, distance=None, time=None):
        self.name = name
        self.distance = distance
        self.time = time

    def get_name_address(self):
        return self.name

    def get_distance_address(self):
        return self.distance

    def set_name_address(self, name):
        self.name = name

    def set_distance_address(self, distance):
        self.distance = distance

    def get_time_address(self):
        return self.time

    def set_time_address(self, time):
        self.time = time

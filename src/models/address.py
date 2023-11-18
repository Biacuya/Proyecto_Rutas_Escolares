class Address:

    def __init__(self, name, distance=None, time_list=None):
        self.name = name
        self.distance = distance
        self.time_list = time_list

    def get_name_address(self):
        return self.name

    def get_distance_address(self):
        return self.distance

    def set_name_address(self, name):
        self.name = name

    def set_distance_address(self, distance):
        self.distance = distance

    def get_time_list_address(self):
        return self.time_list

    def set_time_list_address(self, time_list):
        self.time_list = time_list
        
        

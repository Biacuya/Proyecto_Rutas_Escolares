from address import Address


class AppFlow:
    list_address = []

    def create_address(self, name, distance):
        address = Address(name, distance)
        self.list_address.append(address)
    
    

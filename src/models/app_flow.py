from address import Address


class AppFlow:
    list_address = []

    def create_address(self, name):
        address = Address(name)
        self.list_address.append(address)

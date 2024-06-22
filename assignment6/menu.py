class MenuItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Menu:
    def __init__(self):
        self.menu_items = []

    def add_new_item(self, name, price, quantity):
        item = MenuItem(name, price, quantity)
        self.menu_items.append(item)

    def update_existing_item(self, name, price, quantity):
        for item in self.menu_items:
            if item.name == name:
                item.price = price
                item.quantity = quantity
                return True
        return False

    def delete_item(self, name):
        for item in self.menu_items:
            if item.name == name:
                self.menu_items.remove(item)
                return True
        return False

    def display_menu(self):
        print("Menu Items are:")
        for item in self.menu_items:
            print(f"{item.name} - Price: {item.price}rs - Quantity: {item.quantity}")

    def write_menu_to_file(self, filename):
        with open(filename, 'w') as f:
            for item in self.menu_items:
                f.write(f"{item.name},{item.price},{item.quantity}\n")

    def read_menu_from_file(self, filename):
        try:

            with open(filename, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    name, price, quantity = line.strip().split(',')
                    price = float(price)
                    quantity = int(quantity)
                    self.add_new_item(name, price, quantity)
        except FileNotFoundError:
            print(f"{filename} not found. Starting with an empty menu.")

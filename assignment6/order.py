from exceptions import InvalidMenuItemError, InsufficientQuantityError

class Order:
    def __init__(self, menu):
        self.menu = menu
        self.items = []

    def customer_order(self, name, quantity):
        for item in self.menu.menu_items:
            if item.name == name:
                if item.quantity >= quantity:
                    self.items.append((item, quantity))
                    item.quantity -= quantity
                    return True
                else:
                    raise InsufficientQuantityError(name)
        raise InvalidMenuItemError(name)

    def calculate_total_bill(self):
        total = 0
        for item, quantity in self.items:
            total += item.price * quantity
        return total

    def generate_receipt(self):
        print("\nYour total bill is:")
        for item, quantity in self.items:
            print(f"{item.name} x {quantity} - {item.price * quantity}")
        total = self.calculate_total_bill()
        print(f"Total: {total}rs")

    def write_orders_to_file(self, filename):
        with open(filename, 'w') as f:
            for item, quantity in self.items:
                f.write(f"{item.name},{quantity}\n")

    def read_orders_from_file(self, filename):
        try:
            with open(filename, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    name, quantity = line.strip().split(',')
                    quantity = int(quantity)
                    self.customer_order(name, quantity)
        except:
                print(f"{filename} not found. Starting with no orders.")


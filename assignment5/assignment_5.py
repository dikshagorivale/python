import datetime

class Product:
    def __init__(self, name, category, price, quantity, expiration_date):
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity
        self.expiration_date = expiration_date
    
class Inventory:
    def __init__(self):
        self.products = []

    def add_product_to_inventory(self, product):
        self.products.append(product)

    def remove_product_from_inventory(self, product_name):
        self.products = [p for p in self.products if p.name != product_name]

    def search_products(self, search_term):
        return [p for p in self.products if search_term.lower() in p.name.lower() or search_term.lower() in p.category.lower()]

    def list_all_products(self):
        for p in self.products:
            print(f"{p.name} ({p.category}): {p.quantity} available at {p.price}rs/- each, valid until {p.expiration_date}")

    def categorize_products(self):
        categories = {}
        for p in self.products:
            if p.category not in categories:
                categories[p.category] = []
            categories[p.category].append(p)
        
        for category, products in categories.items():
            print(f"{category}:")
            for product in products:
                print(f"  {product.name} ({product.category}): {product.quantity} available at {product.price}rs/- each, valid until {product.expiration_date}")
    
    def check_expired_products(self):
        today = datetime.date.today()
        self.products = [p for p in self.products if p.expiration_date >= today]
        print("Expired products removed successfully")

    def save_inventory_to_file(self, filename):
        with open(filename, 'w') as file:
            for p in self.products:
                file.write(f"{p.name},{p.category},{p.price},{p.quantity},{p.expiration_date}\n")

    def load_inventory_from_file(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                name, category, price, quantity, expiration_date = line.strip().split(',')
                product = Product(name, category, float(price), int(quantity), datetime.datetime.strptime(expiration_date, '%Y-%m-%d').date())
                self.add_product_to_inventory(product)

def main():
    i = Inventory()

    while True:
        print("\nInventory Management System for a Grocery Store")
        print("1) Add a product")
        print("2) Remove a product")
        print("3) Search for a product")
        print("4) List all products")
        print("5) Categorize products")
        print("6) Check for expired products")
        print("7) Save inventory to file")
        print("8) Load inventory from file")
        print("9) Exit ")

        try:
            ch = int(input("Enter your choice: "))
        except ValueError:
            print("INVALID NUMBER ENTERED.Please enter a number from 1 to 9.")
            continue

        if ch == 1:
            name = input("Enter product name: ")
            category = input("Enter product category: ")
            try:
                price = float(input("Enter product price: "))
                quantity = int(input("Enter product quantity: "))
                expiration_date = input("Enter expiration date (YYYY-MM-DD): ")
                product = Product(name, category, price, quantity, datetime.datetime.strptime(expiration_date, '%Y-%m-%d').date())
                i.add_product_to_inventory(product)
                print("Product added to inventory successfully")
            except ValueError:
                print("INVALID NUMBER ENTERED. Price should be a number and quantity should be an integer.")

        elif ch == 2:
            product_name = input("Enter product name you want to remove: ")
            i.remove_product_from_inventory(product_name)
            print("Product removed from inventory successfully")

        elif ch == 3:
            search_term = input("Enter product name to search: ")
            results = i.search_products(search_term)
            for p in results:
                print(f"{p.name} ({p.category}): {p.quantity} available at {p.price}rs/- each, valid until {p.expiration_date}")

        elif ch == 4:
            i.list_all_products()
        
        elif ch == 5:
            print("Categorized Products are as follows:")
            i.categorize_products()

        elif ch == 6:
            i.check_expired_products()

        elif ch == 7:
            filename = input("Enter filename(with extension) to save inventory to file: ")
            i.save_inventory_to_file(filename)
            print(" INVENTORY SAVED TO FILE SUCCESFULLY")

        elif ch == 8:
            filename = input("Enter filename(with extension) to load inventory from file: ")
            i.load_inventory_from_file(filename)
            print(" INVENTORY LOADED FROM FILE SUCCESSFULLY")

        elif ch == 9:
            print("EXITED FROM THE SYSTEM")
            break
        else:
            print("INVALID NUMBER ENTERED")

if __name__ == "__main__":
    main()
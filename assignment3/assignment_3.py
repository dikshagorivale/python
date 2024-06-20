class Vehicle:
    def __init__(self, vehicle_id, make, model, year, category):
        self.__vehicle_id = vehicle_id
        self.__make = make
        self.__model = model
        self.__year = year
        self.__category = category

    def get_vehicle_id(self):
        return self.__vehicle_id

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def get_category(self):
        return self.__category

class RentalSystem:
    def __init__(self):
        self.vehicles = []
        self.vehicle_categories = {}

    def add_vehicle(self, vehicle):
        if vehicle not in self.vehicles:
            self.vehicles.append(vehicle)
            self.categorize_vehicles()
            print("Vehicle added Successfully..!")
        else:
            print("Vehicle already exists in the system.")

    def remove_vehicle(self, vehicle_id):
        removed = None
        for vehicle in self.vehicles:
            if vehicle.get_vehicle_id() == vehicle_id:
                removed = vehicle
                self.vehicles.remove(vehicle)
                self.categorize_vehicles()
                print("Vehicle removed Successfully..!")
                break
            else:
                print("Vehicle not found.")

    def search_vehicles(self, search_term):
        results = []
        for vehicle in self.vehicles:
            if search_term.lower() in vehicle.get_make().lower() or search_term.lower() in vehicle.get_model().lower():
                results.append(vehicle)
        if results:
            print("Search Results are as follows:")
            for vehicle in results:
                print(f"{vehicle.get_make()} {vehicle.get_model()} ({vehicle.get_year()}) - {vehicle.get_category()}")
        else:
            print("Vehicle not found")

    def list_vehicles(self):
        print("All Vehicles are as follows:")
        for vehicle in self.vehicles:
            print(f"{vehicle.get_make()} {vehicle.get_model()} ({vehicle.get_year()}) - {vehicle.get_category()}")

    def categorize_vehicles(self):
        self.vehicle_categories = {}
        for vehicle in self.vehicles:
            if vehicle.get_category() not in self.vehicle_categories:
                self.vehicle_categories[vehicle.get_category()] = [vehicle]
            else:
                self.vehicle_categories[vehicle.get_category()].append(vehicle)

def main_class():
    
    rs = RentalSystem()
    while True:
        print("1) Add a Vehicle")
        print("2) Remove a Vehicle")
        print("3) Search Vehicles")
        print("4) List all Vehicles")
        print("5) Exit")

        ch = int(input("Enter your choice: "))

        if ch == 1:
            vehicle_id = input("Enter vehicle ID: ")
            make = input("Enter make: ")
            model = input("Enter model: ")
            year = int(input("Enter year: "))
            category = input("Enter category: ")
            vehicle = Vehicle(vehicle_id, make, model, year, category)
            rs.add_vehicle(vehicle)
        elif ch == 2:
            vehicle_id = input("Enter Vehicle ID to remove: ")
            rs.remove_vehicle(vehicle_id)
        elif ch == 3:
            search_term = input("Enter the search term: ")
            rs.search_vehicles(search_term)
        elif ch == 4:
            rs.list_vehicles()
        elif ch == 5:
            print("Exited from Vehicle Rental System")
            break
        else:
            print("INVALID NUMBER")
main_class()

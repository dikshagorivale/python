from menu import Menu
from order import Order
from exceptions import InvalidMenuItemError, InsufficientQuantityError

def main_class():
    menu = Menu()

    try:
        menu.read_menu_from_file('menu.txt')
    except FileNotFoundError:
        print("menu.txt not found. Starting with an empty menu.")

    order = Order(menu)

    try:
        order.read_orders_from_file('orders.txt')
    except FileNotFoundError:
        print("orders.txt not found. Starting with no orders.")

    while True:
        print("\n Restaurant Management System")
        print("1) Add Menu Item")
        print("2) Update Menu Item")
        print("3) Delete Menu Item")
        print("4) Display Menu")
        print("5) Place Order")
        print("6) View Order")
        print("7) Generate Receipt")
        print("8) Exit")

        try:
            ch = int(input("Enter your choice: "))
        except ValueError:
            print("INVALID NUMBER ENTERED! Please enter a number from 1 to 8.")
            continue

        if ch == 1:
            name = input("Enter item name: ")
            try:
                price = float(input("Enter item price: "))
                quantity = int(input("Enter item quantity: "))
                menu.add_new_item(name, price, quantity)
                menu.write_menu_to_file('menu.txt')
                print("ITEM ADDED SUCCESSFULLY IN THE MENU")
            except ValueError:
                print("INVALID NUMBER ENTERED! Price and quantity should be an Number.")

        elif ch == 2:
            name = input("Enter item name to update: ")
            try:
                price = float(input("Enter new price: "))
                quantity = int(input("Enter new quantity: "))
                if menu.update_existing_item(name, price, quantity):
                    menu.write_menu_to_file('menu.txt')
                    print("ITEM UPDATED SUCCESSFULLY IN THE MENU")
                else:
                    print(f"{name} not found in menu.")
            except ValueError:
                print("INVALID NUMBER ENTERED! Price and quantity should be an Number.")

        elif ch == 3:
            name = input("Enter item name to delete: ")
            if menu.delete_item(name):
                menu.write_menu_to_file('menu.txt')
                print("ITEM DELETED SUCCESSFULLY FROM THE MENU")
            else:
                print(f"{name} not found in menu.")

        elif ch == 4:
            menu.display_menu()

        elif ch == 5:
            try:
                name = input("Enter item name to order: ")
                quantity = int(input("Enter quantity: "))
                order.customer_order(name, quantity)
                order.write_orders_to_file('orders.txt')
                print("YOUR ORDER PLACED SUCCESSFULLY")
            except ValueError:
                print("INVALID NUMBER ENTERED! Quantity should be an number.")
            except (InsufficientQuantityError, InvalidMenuItemError) as e:
                print(e)

        elif ch == 6:
            print("\nYour order is:")
            for item, quantity in order.items:
                print(f"{item.name} x {quantity}")

        elif ch == 7:
            order.generate_receipt()

        elif ch == 8:
            print("EXITED FROM THE SYSTEM")
            break

        else:
            print("INVALID NUMBER ENTERED")

if __name__ == "__main__":
    main_class()

import menu_item as me


def show_user_menu():
    print("\nMenu Options:")
    print("V - View an Item")
    print("A - Add an Item")
    print("D - Delete an Item")
    print("U - Update an Item")
    print("S - Show the Menu")
    print("E - Exit")

    choice = input("Please select an option: ").upper()
    if choice == 'V':
        pass  # Placeholder for "View an Item" functionality
    elif choice == 'A':
        add_item_to_menu()
    elif choice == 'D':
        remove_item_from_menu()
    elif choice == 'U':
        update_item_from_menu()
    elif choice == 'S':
        show_menu_restaurant()
    elif choice == 'E':
        print("Exiting the program. Here is the restaurant's menu:")
        show_menu_restaurant()
        exit()
    else:
        print("Invalid option. Please try again.")


def add_item_to_menu():
    name = input("Enter the name of the item: ")
    price = input("Enter the price of the item: ")
    price = int(price)  # Convert price to an integer
    item = me.MenuItem(name, price)
    item.save()
    print(f"{name} was added successfully!")

def remove_item_from_menu():
    name = input("Enter the name of the item to remove: ")
    item = me.MenuItem(name, 0)
    item.delete()
    print(f"{name} was deleted successfully!")

def update_item_from_menu():
    current_name = input("Enter the name of the item to update: ")
    current_price = int(input("Enter the current price of the item: "))
    new_name = input("Enter the new name of the item: ")
    new_price = int(input("Enter the new price of the item: "))
    item = me.MenuItem(current_name, current_price)
    item.update(new_name, new_price)
    print(f"{current_name} was updated successfully to {new_name} with price {new_price}.")

def show_menu_restaurant():
    item = me.MenuItem()
    item.show()


if __name__=='__main__':
    while True:
        show_user_menu()
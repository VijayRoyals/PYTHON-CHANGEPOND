menu_card = {
    'paneer 65': 1,
    'chilly paneer': 2,
    'veg crispy': 3
}

def display_menu():
    print("Current Menu:")
    for item, index in menu_card.items():
        print(f"{index}. {item}")

def add_starter():
    starter = input("Enter starter to add: ")
    if starter not in menu_card:
        index = len(menu_card) + 1
        menu_card[starter] = index
        print(f"{starter} added successfully!")
        display_menu()
    else:
        print(f"{starter} is already in the menu.")

def update_starter():
    display_menu()
    old_starter = input("Enter starter to update: ")
    if old_starter in menu_card:
        new_starter = input("Enter new starter name: ")
        menu_card[new_starter] = menu_card.pop(old_starter)
        print(f"{old_starter} updated to {new_starter} successfully!")
        display_menu()
    else:
        print(f"{old_starter} is not found in the menu.")

def remove_starter():
    display_menu()
    starter_to_remove = input("Enter starter to remove: ")
    if starter_to_remove in menu_card:
        del menu_card[starter_to_remove]
        print(f"{starter_to_remove} removed successfully!")
        display_menu()
    else:
        print(f"{starter_to_remove} is not found in the menu.")

while True:
    print("\nMenu:")
    print("1. Display menu")
    print("2. Add starter to menu")
    print("3. Update starter in menu")
    print("4. Remove starter from menu")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")
    
    if choice == '1':
        display_menu()
    elif choice == '2':
        add_starter()
    elif choice == '3':
        update_starter()
    elif choice == '4':
        remove_starter()
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")

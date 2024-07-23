
menu_card = ['paneer 65', 'chilly paneer', 'veg crispy']


def display_menu():
    print("Current Menu:")
    for item in menu_card:
        print(item)


def add_starter():
    starter = input("Enter starter to add: ")
    menu_card.append(starter)
    print(f"{starter} added successfully!")
    display_menu()


def update_starter():
    display_menu()
    old_starter = input("Enter starter  to update: ")
    if old_starter in menu_card:
        new_starter = input("Enter new starter name: ")
        index = menu_card.index(old_starter)
        menu_card[index] = new_starter
        print(f"{old_starter} updated to {new_starter} successfully!")
        display_menu()
    else:
        print(f"{old_starter} is not found in the menu.")


def remove_starter():
    display_menu()
    starter_to_remove = input("Enter starter to remove: ")
    if starter_to_remove in menu_card:
        menu_card.remove(starter_to_remove)
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

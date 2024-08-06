class MenuCard:
    def __init__(self):
        self.menu = {
            'Espresso': 550,
            'Mocha': 450,
            'Cappuccino': 560,
            'Americano': 650,
        }

    def display(self):
        print('Menu Card:')
        for dish, price in self.menu.items():
            print(f'{dish}: {price}')
        print()

    def add(self, dish, price):
        self.menu[dish] = price
        print(f'{dish} added successfully.\n')

    def update(self, dish, price):
        if dish in self.menu:
            self.menu[dish] = price
            print(f'{dish} price updated successfully.\n')
        else:
            print(f'{dish} not found in the menu.\n')

    def remove(self, dish):
        if dish in self.menu:
            self.menu.pop(dish)
            print(f'{dish} removed successfully.\n')
        else:
            print(f'{dish} not found in the menu.\n')

def main():
    menu_card = MenuCard()
    while True:
        option = int(input(
            'Enter the option:\n'
            '1. Display the Menu Card\n'
            '2. Add a Coffee to the Menu Card\n'
            '3. Update the price of a Coffee in the Menu Card\n'
            '4. Remove a Coffee from the Menu Card\n'
            '5. Exit\n'
        ))

        if option == 1:
            menu_card.display()
        elif option == 2:
            dish = input("Enter the Name of the Coffee: ")
            price = int(input("Enter the Price of the Coffee: "))
            menu_card.add(dish, price)
            menu_card.display()
        elif option == 3:
            menu_card.display()
            dish = input("Enter the Name of the Coffee you want to update the price for: ")
            price = int(input("Enter the new Price of the Coffee: "))
            menu_card.update(dish, price)
            menu_card.display()
        elif option == 4:
            menu_card.display()
            dish = input("Enter the Name of the Coffee you want to remove: ")
            menu_card.remove(dish)
            menu_card.display()
        elif option == 5:
            break
        else:
            print('Enter a valid option.')

if __name__ == '__main__':
    main()

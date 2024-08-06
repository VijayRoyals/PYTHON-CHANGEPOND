class FoodItem:
    food_id = 1
    
    def __init__(self, name, price, description):
        self.food_id = FoodItem.food_id
        FoodItem.food_id += 1
        self.name = name
        self.price = price
        self.description = description
    
    def food_details(self):
        return {
            'Food ID': self.food_id,
            'Name': self.name,
            'Price': self.price,
            'Description': self.description
        }

class Cart:
    def __init__(self):
        self.food_items = []
    
    def add_food_item(self, food_item):
        self.food_items.append(food_item)
        print(f"Food item added to the cart.")
    
    def display_cart(self):
        for food_item in self.food_items:
            details = food_item.food_details()
            print(f"ID: {details['Food ID']}, Name: {details['Name']}, Price: {details['Price']}, Description: {details['Description']}")

def main():
    cart = Cart()
    
    while True:
        print("\nOptions:")
        print("1. Add Food Item")
        print("2. View Cart")
        print("3. Exit")
        
        choice = int(input("Enter your choice (1/2/3): "))
        
        if choice == '1':
            name = input("Enter food name: ")
            price = float(input("Enter food price: "))
            description = input("Enter food description: ")
            
            food_item = FoodItem(name, price, description)
            cart.add_food_item(food_item)
        
        elif choice == '2':
            cart.display_cart()
        
        elif choice == '3':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
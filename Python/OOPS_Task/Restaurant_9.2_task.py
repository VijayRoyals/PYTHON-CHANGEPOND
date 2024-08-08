# main.py

class Restaurant:

    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")    
    def open_restaurant(self):
        print(f'{self.restaurant_name} is Open')

restaurant1 = Restaurant('wizard cusine', 'Italian')
restaurant2 = Restaurant('cafe garage', 'Indian')
restaurant3 = Restaurant('tabun', 'Japanese')


restaurant1.describe_restaurant()
restaurant1.open_restaurant()
restaurant2.describe_restaurant()
restaurant2.open_restaurant()
restaurant3.describe_restaurant()
restaurant3.open_restaurant()




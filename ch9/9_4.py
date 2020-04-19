class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print('Название ресторана:', self.restaurant_name)
        print('Кухня:', self.cuisine_type)

    def open_restaurant(self):
        print(f'Ресторан {self.restaurant_name} открыт!')

    def set_number_served(self, set_number_served):
        self.number_served = set_number_served

    def increment_number_served(self, increment):
        self.number_served += increment


restaurant = Restaurant('McDonalds', 'random')
print(restaurant.number_served)
restaurant.number_served = 2
print(restaurant.number_served)
restaurant.set_number_served(10)
print(restaurant.number_served)
restaurant.increment_number_served(3)
print(restaurant.number_served)

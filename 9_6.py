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


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['milk', 'chocolate']

    def print_flavors(self):
        for flavor in self.flavors:
            print(flavor)


rest1 = IceCreamStand('Iccy', 'ice-cream')
rest1.open_restaurant()
rest1.print_flavors()

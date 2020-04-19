class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print('Название ресторана:', self.restaurant_name)
        print('Кухня:', self.cuisine_type)

    def open_restaurant(self):
        print(f'Ресторан {self.restaurant_name} открыт!')


restaurant1 = Restaurant('Пушкин', 'русская')
restaurant1.describe_restaurant()
restaurant1.open_restaurant()
restaurant2 = Restaurant('McDonalds', 'буржуйская')
restaurant3 = Restaurant('Прага', 'разная')
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

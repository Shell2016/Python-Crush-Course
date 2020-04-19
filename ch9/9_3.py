class User():
    
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def desctribe_user(self):
        print('Имя:', self.first_name, '\nФамилия:', self.last_name,
         '\nВозраст:', self.age)
    def greet_user(self):
        print(f'Привет тебе, {self.first_name}!')    

user1 = User('Михаил', 'Шелудяков', 38)
user1.desctribe_user()
user1.greet_user()
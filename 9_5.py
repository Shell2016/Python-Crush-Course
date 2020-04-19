class User(object):
    
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0

    def desctribe_user(self):
        print('Имя:', self.first_name, '\nФамилия:', self.last_name,
         '\nВозраст:', self.age)
    def greet_user(self):
        print(f'Привет тебе, {self.first_name}!')   
    def increment_login_attempts(self):
        self.login_attempts += 1 
    def reset_login_attempts(self):
        self.login_attempts = 0

user1 = User('Михаил', 'Шелудяков', 38)
user1.desctribe_user()
user1.greet_user()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(user1.login_attempts)
user1.reset_login_attempts()
print(user1.login_attempts)
from random import randint


class Die():
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))


dies6 = Die()
for i in range(10):
    dies6.roll_die()
print('================')
dies10 = Die(10)
for i in range(10):
    dies10.roll_die()
print('================')
dies20 = Die(20)
for i in range(10):
    dies20.roll_die()

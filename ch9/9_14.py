from random import choice

lottery_characters = list(range(10))
lottery_characters += ['A', 'B', 'C', 'D', 'E']
win_combination = []

# print(f'Билет содержащий эту комбинацию является выигрышным:')
# for i in win_combination:
#     print(i, end=' ')
# print()

my_ticket = [3, 7, 'E', 'A']
count = 0

while True:
    count += 1
    temp_list = lottery_characters[:]
    win_combination.clear()
    for i in range(4):
        lucky_character = choice(temp_list)
        win_combination.append(lucky_character)
        temp_list.remove(lucky_character)
    if win_combination == my_ticket:
        print(f'{count} iterations for matching your ticket')
        break

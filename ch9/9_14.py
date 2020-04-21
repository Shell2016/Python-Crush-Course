import random

lottery_characters = list(range(10))
lottery_characters += ['A', 'B', 'C', 'D', 'E']
# win_combination = random.choices(lottery_characters, k=4)

# print(f'Билет содержащий эту комбинацию является выигрышным:')
# for i in win_combination:
#     print(i, end=' ')
# print()

my_ticket = [3, 7, 'E', 'A']
count = 0

while True:
    count += 1
    win_combination = random.choices(lottery_characters, k=4)
    if win_combination == my_ticket:
        print(f'{count} iterations for matching your ticket')
        break

sum = 0
with open('ch10/war and peace.txt', encoding='utf-8') as f:
    for line in f:
        sum += line.lower().count('the ')
print(sum)

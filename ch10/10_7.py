
while True:
    input_1 = input('Введите первое число: ')
    if len(input_1) < 1:
        break
    input_2 = input('Введите второе число: ')
    if len(input_2) < 1:
        break
    try:
        sum = float(input_1) + float(input_2)

    except ValueError:
        print('Введите ЧИСЛОВОЕ значение!')
    else:
        print('Сумма равна:', sum)

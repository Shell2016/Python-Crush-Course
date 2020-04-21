import json

filename = 'ch10/number.json'


def get_stored_number():
    try:
        with open(filename) as f:
            number = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return number


def get_new_number():
    number = input('Введите свое любимое число: ')
    with open(filename, 'w') as f:
        json.dump(number, f)
    return number


def ask_user():
    number = get_stored_number()
    if number:
        print(f'Ваше любимое число  - {number}')
    else:
        number = get_new_number()
        print(f'Любимое число {number} запомнено!')


ask_user()

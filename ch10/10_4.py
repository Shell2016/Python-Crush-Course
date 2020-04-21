with open('ch10/guest_book.txt', 'a') as af:
    while True:
        guest_name = input('Enter your name: ')
        if len(guest_name) < 1:
            break
        else:
            af.write(guest_name + '\n')
            print(f'Hello, {guest_name}!')

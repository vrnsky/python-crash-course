poll_active = True
file_name = './guests_book.txt'

while poll_active:
    guest_name = input("Enter your name: ")
    if guest_name == 'q':
        break

    with open(file_name, 'a') as guests_book:
        guests_book.write(guest_name + "\n")
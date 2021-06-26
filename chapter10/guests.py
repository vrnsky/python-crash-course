user_name = input("Enter your name: ")

with open('guests.txt', 'w') as guest_file:
    guest_file.write(user_name)

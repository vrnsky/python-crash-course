guests = ['Katya', 'Kambar', 'Tanya']
print("I would like to invite you", guests[0], "for dinner")
print("I would like to invite you", guests[1], "for dinner")
print("I would like to invite you", guests[2], "for dinner")
print("Oh no,", guests.pop(), "can't go for dinner")
guests.append("Alex")
print("I would like to invite you", guests[2], "for dinner")
print("I have founnd a  bigger dinner table. Let's invite more people")
guests.insert(0, "Yslam")
guests.insert(1, "Ann")
guests.append("John")
print("I would like to invite you", guests[0], "for dinner")
print("I would like to invite you", guests[1], "for dinner")
print("I would like to invite you", guests[2], "for dinner")
print("I would like to invite you", guests[3], "for dinner")
print("I would like to invite you", guests[4], "for dinner")
print("I would like to invite you", guests[5], "for dinner")
print("Oh, no new dinning table is not fit well for us")
print("I am sorry, but I can't invite you", guests.pop())
print("I am sorry, but I can't invite you", guests.pop())
print("I am sorry, but I can't invite you", guests.pop())
print("I am sorry, but I can't invite you", guests.pop())
print("You are invited to my party", guests[0])
print("You are invited to my party", guests[1])
print(guests)
first_guest = guests.pop()
second_guest = guests.pop()
del first_guest
del second_guest
print(guests)
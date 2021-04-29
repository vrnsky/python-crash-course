poll_active = True
dream_vacation = {'Egor':'Moscow'}
while poll_active:
	name = input('Enter your name')
	city = input('Enter dream vacation')
	dream_vacation[name] = city
        answer = input('Would like to still poll active (y/n)? ')
		if answer == 'n':
			break
		else
			for name, city in dream_vacation.items():
			print(name, "would like to have vacation in", city)


sandwiches = ['tuna', 'standard', 'experiment', 'pastrami', 'pastrami', 'pastrami']
finished_sandwiches = []

print("Sorry, we are out of pastrami")
while sandwiches:
	sandwich = sandwiches.pop()
	if sandwich != 'pastrami':
		print("I made your", sandwich, "sandwich")
		finished_sandwiches.append(sandwich)

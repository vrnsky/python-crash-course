sandwiches = ['tuna', 'standard', 'experiment']
finished_sandwiches = []

while sandwiches:
	sandwich = sandwiches.pop()
	print("I made your", sandwich, "sandwich")
	finished_sandwiches.append(sandwich)

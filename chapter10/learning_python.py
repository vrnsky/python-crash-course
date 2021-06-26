file_path = './learning_python.txt'
with open(file_path) as file:
    contents = file.readlines()

for ability in contents:
    print(ability.strip().replace("Python", "Kotlin"))
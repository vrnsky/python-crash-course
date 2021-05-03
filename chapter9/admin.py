class User:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print("It is", self.last_name.title(), self.first_name.title())

    def greet_user(self):
        print("Welcome back", self.last_name.title(), self.first_name.title())

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

class Privilege:

    def __init__(self, privileges):
        self.privileges = privileges

class Admin(User):

    def __init__(self, first_name, last_name, privileges):
        super().__init__(first_name, last_name)
        self.privileges = privileges

    def print_privileges(self):
        for privilege in self.privileges.privileges:
            print("Admin can", privilege)


privileges = Privilege(['can add post', 'can ban user', 'can drop database'])
admin = Admin("Egor", "Voronianskii", privileges)
admin.print_privileges()
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


me = User("Egor", "Voronianskii")
kambar = User("Kambar", "Mirmanov")

me.describe_user()
kambar.describe_user()

me.greet_user()
kambar.greet_user()


me.increment_login_attempts()
me.increment_login_attempts()
me.increment_login_attempts()
print("Me tried to login", me.login_attempts)
me.reset_login_attempts()
print("After reset:", me.login_attempts)
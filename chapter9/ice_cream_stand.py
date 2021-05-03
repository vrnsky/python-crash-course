class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("There is", self.restaurant_name, " and its cuisine type is", self.cuisine_type)

    def open_restaurant(self):
        print("Now restaurant", self.restaurant_name.title(), "is open")

    def how_many_served(self):
        print(self.restaurant_name, "have already served", self.number_served, "people")

    def increment_number_served(self, served):
        if served <= 0:
            print("It is not valid value for served")
        else:
            self.number_served += served


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def print_flavors(self):
        for flavor in self.flavors:
            print("This restaurant can cook", flavor, "taste")


brand_new_restaurant = IceCreamStand('Brand New Restaurant', 'Casual', ['good', 'bad', 'worst'])
brand_new_restaurant.print_flavors()

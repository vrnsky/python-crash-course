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

restaurant1 = Restaurant("Astana", "Russian")
restaurant2 = Restaurant("Pasta Panas", "Italian")
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant1.open_restaurant()
restaurant2.open_restaurant()
restaurant1.increment_number_served(10)
restaurant1.how_many_served()
restaurant2.increment_number_served(8)
restaurant2.how_many_served()
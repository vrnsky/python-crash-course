class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("There is", self.restaurant_name, " and its cuisine type is", self.cuisine_type)

    def open_restaurant(self):
        print("Now restaurant", self.restaurant_name.title(), "is open")


restaurant1 = Restaurant("Astana", "Russian")
restaurant2 = Restaurant("Pasta Panas", "Italian")
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant1.open_restaurant()
restaurant2.open_restaurant()
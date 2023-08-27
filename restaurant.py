class Restaurant:
    all_restaurants = []

    def __init__(self, name):
        self.name_value = name  
        self.review_list = []  # Create review_list attribute
        Restaurant.all_restaurants.append(self)

    def get_name(self):
        return self.name_value

    def add_review(self, review):
        self.review_list.append(review)  # Append the review to restaurant's review_list

    @classmethod
    def all(cls):
        return cls.all_restaurants

# Testing the Restaurant class
if __name__ == "__main__":
    restaurant1 = Restaurant("Pizza Hut")
    restaurant2 = Restaurant("McDonald's")

    print(restaurant1.get_name())
    print(Restaurant.all())

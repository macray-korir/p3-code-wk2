from customer import Customer
from restaurant import Restaurant

class Review:
    all_reviews = []

    def __init__(self, customer, restaurant, rating):
        self.customer_obj = customer 
        self.restaurant_obj = restaurant  
        self.rating_value = rating
        Review.all_reviews.append(self)
        customer.add_review(self)  
        restaurant.add_review(self)  

    def rating(self):
        return self.rating_value

    def customer(self):
        return self.customer_obj

    def restaurant(self):
        return self.restaurant_obj

    @classmethod
    def all(cls):
        return cls.all_reviews

# Testing the Review class
customer1 = Customer("Ray", "Mond")
restaurant1 = Restaurant("Mama Shiko")
review1 = Review(customer1, restaurant1, 4)
review2 = Review(customer1, restaurant1, 5)
print(review1.rating())
print(review2.customer().full_name())
print(review1.restaurant().get_name())
print(Review.all())

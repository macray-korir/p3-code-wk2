class Customer:
    all_customers = []

    def __init__(self, given_name, family_name):
        self.given_name_value = given_name 
        self.family_name_value = family_name  
        self.review_list = []  # Create review_list attribute
        Customer.all_customers.append(self)

    def full_name(self):
        return f"{self.given_name_value} {self.family_name_value}"

    def given_name(self):
        return self.given_name_value

    def family_name(self):
        return self.family_name_value

    def add_review(self, review):
        self.review_list.append(review)  # Append the review to customer's review_list

    @classmethod
    def all(cls):
        return cls.all_customers
#test
customer1 = Customer("Ray", "mond")
customer2 = Customer("Mercy", "Musenya")
all_customers = Customer.all()
for customer in all_customers:
    print(customer.full_name())

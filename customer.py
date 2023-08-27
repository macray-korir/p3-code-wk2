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

# Testing the Customer class
if __name__ == "__main__":
    customer1 = Customer("John", "Doe")
    customer2 = Customer("Jane", "Smith")

    print(customer1.given_name())
    print(customer2.family_name())
    print(customer1.full_name())

    print(Customer.all())

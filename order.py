# First thing- import Customer and Coffee from their files

from customer import Customer
from coffee import Coffee

class Order:
    # Represents an order placed by a customer for a coffee
    # here we should implement a constructor method to initialize an order with customer, coffee and price
    def __init__(self, customer, coffee,price):
        self.customer=customer
        self.coffee=coffee
        self.price=price
    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, value):
        if isinstance(value, Customer):
            self._customer=value
        else:
            raise TypeError("The customer should be an instance of Customer")
    
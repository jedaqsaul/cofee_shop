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
        # customer
    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, value):
        if isinstance(value, Customer):
            self._customer=value
        else:
            raise TypeError("The customer should be an instance of Customer")
        

        # coffee
    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, value):
        if isinstance(value, Coffee):
            self._coffee=value
        else:
            raise TypeError("The coffee shoudl be an instance of cofee")
        
        # price
    @property
    def price(self):
        return self._price
    


        
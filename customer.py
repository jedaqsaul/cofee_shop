
class Customer:
    # represents a customer who can place coffee orders
    def __init__(self, name):
        self.name=name

    @property
    def name(self):
        return self._name
    
    @name.setter #this makes the method a setter for -name property
    def name(self,value): #check if value is a string and its length is btw 1 and 17
        # if all([isinstance(value, str), 1 <= len(value) <= 15]):
        if isinstance(value, str) and 1<= len(value)<= 15:
            self._name=value #set the private attribute _name if it is valid
        else: #raise and error if value is not a valid string or the stipulated lenght
            raise ValueError('The customers name should be a string between 1 and 15 chars')
    def orders(self):
        from order import Order
        # ********************this one gives all this customer's orders
        return[order for order in Order.all_orders if order.customer ==self]
    def coffees(self):
        from order import Order
        # gives a unique list of coffee they have ordered
        return list({order.coffee for order in self.orders()})
    
    def create_order(self, coffee, price):
        from order import Order  # Local import to avoid circular dependency
        return Order(self, coffee, price)

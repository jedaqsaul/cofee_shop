
class Coffee:
    # represents a type of coffee that can be ordered
    def __init__(self, name):
        self.name=name
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) >=3:
            self._name=value
        else:# raise an error here
            raise ValueError('Coffee is supposed to be a string with no less than 3 chars')
    def orders(self):
        from order import Order
        return [order for order in Order.all_orders if order.coffee == self]

    def customers(self):
        # from order import Order
       
        return list({order.customer for order in self.orders()})
    # returns how many orders were placed for this coffee
    def num_orders(self):
        return len(self.orders())
    # returns the average price of coffee based on all orderes
    # here we should implement sum and len

    def average_price(self):
        orders = self.orders()
        if orders:
            total = sum(order.price for order in orders)
            return total / len(orders)
        return 0.0

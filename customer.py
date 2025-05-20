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
   
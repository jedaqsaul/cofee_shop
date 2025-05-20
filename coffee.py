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
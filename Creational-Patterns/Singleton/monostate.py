class CEO:
    # object properties are shared in static variable
    __shared_state = {
        'name': 'steve',
        'age': 55
    }
    
    def __init__(self):
        # every new object is assigned the same shared properties
        # copying not just data but the REFERENCE to the entire dict
        self.__dict__ = self.__shared_state
    
    def __str__(self):
        return f'{self.name}, {self.age}'

class Monostate:
    __shared_state = {}
    
    def __new__(cls, *args):
        # create object instance
        obj = super(Monostate, cls).__new__(cls, *args)
        # assign shared properties, dict reference
        obj.__dict__ = cls.__shared_state
        return obj

# inherits from monostate     
class CFO(Monostate):
    def __init__(self):
        self.name = ''
        self.money = 0
        
    def __str__(self):
        return f'{self.name} manages ${self.money}'

'''    
c1 = CEO()
print(c1) # steve, 55

c2 = CEO()
c2.age = 77
print(c1) # steve, 77
print(c2) # steve, 77
'''

cf1 = CFO()
cf1.name = 'cheryl'
cf1.money = 1
print(cf1) # cheryl manages $1

cf2 = CFO()
cf2.name = 'ruth'
cf2.money = 10 
print(cf1) # ruth manages $10
print(cf2) # ruth manages $10




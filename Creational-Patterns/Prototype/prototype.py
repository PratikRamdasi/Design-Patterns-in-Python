class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        
    def __str__(self):
        return f'{self.name} lives at {self.address}'
        
john = Person('john', '123 london road')
print(john)
# jane = john # not a good idea, this will change the address for both john and jane
# jane.name = 'jane'
print(jane)

#######################

class Address:
    def __init__(self, st, city):
        self.st = st
        self.city = city
        
    def __str__(self):
        return f'{self.st}, {self.city}'
        
class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        
    def __str__(self):
        return f'{self.name} lives at {self.address}'
        
address = Address('123 london road','london')
john = Person('john', address)
print(john)
jane = Person('jane', address)
jane.address.st = '123v london road' # this will change reference to both JOHN and JANE
# they both keep reference of the address
print('-----')
print(john)
print(jane)

#######################

import copy
class Address:
    def __init__(self, st, city):
        self.st = st
        self.city = city
        
    def __str__(self):
        return f'{self.st}, {self.city}'
        
class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        
    def __str__(self):
        return f'{self.name} lives at {self.address}'
        
# deep copy object
# copy.deepcopy() # copies all attributes recursively and created new object
        # does not keep the reference, its a complete copy and all object properties are modifiable 
# copy.copy() is a shallow copy and reference also gets copied to the new object
    # still keeps the reference of the old objects

john = Person('john', Address('123 london road','london'))
jane = copy.deepcopy(john)
jane.name = 'jane'
jane.address.st = '124 london road'
print(john)
print(jane)
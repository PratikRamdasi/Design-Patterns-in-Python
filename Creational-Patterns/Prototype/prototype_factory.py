import copy
class Address:
    def __init__(self, st, suite, city):
        self.st = st
        self.suite = suite
        self.city = city
        
    def __str__(self):
        return f'{self.st}, suite:#{self.suite}, {self.city}'
        
class Employee:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        
    def __str__(self):
        return f'{self.name} works at {self.address}'
        
# deep copy object
# copy.deepcopy() # copies all attributes recursively and created new object

# copy.copy() is a shallow copy and overwrite the reference 

class EmployeeFactory:
    # contains main and aux employee prototypes
    main_emp = Employee('', Address('123 East Dr', 0, 'london'))
    aux_emp = Employee('', Address('123B East Dr', 0, 'london'))
    
    @staticmethod
    # takes the prototype and 
    def __new_emp(proto, name, suite):
        result = copy.deepcopy(proto)
        result.name = name
        result.address.suite = suite
        return result
    
    @staticmethod
    # creates prototype obj
    def new_main_emp(name, suite):
        return EmployeeFactory.__new_emp(
            EmployeeFactory.main_emp, 
            name, suite
            )
        
    @staticmethod
    def new_aux_emp(name, suite):
        return EmployeeFactory.__new_emp(
            EmployeeFactory.aux_emp, 
            name, suite
            )
            
john = EmployeeFactory.new_main_emp('john', 100)
jane = EmployeeFactory.new_aux_emp('jane', 500)
print(john)
print(jane)
        
    


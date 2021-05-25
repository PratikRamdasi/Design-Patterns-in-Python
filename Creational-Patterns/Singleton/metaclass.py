## other alternative to decorator -> metaclass

# metaclass 
class singleton(type):
    _instances = {}
    
    # instances behave like functions and can be called like a function
    # object() is shorthand for object.__call__()
    # redefining the same object second time, so its not init again
    def __call__(cls, *args):
        if cls not in cls._instances:
            cls._instances[cls] = super(singleton, cls).__call__(*args)
        return cls._instances[cls]

class Database(metaclass=singleton):
    def __init__(self):
        print('load database')

# calls __call__method
d1 = Database()
#d1(arg1, arg2)

d2 = Database()
print(d1 == d2)

''' 
Example for __call__ method

class Example: 
    def __init__(self): 
        print("Instance Created") 
      
    # Defining __call__ method 
    def __call__(self): 
        print("Instance is called via special method") 
  
# Instance created 
e = Example() 
  
# __call__ method will be called 
e() 
'''
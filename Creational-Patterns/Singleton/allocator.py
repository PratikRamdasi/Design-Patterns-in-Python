import random
class singleton:
    __instance = None
    
     # called when the object is initialized
    def __init__(self):
        id = random.randint(1, 101)
        print('id:', id)
    
    # this method is pointing to the class
    # called when the object is created <------- Preference

    ##  IMP 
    # If both __init__ method and __new__ method exists in the class, 
    # then the __new__ method is executed first and decides whether to 
    # use __init__ method or not, because other class constructors 
    # can be called by __new__ method or it can simply return other 
    # objects as an instance of this class.
    def __new__(cls, *args):
        if not cls.__instance:
            cls.__instance = super(singleton , cls).__new__(cls, *args)
        return cls.__instance

# both the objects are still initialized twice (addressed in next script decorator.py)
# but the reference for both objects is still the same -> (s1 == s)
s = singleton()
s1 = singleton()
print(s1 == s)  # returns True
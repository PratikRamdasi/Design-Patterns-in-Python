from abc import ABC
from enum import Enum, auto

# base class 
class HotDrink(ABC):
    def consume(self):
        pass

# inherited  
class Tea(HotDrink):
    def consume(self):
        print('Tea is good')

class Coffee(HotDrink):
    def consume(self):
        print('Coffee is good')

# Hierarchy of factories
class HotDrinkFactory(ABC):
    def prepare(self, amount):
        pass

# all methods should create objects    
class TeaFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f'making the tea {amount}')
        return Tea()

class CoffeeFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f'making the coffee {amount}')
        return Coffee()


def make_drink(type):
    if type == 'tea':
        return TeaFactory().prepare(10)
    elif type == 'coffee':
        return CoffeeFactory().prepare(20)
    else:
        return None


# binds all factories together
class HotDrinkMachine:
    class AvailableDrink(Enum): # breaks OCP to add new beverage
        coffee = auto()
        tea = auto()

    factories = []
    initialized = False

    def __init__(self):
        if not self.initialized:
            self.initialized = True
            # init all factories
            for d in self.AvailableDrink:
                name = d.name[0].upper() + d.name[1:] # first letter is uppercase Tea, Coffee
                f_name = name + 'Factory' # CoffeeFactory
                f_instance = eval(f_name)() # no args to factory inits
                self.factories.append((name, f_instance))
    
    def make_drink(self):
        # print avail drinks
        print('Avail drinks:')
        for f in self.factories:
            print(f[0])
        
        s = input(f'Please pick drink (0-{len(self.factories)-1}):')
        idx = int(s)
        a = input('Specify amount:')
        amount = int(a)

        # grab the factory instance with idx
        return self.factories[idx][1].prepare(amount)


if __name__ == "__main__":
    hdm = HotDrinkMachine()
    d = hdm.make_drink()
    d.consume()
    
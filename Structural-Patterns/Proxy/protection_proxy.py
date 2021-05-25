class Car:
    def __init__(self, driver):
        self.driver = driver
        self.age = 
    
    def drive(self):
        if self.age < 16:
        else:
            
        print(f'Car is being driven by {self.driver.name}')


# PROXY
class CarProxy:
    def __init__(self, driver):
        self.driver = driver
        self._car = Car(driver) # defined a proxy car as a private object

    def drive(self):
        if self.driver.age >= 16:
            self._car.drive()
        else:
            print('Driver too young!')


class Driver:
    def __init__(self, name, age):
        self.name = name
        self.age = age

if __name__ == "__main__":
    d = Driver('John', 27)
    c = Car(d)
    c.drive()

    # Control the age parameter -> driving under certain age is not allowed
    # Solution 1: in the `drive` method, add a condition to check the age 
        # -> Violates the OCP
    
    # Without changing the functionality of the Car class, 
    # ADD a proxy for `drive` with the same interface
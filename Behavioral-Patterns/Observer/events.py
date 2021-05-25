# Event -> notification for that event
# Doctors want to know when person is ill

class Event(list):
    # list of functions to invoke when the event happens
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)

# Anyone can subscribe to event class
# For ex. doctor will subscribe to know when person is ill

class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.falls_ill = Event()

    def catch_a_cold(self):
        # raise notification
        self.falls_ill(self.name, self.address)

def call_doctor(name, address):
    # wants to be notified
    print(f'{name} needs a doctor at {address}')

if __name__ == "__main__":
    person = Person('Pratik', '221B Baker St')
    # can also invoke lambda with additional details
    person.falls_ill.append(
        lambda name, address: print(f'{name} is ill')
    ) # need to provide all args to lambda (name & address)
    person.falls_ill.append(call_doctor)
    '''
    Pratik is ill
    Pratik needs a doctor at 221B Baker St
    '''
    
    person.catch_a_cold() # fires the event, call very subscriber
    
    # remove subscription -> person doesn't need a doctor
    person.falls_ill.remove(call_doctor)
    person.catch_a_cold() 
    '''
    Pratik is ill
    '''


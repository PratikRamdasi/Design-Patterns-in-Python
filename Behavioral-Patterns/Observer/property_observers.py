# tells when property is changed

class Event(list):
    # list of functions to invoke when the event happens
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)

# generates the events when property is changed
class PropertyObservable:
    def __init__(self):
        self.property_changed = Event()


# lets change the age property of a person
# person is associated with the property observable
class Person(PropertyObservable):
    def __init__(self, age=0):
        super().__init__()
        self._age = age 

    @property
    def age(self):
        return self._age

    @age.setter
    # check if the property is changed
    # if value is diff, send notification
    def age(self, value):
        if self._age == value:
            # value is not changed
            return
        self._age = value  # assign new value
        self.property_changed('age', value)

# how do we monitor (subscribe to) the events ? 
class DMV:
    def __init__(self, person):
        self.person = person
        # subscribe to the property changed event
        person.property_changed.append(
            self.person_changed
        )
    
    def person_changed(self, name, value):
        # check if it was 'age' that modified
        if name == 'age':
            if value < 16:
                print('Sorry you still cannot drive!')
            else:
                print('Okay, you can drive!')
                # unsubscribe to event -> remove from event list
                self.person.property_changed.remove(self.person_changed)
    
if __name__ == "__main__":
    p = Person()
    ta = DMV(p)

    for age in range(14, 20):
        print(f'Setting age to {age}')
        p.age = age

    '''
    Setting age to 14
    Sorry you still cannot drive!
    Setting age to 15
    Sorry you still cannot drive!
    Setting age to 16
    Okay, you can drive!
    Setting age to 17
    Setting age to 18
    Setting age to 19
    '''


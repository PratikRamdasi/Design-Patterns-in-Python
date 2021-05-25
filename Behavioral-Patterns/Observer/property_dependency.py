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

    # DEPENDENT PROPERTY -
    @property
    def can_vote(self):
        return self._age >= 18
    
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

        # cache old value
        old_can_vote = self.can_vote
        
        self._age = value  # assign new value
        self.property_changed('age', value)

        # after age is changed, compare the new can_vote value
        if old_can_vote != self.can_vote:
            self.property_changed('can_vote', self.can_vote)

        # NOTE : WE CAN't CALL LIKE THIS
        # between age 15-16, can_vote is not changed even though age is changed
        ## self.property_changed('can_vote', value)

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

    def person_changed(name, value):
        if name == 'can_vote':
            # voting status changed
            print(f'Voting ability changed to {value}')

    p = Person()
    p.property_changed.append(
        person_changed
    )

    for age in range(16, 21):
        print(f'Changing age to {age}')
        p.age = age

    '''
    No can_vote is called -> 
    Changing age to 16
    Changing age to 17
    Changing age to 18 
    Changing age to 19
    Changing age to 20
    '''

    # After CACHING
    '''
    Changing age to 16
    Changing age to 17
    Changing age to 18
    Voting ability changed to True
    Changing age to 19
    Changing age to 20
    '''
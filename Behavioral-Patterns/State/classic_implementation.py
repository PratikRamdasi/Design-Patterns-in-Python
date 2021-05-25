from abc import ABC

# single attr -> on/off
class Switch:
    def __init__(self):
        self.state = offState() # its currently OFF

    # calls -> offState().on()
    def on(self):
        self.state.on(self) # current state -> transition to ON state

    # calls -> onState().off()
    def off(self):
        self.state.off(self)

# state machine -> base class
# Switching to OFF when light is OFF
class State(ABC):
    def on(self, switch):
        print('Light is already on!')

    def off(self, switch):
        print('Light is already off!')

# simpler way -> enum for on/off state
class onState(State):
    def __init__(self):
        print('Light is turned on')
    
    def off(self, switch):
        print('Turning the light off...')
        switch.state = offState()
    
    # for on() -> base class is called

class offState(State):
    def __init__(self):
        print('Light is turned off')
    
    def on(self, switch):
        print('Turning the light on...')
        switch.state = onState()

    # for off() -> base class is called

if __name__ == "__main__":
    sw = Switch()

    sw.on()

    sw.off()

    sw.off()

    '''
    Light is turned off
    Turning the light on...
    Light is turned on
    Turning the light off...
    Light is turned off
    Light is already off!
    '''


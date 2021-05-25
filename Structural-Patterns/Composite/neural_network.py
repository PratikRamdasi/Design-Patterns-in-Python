from abc import ABC
from collections.abc import Iterable

## Improve 3 : add connect_to in base class
class Connectable(Iterable, ABC):

    def connect_to(self, other):
        for s in self:
            for o in other:
                s.outputs.append(o)
                o.inputs.append(s)

class Neuron(Connectable):
    def __init__(self, name):
        self.name = name
        self.inputs = []
        self.outputs = []

    def __str__(self):
        return f'{self.name} ' \
            f'{len(self.inputs)} inputs, ' \
            f'{len(self.inputs)} outputs'

    # Solution 2
    # NOTE : Turn scalar into collection of 1 element
    def __iter__(self):
        yield self
    
    # connect other neuron -> two-way
    #def connect_to(self, other):
    #    self.outputs.append(other)
    #    other.inputs.append(self)

class NeuronLayer(list, Connectable):
    def __init__(self, name, count):
        super().__init__()
        self.name = name
        for x in range(0, count):
            self.append(Neuron(f'{name}-{x}'))
        
    def __str__(self):
        return f'{self.name} with {len(self)} neurons'

## Problem -> connect Neuron and NeuronLayer

## solution 1 : Connect every neuron with every other neuron
#def connect_to(self, other):
#    for s in self:
#        # print('yes')
#        for o in other:
#            s.outputs.append(o)
#            o.inputs.append(s)
## Problem : neuron1.connect_to(neuron2) won't work because
# neuron is not iterable, its a scalar object 

## Solution 2 : Turn scalar value into iterable using __iter__


if __name__ == "__main__":
    neuron1 = Neuron('n1')
    neuron2 = Neuron('n2')
    layer1 = NeuronLayer('L1', 3)
    layer2 = NeuronLayer('L2', 4)

    # Solution 1 : improvement 3
    # Neuron.connect_to = connect_to
    # NeuronLayer.connect_to = connect_to

    neuron1.connect_to(neuron2)
    # TODO:
    neuron1.connect_to(layer1)
    layer1.connect_to(neuron2)
    layer1.connect_to(layer2)
    
    print(neuron1)
    print(neuron2)
    print(layer1)
    print(layer2)




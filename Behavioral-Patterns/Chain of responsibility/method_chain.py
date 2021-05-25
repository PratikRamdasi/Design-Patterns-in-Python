# multplayer game -> modify different creatures and their abilities
# creature increased in power after picking up sword ...

class Creature:
    def __init__(self, name, attack, defense):
        self.name = name
        self.attack = attack
        self.defense = defense

    def __str__(self):
        return f'{self.name} ({self.attack}/{self.defense})'


# creature modifier -> class that applies modifications to the creature
    # -> can have multiple modifiers
    # -> pick up magic sword to increase value, then eats a mushroom 
    #    that decreases value
    # ... one after other modifiers ...
class CreatureModifier:
    def __init__(self, creature):
        self.creature = creature
        self.next_modifier = None # Building a chain of modifiers

    # adds new modifier to the chain if not already present
    def add_modifier(self, modifier):
        # if already present, add to the pos after that
        if self.next_modifier:
            self.next_modifier.add_modifier(modifier)
        else:
            self.next_modifier = modifier

    # Position/activity at which the creature needs to be modified
    # does nothing as it is 
    # NOTE : But this propagates chain of respobility
    # NOTE : adds value after this is inherited
    def handle(self):
        if self.next_modifier:
            self.next_modifier.handle()

class DoubleAttackModifier(CreatureModifier):
    def handle(self):
        print(f'Doubling {self.creature.name}''s attack')
        # update the attack
        self.creature.attack *= 2

        # call base class's `handle` to propagate the chain
        # it gets other modifiers
        super().handle()

class IncreaseDefenseModifier(CreatureModifier):
    def handle(self):
        if self.creature.attack <= 2:
            print(f'Increasing {self.creature.name} denfense')
            self.creature.defense += 1
        super().handle()

# This is to terminate the chain, no other modifier will get applied
class noBonusesModifier(CreatureModifier):
    # NOTE : DON'T call super handle
    def handle(self):
        print('No bonuses for you!!')

if __name__ == "__main__":
    goblin = Creature('Goblin', 1, 1)
    print(goblin)

    # start adding modifiers
    root = CreatureModifier(goblin) # base class

    root.add_modifier(noBonusesModifier(goblin)) # not applying any modifier
    '''
    Goblin (1/1)
    No bonuses for you!!
    Goblin (1/1)
    '''

    root.add_modifier(DoubleAttackModifier(goblin))
    root.add_modifier(IncreaseDefenseModifier(goblin))
    root.add_modifier(DoubleAttackModifier(goblin)) # apply multiple times
    
    root.handle() # applies modifiers
    print(goblin)

    '''
    Goblin (1/1)
           (2/1)
           (2/2)
    Doubling Goblins attack
    Increasing Goblin denfense
    Doubling Goblins attack
    Goblin (4/2)
    '''

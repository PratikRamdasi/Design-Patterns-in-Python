# Attributes apply before calling Handle
# modifiers need to be used as soon as modifier enters the game
from enum import Enum
from abc import ABC

# Event broker (Observer design pattern)
# Command Query Separation 

# list of functions you can call
class Event(list):
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)

# defines what to query
class WhatToQuery(Enum):
    ATTACK = 1
    DEFENSE = 2

# define query for each creature 
class Query:
    def __init__(self, creature_name, what_to_query, default_value):
        # modifiers will modify default_value 
        self.value = default_value
        self.creature_name = creature_name
        self.what_to_query = what_to_query


# Event broker -> game -> takes care of chain of responsibility 
class Game:
    def __init__(self):
        # list of queries, attack, defense, attack etc...
        self.queries = Event()
    
    # sender is a modifier and query is attack/defense
    def perform_query(self, sender, query):
        self.queries(sender, query)

# modifiers class
class CreatureModifier(ABC):
    def __init__(self, game, creature):
        self.game = game
        self.creature = creature
        self.game.queries.append(self.handle)

    # this will be modified in the inherited classes
    def handle(self, sender, query):
        pass

    # terminate the modifiers
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        # remove yourself from handlers
        self.game.queries.remove(self.handle)


# using Event Broker 
class DoubleAttackModifier(CreatureModifier):
    def handle(self, sender, query):
        # verify that sender is actually current creature and query is attack
        if sender.name == self.creature.name and query.what_to_query == WhatToQuery.ATTACK:
            print(f'Doubling {self.creature.name}''s attack')
            query.value *= 2


class Creature:
    # initial values for attack and defense
    def __init__(self, game, name, attack, defense):
        self.name = name
        self.initial_attack = attack
        self.initial_defense = defense
        self.game = game

    @property
    def attack(self):
        q = Query(self.name, WhatToQuery.ATTACK, self.initial_attack)
        self.game.perform_query(self, q) # perform the event
        return q.value

    @property
    def defense(self):
        q = Query(self.name, WhatToQuery.DEFENSE, self.initial_defense)
        self.game.perform_query(self, q) # perform the event
        return q.value

    def __str__(self):
        return f'{self.name} ({self.attack}/{self.defense})' # use propert values


if __name__ == "__main__":
    game  = Game()
    goblin = Creature(game, 'Pratik', 2, 2)
    print(goblin)

    # dam = DoubleAttackModifier(game, goblin)
    # print(goblin)
    '''
    Pratik (2/2)
    Doubling Pratiks attack
    Pratik (4/2)
    '''
    ## Uuse with to terminate the modifiers -
    with DoubleAttackModifier(game, goblin):
        print(goblin)
        # exit the scope

    print(goblin)


    
        
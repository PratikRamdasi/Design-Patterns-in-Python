from abc import ABC
from enum import Enum

class Creature(ABC):
    def __init__(self, game, attack, defense):
        self.game = game
        self.initial_attack = attack
        self.initial_defense = defense

    @property
    def attack(self): pass

    @property
    def defense(self): pass

    def query(self, source, query): pass

class WhatToQuery(Enum):
    ATTACK = 1
    DEFENSE = 1

class Query:
    def __init__(self, what_to_query, default_value):
        # modifiers will modify default_value 
        self.value = default_value
        self.what_to_query = what_to_query
    

class Goblin(Creature):
    def __init__(self, game, attack=1, defense=1):
        super().__init__(game, attack, defense)

    @property
    def attack(self):
        q = Query(WhatToQuery.ATTACK, self.initial_attack)
        for c in self.game.creatures:
            c.query(self, q)
        return q.value
        
    @property
    def defense(self):
        q = Query(WhatToQuery.DEFENSE, self.defense)
        for c in self.game.creatures:
            c.query(self, q)
        return q.value

    def query(self, source, query):
        if self != source and WhatToQuery.DEFENSE == query.what_to_query:
            query.value += 1


class GoblinKing(Goblin):
    def __init__(self, game):
        super().__init__(game, 3, 3)
    
    def query(self, source, query):
        if self != source and WhatToQuery.ATTACK == query.what_to_query:
            query.value += 1


class Game:
    def __init__(self):
        self.creatures = []

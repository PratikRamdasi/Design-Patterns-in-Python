# building a game -> keep stats of creature
# expose properties to iterator
'''
class Creature:
    def __init__(self):
        self.strength = 10
        self.agility = 10
        self.intelligence = 10

    # aggregate stats 
    #   -> unstable, need to make sure not to miss any property
    @property
    def sum_of_stats(self):
        return self.strength + self.intelligence + self.agility

    @property
    def max_stat(self):
        return max(self.strength, self.intelligence, self.agility)

    @property
    def average_stat(self):
        return self.sum_of_stats / 3.0 # manual number -> unstable
'''

# better refactor
# ==> instead of separate properties, define them in list of stats
# LIST BACKED PROPERTIES
# iterating on attributes
class Creature:
    _strength = 0
    _agility = 1
    _intelligence = 2 

    def __init__(self):
        self.stats = [10, 10, 10]

    # expose the stats
    @property
    def strength(self):
        return self.stats[Creature._strength]
    
    @strength.setter
    def strength(self, value):
        self.stats[Creature._strength] = value

    @property
    def agility(self):
        return self.stats[Creature._agility]
    
    @agility.setter
    def agility(self, value):
        self.stats[Creature._agility] = value

    @property
    def intelligence(self):
        return self.stats[Creature._intelligence]
    
    @intelligence.setter
    def intelligence(self, value):
        self.stats[Creature._intelligence] = value

    @property
    def sum_of_stats(self):
        return sum(self.stats)

    @property
    def max_stat(self):
        return max(self.stats)

    @property
    def average_stat(self):
        return float(sum(self.stats) / len(self.stats)) # manual number -> unstable
    


    


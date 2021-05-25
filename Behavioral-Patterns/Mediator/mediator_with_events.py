# Event is a list of functions to be called
class Event(list):
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)

# soccer game
# game as a mediator -> generated events 
# players and other people gain info about the game from these events
class Game:
    def __init__(self):
        # anyone can subscribe to events
        self.events = Event()

    def fire(self, args):
        self.events(args)

class GoalScoredInfo:
    def __init__(self, who_scored, goals_scored):
        self.who_scored = who_scored
        self.goals_scored = goals_scored

class Player:
    def __init__(self, name, game):
        self.name = name
        self.game = game
        self.goals_scored = 0

    def score(self):
        self.goals_scored += 1
        args = GoalScoredInfo(self.name, self.goals_scored)
        # mediator fires the event that player is subscribed
        # and broadcasted this event to others 
        self.game.fire(args)

class Coach:
    def __init__(self, game):
        game.events.append(self.celebrate_goal)

    def celebrate_goal(self, args):
        # goalsscoredinfo -> args (here)
        if isinstance(args, GoalScoredInfo) and args.goals_scored < 3:
            print(f'Coach says: well done, {args.who_scored}!')

if __name__ == "__main__":
    game = Game()
    player = Player('Sam', game)
    coach = Coach(game)

    player.score()
    player.score()
    player.score()
    '''
    Coach says: well done, Sam!
    Coach says: well done, Sam!
    '''


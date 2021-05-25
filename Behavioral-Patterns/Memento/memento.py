class Memento:
    def __init__(self, balance):
        self.balance = balance

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
        ## SAVE all states
        self.changes = [Memento(self.balance)]
        ## NEED to know index of current state for undo/redo
        self.current = 0
    
    def deposit(self, amount):
        self.balance += amount
        m = Memento(self.balance)
        self.changes.append(m)
        self.current += 1
        return m

    # roll back to preserved system
    def restore(self, memento):
        if memento: # memento can be None
            self.balance = memento.balance
            self.changes.append(memento)
            self.current = len(self.changes) - 1 
                # points to last element in list

    def undo(self):
        # can undo only when current position is not zero
        if self.current > 0:
            self.current -= 1 # go back 
            m = self.changes[self.current]
            self.balance = m.balance
            return m
        return None

    def redo(self):
        # can redo only when current position is last
        if self.current + 1 < len(self.changes):
            self.current += 1 # go back 
            m = self.changes[self.current]
            self.balance = m.balance
            return m
        return None
        

    def __str__(self):
        return f'Balance = {self.balance}'

if __name__ == "__main__":
    '''
    # no memento for init balance - since its object initializer
    ba = BankAccount(100)
    m1 = ba.deposit(50) # memento1
    m2 = ba.deposit(25) # memento2
    print(ba) # Balance = 175

    # restore the state
    ba.restore(m1)
    print(ba) # Balance = 150

    ba.restore(m2)
    print(ba) # Balance = 175
    '''
    ## UNDO and REDO
    ba = BankAccount(100)
    ba.deposit(50)
    ba.deposit(25)
    print(ba) # Balance = 175

    ba.undo()
    print(f'Undo 1: {ba}')
    ba.undo()
    print(f'Undo 2: {ba}')

    ba.redo()
    print(f'Redo 1: {ba}')
    ba.redo()
    print(f'Redo 2: {ba}')



from abc import ABC
from enum import Enum

# Bank needs to keep record of every transaction 
#   -> i.e. keep record of every withdraw and deposit
#   -> Provide INTERFACE for calling commands for that
#        -> commands will be invoked, recorded and undone as well

class BankAccount:
    OVERDRAFT_LIMIT = -500

    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f'Deposited {amount}, balance = {self.balance}')
        
    def withdraw(self, amount):
        if self.balance - amount >= self.OVERDRAFT_LIMIT:
            self.balance -= amount
            print(f'Withdrew {amount}, balance = {self.balance}')
            return True
        return False

    def __str__(self):
        return f'Balance = {self.balance}'

# command interface
class Command(ABC):
    def invoke(self):
        pass

    def undo(self):
        pass

# command interface for bank account
class BankAccountCommand(Command):
    
    class Action(Enum):
        DEPOSIT = 0
        WITHDRAW = 1

    # account -> what account to operate on
    # action -> what action to take
    # amount -> to be withdrawn, deposited
    def __init__(self, account, action, amount):
        self.account = account
        self.action = action
        self.amount = amount
        # track every operation is its successful
        self.success = None

    def invoke(self):
        if self.action == self.Action.DEPOSIT:
            self.account.deposit(self.amount)
            self.success = True
        elif self.action == self.Action.WITHDRAW:
            self.success = self.account.withdraw(self.amount)

    # undo deposit -> withdraw
    def undo(self):
        # make sure that prev operation was successful
        if not self.success:
            return
            
        if self.action == self.Action.DEPOSIT:
            self.account.withdraw(self.amount)
        elif self.action == self.Action.WITHDRAW:
            self.account.deposit(self.amount)


if __name__ == "__main__":
    ba = BankAccount() # $0 by default
    cmd = BankAccountCommand(
        ba, BankAccountCommand.Action.DEPOSIT, 100
    )
    cmd.invoke()
    print(f'After $100 deposit: {ba}') 
    '''
    Deposited 100, balance = 100
    After $100 deposit: Balance = 100
    '''

    ## side effect -> UNDO method -> rolls back changes done
    cmd.undo()
    print(f'After $100 deposit undone: {ba}')
    '''
    Deposited 100, balance = 100
    After $100 deposit: Balance = 100
    Withdrew 100, balance = 0
    After $100 deposit undone: Balance = 0
    '''

    ## Working with illegal command -> withdraw large amount
    illegal_cmd = BankAccountCommand(
        ba, BankAccountCommand.Action.WITHDRAW, 1000
    )
    illegal_cmd.invoke()
    print(f'After impossible withdrawal: {ba}')

    # NOTE Problem -> here UNDO will add $1000 deposit which is wrong since the
    # previous command of withdrawal is failed - balance was 0 and 1000
    # could not be withdrawn

    # NOTE Solution -> Need to track every operation is it was successful
    illegal_cmd.undo()
    print(f'After undo: {ba}')


    
    
from abc import ABC
from enum import Enum
import unittest

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
    def __init__(self):
        # track every operation is its successful
        self.success = False

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
        super().__init__() # improved for self.success in base class
        self.account = account
        self.action = action
        self.amount = amount

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

# apply list of commands
# works for single and list of commands
# compsite command interface
class CompositeBankAccountCommand(Command, list):
    def __init__(self, items):
        # append all items as list of commands
        super().__init__()
        for i in items:
            self.append(i)

    def invoke(self):
        # invoke every command
        for x in self:
            x.invoke()

    def undo(self):
        # undo each of the consistent command
        # in reverse order -> last uncorrect commands needs to undone first
        for x in reversed(self):
            x.undo()

# Improved composite command
class MoneyTransferCommand(CompositeBankAccountCommand):
    def __init__(self, from_acct, to_acct, amount):
        super().__init__([
            # list of ba commands -> deposit and withdraw
            # transfer from one account to another 
            BankAccountCommand(from_acct, BankAccountCommand.Action.WITHDRAW, amount),
            BankAccountCommand(to_acct, BankAccountCommand.Action.DEPOSIT, amount),
        ])

    def invoke(self):
        # check if prev operation was successful
        ok = True # default
        for cmd in self:
            if ok:
                cmd.invoke()
                ok = cmd.success
            else:
                cmd.success = False
        self.success = ok # set the success value

# Unit tests
class TestSuite(unittest.TestCase):
    '''
    def test_composite_deposit(self):
        ba = BankAccount() # $0 by default
        # define commands
        deposit1 = BankAccountCommand(
            ba, BankAccountCommand.Action.DEPOSIT, 100
        )
        deposit2 = BankAccountCommand(
            ba, BankAccountCommand.Action.DEPOSIT, 50
        )
        # composite command
        composite = CompositeBankAccountCommand(
            [deposit1, deposit2]
        )
        composite.invoke()
        print(ba)

        composite.undo()
        print(ba)

    def test_transfer_fail(self):
        # test to transfer money from one account to another
        ba1 = BankAccount(100)
        ba2 = BankAccount()

        # amount to be transferred from ba1 to ba2
        ## NOTE :Fails if the amount is >100
        ##    -> Since self.success is asscociated with a single command
        ##    -> we need to modify it to be associated with 2 bank accounts (commands)
        ## NOTE (solution): add self.success in base class Command instead, check above
        amount = 100

        # create transfer composite command
        wc = BankAccountCommand(
            ba1, BankAccountCommand.Action.WITHDRAW, amount
        )
        dc = BankAccountCommand(
            ba2, BankAccountCommand.Action.DEPOSIT, amount
        )
        transfer = CompositeBankAccountCommand([wc, dc])
        transfer.invoke()
        print(f'ba1: {ba1}, ba2: {ba2}')
        transfer.undo()
        print(f'ba1: {ba1}, ba2: {ba2}')
    '''
    def test_better_transfer(self):
        ba1 = BankAccount(100)
        ba2 = BankAccount()

        amount = 100
        transfer = MoneyTransferCommand(ba1, ba2, amount)
        transfer.invoke()
        print(f'ba1: {ba1}, ba2: {ba2}')

        transfer.undo()
        print(f'ba1: {ba1}, ba2: {ba2}')
        print(transfer.success)
        '''
        Withdrew 100, balance = 0
        Deposited 100, balance = 100
        ba1: Balance = 0, ba2: Balance = 100
        Withdrew 100, balance = 0
        Deposited 100, balance = 100
        ba1: Balance = 100, ba2: Balance = 0
        True
        '''
        '''
        For amount -> 1000
        ba1: Balance = 100, ba2: Balance = 0
        ba1: Balance = 100, ba2: Balance = 0
        False
        '''

    
if __name__ == "__main__":
    unittest.main()




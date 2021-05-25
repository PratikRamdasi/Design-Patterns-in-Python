import string
import random

class User:
    def __init__(self, name):
        self.name = name

# NOTE: FLYWEIGHT CLASS
class User2:
    # static list of common first and last names
    strings = []

    # NOTE : name is combined - first + last
    # split it and store first and last names' indices
    def __init__(self, full_name):

        # get_or_add checks if string is present and returns its index
        # otherwise adds the string to store
        def get_or_add(s):
            if s in self.strings:
                return self.strings.index(s)
            else:
                self.strings.append(s)
                return len(self.strings) - 1
                
        self.names = [get_or_add(x) for x in full_name.split(' ')] 
        # stores the indexes for each first and last name

    # print the full name using self.strings
    def __str__(self):
        return ' '.join([self.strings[x] for x in self.names])


#  makes a random name for user with 8 characters
def make_random_string():
    chars = string.ascii_lowercase
    return ''.join(
        [random.choice(chars) for x in range(8)]
    )

if __name__ == "__main__":
    users = []
    # make random 100 first and last names
    first_names = [make_random_string() for x in range(100)]
    last_names = [make_random_string() for x in range(100)]
    
    # cartesian product
    # make 10,000 users
    for first in first_names:
        for last in last_names:
            # users.append(User(f'{first} {last}'))
            users.append(User2(f'{first} {last}'))   # memory saving 

    # Typically, we will need to store 10,000 strings 
    # NOTE: but we can use references for first and last names instead, so total
    # we need to store only 100 + 100 = 200 references => Build a Flyeight 
    print(users[0])

# people join / leave chat room
# not necessarily being aware of each other -> unless there is a direct
# communication

class Person:
    def __init__(self, name):
        self.name = name
        # save the chatting log of that person
        self.chat_log = []
        # room this person is assigned to
        self.room = None

    def receive(self, sender, message):
        s = f'{sender}: {message}'
        print(f'[{self.name}\'s chat session] {s}')
        self.chat_log.append(s)

    def say(self, message):
        # broadcast msg to the room
        self.room.broadcast(self.name, message)

    def private_message(self, who, message):
        self.room.message(self.name, who, message)

# Mediator
class ChatRoom:
    def __init__(self):
        # specify people in room
        self.people = []

    def join(self, person):
        join_msg = f'{person.name} joints the chat'
        # broadcast to other members that this person has joined
        self.broadcast('room', join_msg)
        # set room ref for person
        person.room = self
        self.people.append(person)

    def broadcast(self, source, message):
        # broadcast to people besides self
        for p in self.people:
            if p.name != source:
                p.receive(source, message)

    # msg a particular participant
    def message(self, source, dest, message):
        for p in self.people:
            if p.name == dest:
                p.receive(source, message) 

    ## Leave chat room


if __name__ == "__main__":
    room = ChatRoom()

    john = Person('John')
    jane = Person('Jane')

    room.join(john)
    room.join(jane)

    john.say('hi room!')
    jane.say('Oh, hey john')

    simon = Person('Simon')
    room.join(simon)
    simon.say('hi everyone!')

    # private messages
    jane.private_message('Simon', 'glad you could join us!!')

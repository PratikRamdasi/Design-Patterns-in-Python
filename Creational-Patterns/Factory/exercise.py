
class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f'id:{self.id}, name:{self.name}'

#class newFactory:
#    def create_person(self, id, name):
#        return Person(id, name)

class PersonFactory:
    id = 0

    def create_person(self, name):
        p = Person(PersonFactory.id, name)
        PersonFactory.id += 1
        return p

if __name__ == "__main__":
    p = PersonFactory().create_person('pratik')
    p1 = PersonFactory().create_person('pratik2')
    print(p)
    print(p1)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Person: {self.name}, Age: {self.age}'

class House:
    def __init__(self, address, num_rooms):
        self.address = address
        self.num_rooms = num_rooms
        self.people = []

    def add_person(self, person):
        self.people.append(person)

    def remove_person(self, person):
        self.people.remove(person)

    def display_people(self):
        for person in self.people:
            print(person)


p1 = Person('John Wick', 30)
p2 = Person('Fahad Saleem', 28)

h1 = House('123 Main St', 3)

h1.add_person(p1)
h1.add_person(p2)

h1.display_people()

h1.remove_person(p2)

h1.display_people()

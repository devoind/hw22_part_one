from part_1.practice.abstract_classes.solution import *

boat = Boat()
car = Car()
kamikaze = Electroscooter()

if __name__ == '__main__':
    person = Person()
    person.use_transport(boat)
    print('=' * 45)
    person.use_transport(car)
    print('=' * 45)
    person.use_transport(kamikaze)

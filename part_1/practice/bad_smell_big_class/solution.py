class Warrior:
    def attack(self):
        print("Я атакую")

    def defense(self):
        print("Я обороняюсь")

    def move(self):
        print("Я иду вперед")


class Healer:
    def defense(self):
        print("Я в домике")

    def move(self):
        print("Я иду")

    def heal(self):
        print("Сейчас подлечу")


class Tree:
    def defense(self):
        print("Я в защите")

    def on_fire(self):
        print("Я горю")


class Trap:
    def attack(self):
        print("It's a trap!")

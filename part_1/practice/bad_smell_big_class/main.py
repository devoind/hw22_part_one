from part_1.practice.bad_smell_big_class.solution import Warrior, Healer, Tree, Trap

unit = Warrior()
healer = Healer()
tree = Tree()
trap = Trap()

if __name__ == '__main__':
    unit.attack()
    print('=' * 45)
    healer.heal()
    print('=' * 45)
    tree.defense()
    print('=' * 45)
    trap.attack()

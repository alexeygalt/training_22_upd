from abc import ABC, abstractmethod


class Unit(ABC):
    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def defense(self):
        pass

    @abstractmethod
    def move(self):
        pass


class Warrior(Unit):
    ...


class Healer(Unit):
    def heal(self):
        pass


class Tree(Unit):

    def on_fire(self):
        pass


class Trap(Unit):
    ...


if __name__ == '__main__':
    unit = Warrior()
    healer = Healer()
    trap = Trap()

from random import randint


class Soldier:
    def __init__(self, name: str, health: int = 100):
        self.name: str = name
        self.health: int = health

    def make_kick(self, enemy: 'Soldier'):
        enemy.health -= 20
        if enemy.health <= 0:
            enemy.health = 0
        self.health += 10
        print(f'{self.name} hits {enemy.name}')
        print(f'{enemy.name} = {enemy.health}')

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, other_name):
        self.name = other_name
    

class Battle:
    def __init__(self, sol1: Soldier, sol2: Soldier):
        self.sol1: Soldier = sol1
        self.sol2: Soldier = sol2
        self.result: str = 'There was no battle'

    def battle(self):
        while self.sol1.health >= 0 or self.sol2.health >= 0:
            n = randint(1, 2)
            if n == 1:
                self.sol1.make_kick(self.sol2)
            else:
                self.sol2.make_kick(self.sol1)

        if self.sol1.health > 0:
            self.result = f'{self.sol1.name}: Win'
        if self.sol2.health > 0:
            self.result = f'{self.sol2.name}: Win'

    def get_winner(self):
        print(self.result)
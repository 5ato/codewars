class Person:
    id = 0

    def __init__(self, c):
        self.id = Person.id
        Person.id += 1
        self.command = c


class Hero(Person):
    def __init__(self, c):
        Person.__init__(self, c)
        self.lvl: int = 0

    def level_up(self):
        self.lvl += 1
        

class Soldier(Person):
    def __init__(self, c):
        Person.__init__(self, c)
        self.my_hero: Hero = None

    def follow(self, hero: Hero):
        self.my_hero = hero.id
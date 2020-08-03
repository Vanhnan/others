class Soldier:
    def __init__(self, n, t):
        self.number = n
        self.team = t
    def follow_hero(self, hero):
        print("soldier number "+str(self.number)+" follows hero number "+str(hero.number))

class Hero:
    def __init__(self, n, t):
        self.number = n
        self.team = t
        self.lvl = 1
    def level_up(self):
        self.lvl += 1


        

class Warrior:
    def __init__(self):
        self.health=50
        self.attack=5
        self.type="w"

    def equip_weapon(self,weapon_name):
        self.attack = self.attack + weapon_name.attack
        self.health = self.health + weapon_name.health
        # if self.type == "w" or self.type == "k" or self.type == "r":
        #     self.attack = self.attack + weapon_name.attack
        #     self.health = self.health + weapon_name.health
        if self.type == "d":

            self.defense = self.defense + weapon_name.defense
        if self.type == "v":

            self.vampirism = self.vampirism + weapon_name.vampirism
            if self.type == "h":

                self.heal_power = self.heal_power + weapon_name.heal_power
        if  self.attack < 0 :
            self.attack = 0
        if  self.health<0:
            self.health = 0
        if  self.defense < 0:
            self.defense = 0
        if self.vampirism <0:
            self.vampirism = 0
        if  self.heal_power <0:
            self.heal_power = 0



    def fight(self,enemy):


        while True:
            if self.type=="v":
                print(self.health)

                if enemy.type=="d":
                    if self.attack > enemy.defense:
                        self.health = self.health + (self.attack - enemy.defense)*self.vampirism
                else:
                    self.health = self.health + self.attack*self.vampirism
            print(self.health)
            if enemy.type=="d":
                print("enemy defender")
                if self.attack > enemy.defense :
                    enemy.health = enemy.health + enemy.defense - self.attack
            else:
                print("!!!")
                enemy.health = enemy.health - self.attack
            if self.health <= 0:
                return False
            if enemy.health <=0:
                return True
            if enemy.type=="v":
                print(enemy.health)
                if self.type=="d":
                    if enemy.attack > self.defense:
                        enemy.health = enemy.health + (enemy.attack - self.defense)*enemy.vampirism
                else:
                    enemy.health = enemy.health + enemy.attack*enemy.vampirism
            print(enemy.health)

            if self.type == "d":
                if enemy.attack > self.defense:
                    self.health = self.health + self.defense - enemy.attack
            else:
                self.health = self.health - enemy.attack
    def isAlive(self):
        if self.health > 0:
            return True
        else:
            return False
class Knight(Warrior):


     def __init__(self):
         super().__init__()
         self.attack=7
         self.type = "k"


class Army:
    def __init__(self):
        self.units=[]
    def add_units(self,unit):
        self.units.append(unit)

class Battle:
    def __init__(self):
        print()
    def __init__(self,army1,army2):
        self.army1=army1
        self.army2=army2

    def straight_fight(self):


        minimun=min(len(self.army1.units),len(self.army2.units))
        print("###"+str(len(self.army2.units)))
        while True:
            killed = []
            i = 0
            j = 0
            if len(self.army1.units) == 0:
                return False
            if  len(self.army2.units) == 0:
                return True
            while i < minimun :
                #print(self.army1.units[i].fight(self.army2.units[j]))
                if self.army1.units[i].fight(self.army2.units[j]):
                    killed.append(1)
                    print(True)
                else:
                    killed.append(2)
                    print(False)
                i=i+1
                j=j+1
            n=0
            print(killed)
            print(killed[n] == 1 )
            while n < len(killed):
                if killed[n] == 1:
                    self.army2.units.pop(n)
                    print("first")
                else:
                    self.army1.units.pop(n)
                    print("second")
                n=n+1




    def fight(self):
        health1=0
        health2=0
        health1_list=[]
        health2_list=[]
        for n in range(len(self.army1.units)):
            health1=health1+self.army1.units[n].health
            health1_list.append(self.army1.units[n].health)
        for m in range(len(self.army2.units)):
            health2=health2+self.army2.units[m].health
            health2_list.append(self.army2.units[m].health)

        # for i in range(len(army1.units)):

           # army1.units[i].fight(army2.units[i])
        i=0
        j=0
        counter=0
        while True:
            print(i , j , counter ,health1 , health2)
            if health1 <= 0:

                return  False
            if health2 <=0:
                return True

            if self.army1.units[i].fight(self.army2.units[j]):
                print(self.army1.units[0].health)
                health2=health2-health2_list[j]
                j=j+1

            else:
                print(self.army1.units[i].health)
                health1=health1-health1_list[i]
                i=i+1
            counter=counter+1
class Defender(Warrior):
    def __init__(self):
        super().__init__()
        self.attack=3
        self.health=60
        self.defense = 2
        self.type="d"
class Rookie(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 50
        self.attack = 1
        self.type="r"

class Vampire(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 40
        self.attack = 4
        self.type="v"
        self.vampirism = 0.5
class Healer(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 60
        self.attack = 0
        self.heal_power=2
        self.type="h"
    def healing(self,w):
        w.health = w.health + self.heal_power
        if w.type == "w" or w.type == "k" or type == "r":

            if w.health > 50:
                w.health = 50
        if w.type == "d" or w.type == "h":
            if w.health > 60:
                w.health = 60
        if w.type == "v":
            if w.health > 40:
                w.health = 40

class Weapon:
    def __init__(self,health, attack, defense, vampirism, heal_power):
        self.health=health
        self.attack=attack
        self.defense=defense
        self.vampirism=vampirism
        self.heal_power=heal_power


class Sword(Weapon):
    def __init__(self):
        super().__init__(0,0,0,0,0)
        self.health=5
        self.attack=2
class Shield (Weapon):
    def __init__(self):
        super().__init__(0,0,0,0,0)
        self.health=20
        self.attack=-1
        self.defense=2
class A (Weapon):
    def __init__(self):
        super().__init__(0,0,0,0,0)
        self.health=-15
        self.attack=5
        self.defense=-2
        self.vampirism=0.1
class Katana (Weapon):
    def __init__(self):
        super().__init__(0,0,0,0,0)
        self.health=-20
        self.attack=6
        self.defense=-5
        self.vampirism=0.5
class MagicWand  (Weapon):
    def __init__(self):
        super().__init__(0,0,0,0,0)
        self.health=30
        self.attack=3
        self.heal_power=3


class Main:
    def main():
        r1=Rookie()
        w1=Warrior()
        w2=Warrior()
        k1=Knight()
        army1=Army()
        army1.add_units(k1)
        army2=Army()
        army2.add_units(w2)
        army2.add_units(w1)
        battle=Battle(army1,army2)
        v1=Vampire()
        h1=Healer()
        h1.healing(w1)
        w1.health=46
        h1.healing(w1)

        weapon=Weapon(1,1,1,1,1)
        a=A()

        print(a.heal_power)
        #print(w1.fight(w2))

       #print( battle.fight())
        d1=Defender()
        #print(d1.health,d1.attack,d1.defense,d1.type,v1.fight(d1))
       # print(battle.straight_fight())

    if __name__ == '__main__': main()
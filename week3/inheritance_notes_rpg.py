class Monster:

    def __init__(self):
        self.hp = 10


class Weapon:

    def __init__(self):
        self.damage = 0
        self.durability = 0

    def attack(self):
        self.set_durability()
        return self.damage

    def set_durability(self):
        self.durability -= 1
        if self.durability < 0:
            self.durability = 0
            self.damage = 0


# class Warrior:

#     __
#     self.weapon = Sword()


class Sword(Weapon):

    def __init__(self):
        self.damage = 3
        self.durability = 2


class UnbreakableSword (Sword):

    def set_durabiliity(self):
        pass

orc = Monster()
bad_sword = Weapon()

ok_sword = Sword()

awesome_sword = UnbreakableSword()

print(orc.hp)
orc.hp -= bad_sword.attack()
print(orc.hp)
orc.hp -= ok_sword.attack()
print(orc.hp)
orc.hp -= UnbreakableSword.attack()
print(orc.hp)
orc.hp -= UnbreakableSword.attack()
print(orc.hp)
orc.hp -= UnbreakableSword.attack()
print(orc.hp)
orc.hp -= UnbreakableSword.attack()
print(orc.hp)

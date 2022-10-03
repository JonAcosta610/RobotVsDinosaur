from weapon import Weapon

class Robot:

    def __init__(self, name):
        self.name = name
        self.health_points = 100
        self.active_weapon = Weapon("Biggoron's Sword")

    def attack_dinosaur(self, dinosaur):
        dinosaur.health_points -= self.attack_weapon.attack_power
        print(f"\n{self.name} attacked {dinosaur.name} with {self.weapon.name} for {self.weapon.attack_power} damage!\n{dinosaur.name}'s HP is now {dinosaur.health_points}")
        if dinosaur.health_points <= 0:
            print(f"\n{dinosaur.name} has been destroyed!\nThe winner is {self.name}!")

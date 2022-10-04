from weapon import Weapon

class Robot:

    def __init__(self, name):
        self.name = name
        self.health_points = 100
        self.active_weapon = Weapon("Biggoron's Sword", 20)

    def attack_dinosaur(self, dinosaur):
        dinosaur.health_points -= self.active_weapon.attack_power
        print(f"\n{self.name} attacked {dinosaur.name} with {self.active_weapon.name} for {self.active_weapon.attack_power} damage!\n{dinosaur.name}'s HP is now {dinosaur.health_points}")

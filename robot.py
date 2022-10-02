from weapon import Weapon

class Robot:

    def __init__(self):
        self.name = "Ro-Bo-Botto"
        self.health_points = 100
        self.active_weapon = Weapon()

    def attack_dinosaur(self, dinosaur):
        pass

    def health(self):
        if self.health >= 0:
            print(f"Ro-Bo_Botto's health is {self.health_points}")
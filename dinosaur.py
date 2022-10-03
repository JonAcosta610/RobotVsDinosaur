
class Dinosaur:

    def __init__(self, name):
        self.name = name
        self.attack_power = 25
        self.health_points = 100

    def attack_robot(self, robot):
        robot.health_points -= self.attack_power
        print(f"\n{self.name} attacked {robot.name} for {self.attack_power} damage!\n{robot.name}'s HP is now {robot.health_points}")
        if robot.health_points <= 0:
            print(f"\n{robot.name} has been destroyed!\nThe winner is {self.name}!")
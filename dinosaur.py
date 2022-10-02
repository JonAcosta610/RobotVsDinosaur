
class Dinosaur:

    def __init__(self):
        self.name = ""
        self.attack_power = 100
        self.health = 100

    def attack_robot(self, robot):
        robot.health_points = robot.health_points - int(self.attack_power)
        print(f"\n{self.name} attacked {robot.name} for {self.attack_power} damage!\n {robot.name}'s HP is now {robot.health_points}")
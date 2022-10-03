from robot import Robot
from dinosaur import Dinosaur

class Battlefield:

    def __init__(self):
        self.robot = Robot("Ro-Bo-Boot")
        self.dinosaur = Dinosaur("Veli-Raptor")

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()
    
    def display_welcome(self):
        print("Welcome to the battle of the century! Robots VS Dinosaurs!")
        print(f"In the red corner, hailing from the Dexter's Labora tory, we have {self.robot.name}!")
        print(f"And in the blue corner, hailing from Jurassic Park, we have {self.dinosaur.name}!")

    def battle_phase(self):
        while self.dinosaur.health_points >= 0 and self.robot.health_points >= 0:
            self.dinosaur.attack_robot(self.robot)
            self.robot.attack_dinosaur(self.dinosaur)

    def display_winner(self):
        if dinosaur.health_points > robot.health_points:
            print(f"\n{self.robot.name} has been destroyed!\nThe winner is {self.dinosaur.name}!")
        else:
            print(f"\n{self.dinosaur.name} has been destroyed!\nThe winner is {self.robot.name}!")

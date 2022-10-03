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
        self.dinosaur.attack_robot(self.robot)
        self.robot.attack_dinosaur(self.dinosaur)

    def display_winner(self):
        pass
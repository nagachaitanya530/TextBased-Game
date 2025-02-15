# player.py
class Player:
    def __init__(self, name, health, score):
        self.name = name
        self.health = health
        self.score = score
        self.inventory = []

    def view_inventory(self):
        print("Your inventory:")
        for item in self.inventory:
            print(item)

    def view_player_data(self):
        print("Your player data:")
        print(f"Name: {self.name}")
        print(f"Health: {self.health}")
        print(f"Score: {self.score}")

def create_player():
    name = input("Enter your name: ")
    health = 100
    score = 0
    return Player(name, health, score)
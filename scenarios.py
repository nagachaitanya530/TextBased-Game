# scenarios.py
import random

def explore_forest(player):
    print("You enter the dark forest...")
    event = random.choice(["find_item", "lose_health", "nothing"])
    if event == "find_item":
        item = random.choice(["sword", "shield", "potion"])
        player.inventory.append(item)
        print(f"You found a {item}!")
    elif event == "lose_health":
        damage = random.randint(10, 20)
        player.health -= damage
        print(f"You encountered a wild beast and lost {damage} health!")
    else:
        print("Nothing happens, but the silence is eerie...")
    player.view_player_data()
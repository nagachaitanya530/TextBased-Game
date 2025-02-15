# game.py
import calculator
import database
import player
import scenarios

def start_game():
    print("Welcome to the adventure game!")
    player_data = player.create_player()
    while True:
        print("\nChoose an action:")
        print("1. Explore the forest")
        print("2. Solve a puzzle using the calculator")
        print("3. View inventory")
        print("4. View player data")
        print("5. View calculation history")
        print("6. Exit game")
        choice = input("Enter your choice: ")

        if choice == "1":
            scenarios.explore_forest(player_data)
        elif choice == "2":
            calculator.calculate()
        elif choice == "3":
            player_data.view_inventory()
        elif choice == "4":
            player_data.view_player_data()
        elif choice == "5":
            database.display_calculation_history()
        elif choice == "6":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    start_game()
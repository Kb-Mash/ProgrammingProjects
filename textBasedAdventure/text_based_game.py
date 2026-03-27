def start_game():
    print("Welcome to the Text-Based Adventure Game!")
    print("You find yourself in a dark forest. You need to find your way out.")
    print("What do you do?")
    print("1. Go north towards the sound of running water")
    print("2. Go east towards the light")
    print("3. Go west towards the mountains")

    choice = input("Enter your choice (1-3): ").strip()

    if choice == "1":
        north_path()
    elif choice == "2":
        east_path()
    elif choice == "3":
        west_path()
    else:
        print("Invalid choice. Please try again.")
        start_game()

def north_path():
    print("\nYou head north and find a river with a bridge.")
    print("As you approach the bridge, you see a troll guarding it.")
    print("What do you do?")
    print("1. Try to cross the bridge quietly")
    print("2. Talk to the troll")
    print("3. Go back to the forest")

    choice = input("Enter your choice (1-3): ").strip()

    if choice == "1":
        print("\nThe troll hears you and blocks your path!")
        print("You try to fight but are defeated. Game Over.")
        play_again()
    elif choice == "2":
        print("\nThe troll is friendly and lets you pass.")
        print("You cross the bridge and find a hidden treasure!")
        print("Congratulations! You win!")
        play_again()
    elif choice == "3":
        start_game()
    else:
        print("Invalid choice.")
        north_path()

def east_path():
    print("\nYou head east and find a small village.")
    print("The villagers welcome you and offer you a place to stay.")
    print("What do you do?")
    print("1. Accept their hospitality")
    print("2. Ask for directions out of the forest")
    print("3. Go back to the forest")

    choice = input("Enter your choice (1-3): ").strip()

    if choice == "1":
        print("\nYou stay the night and learn about the forest.")
        print("In the morning, the villagers guide you to safety.")
        print("You made it out of the forest! You win!")
        play_again()
    elif choice == "2":
        print("\nThe villagers give you directions.")
        print("Following them, you get lost and wander deeper into the forest.")
        print("You never find your way out. Game Over.")
        play_again()
    elif choice == "3":
        start_game()
    else:
        print("Invalid choice.")
        east_path()

def west_path():
    print("\nYou head west and encounter a cave.")
    print("Inside the cave, you find two tunnels.")
    print("What do you do?")
    print("1. Take the left tunnel")
    print("2. Take the right tunnel")
    print("3. Go back to the forest")

    choice = input("Enter your choice (1-3): ").strip()

    if choice == "1":
        print("\nThe left tunnel leads to a dead end with bats.")
        print("The bats attack you! Game Over.")
        play_again()
    elif choice == "2":
        print("\nThe right tunnel leads to the exit of the forest!")
        print("You step out into the sunlight. You win!")
        play_again()
    elif choice == "3":
        start_game()
    else:
        print("Invalid choice.")
        west_path()

def play_again():
    print("\nWould you like to play again?")
    print("1. Yes")
    print("2. No")

    choice = input("Enter your choice (1-2): ").strip()

    if choice == "1":
        start_game()
    elif choice == "2":
        print("Thanks for playing!")
        exit()
    else:
        print("Invalid choice.")
        play_again()

if __name__ == "__main__":
    start_game()
from os import system
from random import randint
from time import sleep


def main() -> None:
    game_over: bool = False
    round_counter: int = 0
    enemy_wins: int = 0
    user_wins: int = 0
    print("*" * 60)
    print("Rock, Paper, Scissors! Face off against a random enemy!")
    print("*" * 60)
    while not game_over:
        round_counter += 1
        enemy_choice = str(randint(1, 3))

        print(f"Round {round_counter}")
        print("Score:")
        print(f"   You: {user_wins}")
        print(f"   Enemy: {enemy_wins}")
        print()
        sleep(0.1)
        print("Choose one below")
        print("   1. Rock")
        print("   2. Paper")
        print("   3. Scissors")
        print()
        sleep(0.2)
        user_choice = input("Enter choice (1/2/3): ")

        while user_choice not in ["1", "2", "3"]:
            print("Invalid input. Input must be 1, 2, or 3.")
            user_choice = input("Enter choice (1/2/3): ")

        if user_choice == "1":  # Rock
            print()
            print("Rock!")
            if enemy_choice == "1":
                print("Enemy also through rock. Tie!")
                sleep(0.2)
                print("Replaying round...")
                round_counter -= 1
            elif enemy_choice == "2":
                print("Enemy threw paper! Round lost.")
                enemy_wins += 1
            elif enemy_choice == "3":
                print("Enemy threw scissors. Round won!")
                user_wins += 1

        elif user_choice == "2":  # Paper
            print()
            print("Paper!")
            if enemy_choice == "1":
                print("Enemy threw rock. Round won!")
                user_wins += 1
            elif enemy_choice == "2":
                print("Enemy also through paper. Tie!")
                round_counter -= 1
            elif enemy_choice == "3":
                print("Enemy threw scissors. Round lost!")
                enemy_wins += 1

        elif user_choice == "3":  # Scissors
            print()
            print("Scissors!")
            if enemy_choice == "1":
                print("Enemy threw rock. Round lost!")
                enemy_wins += 1
            elif enemy_choice == "2":
                print("Enemy threw paper. Round won!")
                user_wins += 1
            elif enemy_choice == "3":
                print("Enemy also through scissors. Tie!")
                round_counter -= 1

        if user_wins >= 3 and user_wins > enemy_wins:
            print("You Win!")
            game_over = True

        elif enemy_wins >= 3 and enemy_wins > user_wins:
            print("Enemy wins!")
            game_over = True
        else:
            sleep(1.2)
            system("clear")


if __name__ == "__main__":
    main()


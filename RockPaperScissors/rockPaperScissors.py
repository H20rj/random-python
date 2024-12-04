from random import randint

loss = False
round_counter, enemy_wins, user_wins = 0, 0, 0
from time import sleep
from os import system



print("*" * 60)
print("Rock, Paper, Scissors! Face off against a random enemy!")
print("*" * 60)
while not False:
    round_counter += 1
    enemy_choice = str(randint(1,3))

    print(f"Round {round_counter}")
    print()
    sleep(0.1)
    print("Choose one below")
    print("   1. Rock")
    print("   2. Paper")
    print("   3. Scissors")
    print()
    sleep(0.2)
    user_choice = input('Enter choice (1/2/3): ')

    while user_choice not in ['1', '2', '3']:
        print("Invalid input. Input must be 1, 2, or 3.")
        user_choice = input('Enter choice (1/2/3): ')

    if user_choice == '1':  # Rock
        print()
        print("Rock!")
        if enemy_choice == '1':
            print("Enemy also through rock. Tie!")
            sleep(0.2)
            print("Replaying round...")
            round_counter -= 1
        elif enemy_choice == '2':
            print('Enemy threw paper! Round lost.')
            enemy_wins += 1
        elif enemy_choice == '3':
            print('Enemy threw scissors. Round won!')
            user_wins += 1

    elif user_choice == '2':   # Paper
        print()
        print('Paper!')
        if enemy_choice == '1':
            print("Enemy threw rock. Round won!")
            user_wins += 1
        elif enemy_choice == '2':
            print("Enemy also through paper. Tie!")
            round_counter -= 1
        elif enemy_choice == '3':
            print('Enemy threw scissors. Round lost!')
            enemy_wins += 1

    elif user_choice == '3':  # Scissors
        print()
        print('Scissors!')
        if enemy_choice == '1':
            print("Enemy threw rock. Round lost!")
            enemy_wins += 1
        elif enemy_choice == '2':
            print('Enemy threw paper. Round won!')
            user_wins += 1
        elif enemy_choice == '3':
            print("Enemy also through scissors. Tie!")
            round_counter -= 1



    if user_wins >= 3 and user_wins > enemy_wins:
        print("You Win!")
        break

    elif enemy_wins >= 3 and enemy_wins > user_wins:
        print("Enemy wins!")
        break
    else:
        sleep(1.2)
        print()
        print("Score")
        print(f"   You: {user_wins}")
        print(f"   Enemy: {enemy_wins}")
        print()
        sleep(1)
        system("clear")



from random import randint

print("......................................")
print("Fighting Game (Fully Randomized Stats)")
print("......................................")

character_name = input("Pick a name for your character: ")
character_name = character_name.capitalize()
print(f"Hello, {character_name}")
print("")

possible_classes = ["Mage", "Hunter", "Tank"]
user_class = input("Please choose a character class (Mage, Hunter, or Tank): ").lower()
user_class = user_class.capitalize()

while not user_class in possible_classes:
    print("Invalid class, maybe there is a rogue capital? Or there ")
    user_class = input("Please choose again (Mage, Hunter, or Tank): ")

if user_class == "Mage" or user_class == "mage":
    health, attack, defense = randint(13, 17), randint(5, 12), 5
elif user_class == "Hunter" or user_class == "hunter":
    health, attack, defense = randint(13, 17) + 1, randint(5, 12) - 1, 8
elif user_class == "Tank" or user_class == "tank":
    health, attack, defense = randint(13, 17) + 2, randint(5, 12) - 2, 10

print("")

enemy_name = input("Now, please choose a name for your opponent: ").lower()
enemy_name = enemy_name.capitalize()

enemy_health = randint(13, 17)
enemy_attack = randint(3, 12)
enemy_defense = 12 - enemy_attack

print("")
print(f"Welcome, {character_name} the {user_class}. Your stats are below: ")
print(f"                                        Health = {health}")
print(f"                                        Attack = {attack}")
print(f"                                        Defense = {defense}")

print("")

print(f"You will be facing the mighty foe, {enemy_name}. Their stats are below:")
print(f"                                        Health = {enemy_health}")
print(f"                                        Attack = {enemy_attack}")
print(f"                                        Defense = {enemy_defense}")

print("")
input("Enter to start fight...")
DEFENSE_CONSTANT: int = 50
damage: float = round(((attack + DEFENSE_CONSTANT) / (enemy_defense + 5)) + 1)
enemy_damage: float = round((enemy_attack + DEFENSE_CONSTANT) / (defense + 5))
counter = 0
wins = 0
enemy_wins = 0
for i in range(2):

    counter = 0


    if i > 0:

        if user_class == "Mage" or user_class == "mage":
            health, attack, defense = randint(13, 17), randint(5, 12), 5
        elif user_class == "Hunter" or user_class == "hunter":
            health, attack, defense = randint(13, 17) + 1, randint(5, 12) - 1, 8
        elif user_class == "Tank" or user_class == "tank":
            health, attack, defense = randint(13, 17) + 2, randint(5, 12) - 2, 10
        enemy_health = randint(13, 17)
        enemy_attack = randint(3, 12)
        enemy_defense = 12 - enemy_attack
        print("")
        print(f"Welcome, {character_name} the {user_class}, to game {i+1}!. Your stats have changed, and they are below: ")
        print(f"                                        Health = {health}")
        print(f"                                        Attack = {attack}")
        print(f"                                        Defense = {defense}")

        print("")

        print(f"You will be facing the same mighty foe, {enemy_name}. Their stats have also changed, nd they are below:")
        print(f"                                        Health = {enemy_health}")
        print(f"                                        Attack = {enemy_attack}")
        print(f"                                        Defense = {enemy_defense}")
        print("")
        input("Enter to start fight...")
    while health > 0 and enemy_health > 0:
        can_take_damage = True
        counter += 1
        print("....................................................")
        print(f"Round {counter}")
        print("What would you like to do?")
        print("    1. Attack")
        print("    2. Defend")
        print("    3. Heal 1HP")
        user_decision = input("Please choose an option (1/2/3): ")

        while user_decision not in ["1", "2", "3", "I want to win"]:
            print("Invalid option. Please choose again.")
            user_decision = input("Please choose an option (1/2/3): ")

        ## USER

        if user_decision == "1":
            enemy_health -= damage
            print(f"{character_name} attacked {enemy_name} with {damage} damage.")
        elif user_decision == "2":
            can_take_damage = False
            print(f"{character_name} can no longer take damage.")
        elif user_decision == "3":
            health += 1
            print(f"{character_name} healed 1HP.")
        elif user_decision == "I want to win":
            break

        if enemy_health <= 0:
            print(f"{enemy_name} died!")
            break
        ## line break
        print("")
        ## Enemy

        enemy_decision = randint(1, 10)

        if enemy_decision <= 7 and can_take_damage:  # Enemy will attack
            health -= enemy_damage
            print(f"{enemy_name} attacked {character_name} for {enemy_damage}.")

        elif enemy_decision <= 7 and not can_take_damage:
            print(f"{enemy_name} tried to attack for {enemy_damage}, but was blocked by {character_name}.")

        elif enemy_decision <= 10:
            enemy_health += 1
            print(f"{enemy_name} healed 1HP.")

        print("")
        print(f"{character_name}'s health is now {health}")
        print(f"{enemy_name}'s health is now {enemy_health}")

    # if user_decision == "I want to win":
    #  print(f"{character_name} found the cheat!")
    #  pass
    if enemy_health < 0:
        enemy_health = 0
        wins += 1
    if health < 0:
        health = 0
        enemy_wins += 1

    if health > enemy_health:
        print(f"{character_name} wins game {i + 1}! Good job {character_name}.")
    elif health == enemy_health:
        print("Both died! Unlucky!")
    else:
        print(f"{character_name} loses.")


    if wins >= 2 and enemy_wins == 0:
        break
    elif enemy_wins >= 2 and wins == 0:
        break
    print("")
    input(f"Press enter to start game {i + 2}...")
if wins > enemy_wins:
    print(f"{character_name} wins the match! Good job {character_name}. Final score {wins} to {enemy_wins}")
if enemy_wins > wins:
    print(f"{enemy_name} wins the match! Final score: {enemy_wins} to {wins}")

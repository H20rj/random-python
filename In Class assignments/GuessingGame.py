## import randint function from random module
from random import randint
## Assign numbers for user
my_number = randint(1, 30)


user_number = int(input("Give me a number from 1 - 30: "))

while not user_number > 30 or user_number < 0:
    user_number = int(input("follow the rules please. enter another number: "))

try_counter = 1

## Start the guessing
while not user_number == my_number:
    print("Wrong!")
    if user_number > my_number:
        print("Too high! Idiot.")
    if user_number < my_number:
        print("Too low!That was a stupid guess.")
    user_number = int(input("Try again! Enter a new number from 1 - 30: "))
    try_counter += 1

## Tie the knot
try_results = str(try_counter)
print(f"Good job! You got it in {try_results} tries!")

## import randint function from random module
from random import randint

## Assign numbers for user
target = randint(1, 30)


user_number = int(input("Give me a number from 1 - 30: "))

while user_number < 1 or user_number > 30:
    user_number = int(input("Follow the rules please. Enter a number: "))

try_counter = 0



## Start the guessing
while user_number != target:
    try_counter += 1
    print("Thinking...")
    if user_number > target:
        print("Too high!")
    if user_number < target:
        print("Too low!")
    user_number = int(input("Try again! Enter a new number from 1 - 30: "))
    while user_number > 30 or user_number < 0:
        user_number = int(input("follow the rules please. enter another number: "))



## Tie the knot

print(f"Good job! You got it in {try_counter} tries!")

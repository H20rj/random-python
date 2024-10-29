## import randint function from random module
from random import randint
import time
## Assign numbers for user
my_number = randint(1, 30)


user_number = int(input("Give me a number from 1 - 30: "))

while user_number < 0 or user_number > 30:
    user_number = int(input("follow the rules please. enter another number: "))

try_counter = 1

## Start the guessing
while not user_number == my_number:
    print("Thinking...")
    time.sleep(1.5)
    print("Wrong!")
    print("But where?")
    time.sleep(0.5)
    if user_number > my_number:
        print("Too high! Idiot.")
    if user_number < my_number:
        print("Too low!That was a stupid guess.")
    time.sleep(1.5)
    user_number = int(input("Try again! Enter a new number from 1 - 30: "))
    while user_number > 30 or user_number < 0:
        user_number = int(input("follow the rules please. enter another number: "))
    try_counter += 1


## Tie the knot

print(f"Good job! You got it in {str(try_counter)} tries!")

answerDict: dict[int, str] = {}
string = input("Enter a list of answers:\n").replace(" ", "").upper()
ITERATIONS: int = 0
RUN: bool = True
for letter in string:  # create dictionary
    ITERATIONS += 1
    answerDict[ITERATIONS] = letter
ITERATIONS = 1

while RUN:
    jump_to: str = input(
        "Enter a question number to jump to (q to exit, enter for next): "
    )
    if jump_to.isdigit():
        print(f"{jump_to}: {answerDict[int(jump_to)]}")
        ITERATIONS = int(jump_to) + 1
    elif jump_to == "q":
        RUN = False
    elif not jump_to.isdigit() and not jump_to == "":
        print("Invalid input")

    else:
        if ITERATIONS > len(answerDict):
            print("No more answers")
            RUN = False
        else:
            print(f"{ITERATIONS}: {answerDict[ITERATIONS]}")
            ITERATIONS += 1

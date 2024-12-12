"""Takes Answers given by classmates and reads them out
version: 1
"""

from os import system


def main() -> None:
    """Main function"""
    string = input("Enter a string of answers, no commas: \n").replace(" ", "")
    iterations = 0
    string_len = range(len(string))
    system("clear")
    run = True
    while run:
        iterations += 1
        jump_to = input(
            "Enter a number to jump to question" "(enter for next, q to exit)...\n"
        )
        system("clear")

        if jump_to.isdigit():
            jump_to_index = int(jump_to) - 1
            if jump_to_index in string_len:
                print(f"Answer for question" f"{jump_to}: {string[int(jump_to_index)]}")
                iterations = jump_to_index + 1
            else:
                print(f"Invalid question number: {jump_to}")
        elif jump_to == "q":
            run = False
        else:
            if iterations - 1 > max(string_len):
                print("no more answers")
                run = False
            else:
                print(f"Answer for question {iterations}: {string[iterations-1]}")


if __name__ == "__main__":
    main()

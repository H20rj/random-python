"""Version: 2"""


def main() -> None:
    """Main"""
    answer_dict: dict[int, str] = {}

    string = input("Enter a list of answers:\n").replace(" ", "").upper()
    iterations: int = 0
    run: bool = True
    for letter in string:  # create dictionary
        iterations += 1
        answer_dict[iterations] = letter
    iterations = 1

    while run:
        jump_to: str = input(
            "Enter a question number to jump to (q to exit, enter for next): "
        )
        if jump_to.isdigit():
            print(f"{jump_to}: {answer_dict[int(jump_to)]}")
            iterations = int(jump_to) + 1
        elif jump_to == "q":
            run = False
        elif not jump_to.isdigit() and not jump_to == "":
            print("Invalid input")

        else:
            if iterations > len(answer_dict):
                print("No more answers")
                run = False
            else:
                print(f"{iterations}: {answer_dict[iterations]}")
                iterations += 1


if __name__ == "__main__":
    main()

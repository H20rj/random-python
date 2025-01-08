
import_success = True
try:
    from colorama import Fore
except ModuleNotFoundError:
    print("Colorama module not found. Please install it using 'pip install colorama'")
    import_success = False

def add(a: int or float, b: int or float) -> int or float:
    return a + b

def subtract(a: int or float, b: int or float) -> int or float:
    return a - b

def multiply(a: int or float, b: int or float) -> int or float:
    return a * b

def divide(a: int or float, b: int or float) -> float:
    return a / b

def exponent(a: int or float, b: int or float) -> int or float:
    return a ** b

def main_colorama() -> None:
    print(Fore.MAGENTA + "Welcome to the Calculator!")
    print()
    print(Fore.BLUE + "What operation would you like to perform?")
    print(Fore.YELLOW + "    1. Addition")
    print("    2. Subtraction")
    print("    3. Multiplication")
    print("    4. Division")
    print("    5. Exponent")
    user_input = input(Fore.BLUE + "Select an option: ")
    print()

    while user_input not in ["1", "2", "3", "4", "5"]:
        print("Incorrect value. Please try again.")


    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    while True:
        try:
            num1 = int(num1.strip())
            num2 = int(num2.strip())
            break
        except ValueError:
            print()
            print("Not a number in one of your number entries. Please try again.")
            num1 = input("Enter the first number: ")
            num2 = input("Enter the second number: ")
    if user_input == "1":

        print(add(num1, num2))

    elif user_input == "2":

        print(subtract(num1, num2))

    elif user_input == "3":

        print(multiply(num1, num2))

    elif user_input == "4":

        print(divide(num1, num2))

    elif user_input == "5":
        print(exponent(num1, num2))

def main_no_colorama() -> None:
    print("Welcome to the Calculator!")
    print()
    print("What operation would you like to perform?")
    print("    1. Addition")
    print("    2. Subtraction")
    print("    3. Multiplication")
    print("    4. Division")
    print("    5. Exponent")
    user_input = input("Select an option: ")
    print()

    while user_input not in ["1", "2", "3", "4", "5"]:
        print("Incorrect value. Please try again.")

    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    while True:
        try:
            num1 = int(num1.strip())
            num2 = int(num2.strip())
            break
        except ValueError:
            print()
            print("Not a number in one of your number entries. Please try again.")
            num1 = input("Enter the first number: ")
            num2 = input("Enter the second number: ")
    if user_input == "1":

        print(add(num1, num2))

    elif user_input == "2":

        print(subtract(num1, num2))

    elif user_input == "3":

        print(multiply(num1, num2))

    elif user_input == "4":

        print(divide(num1, num2))

    elif user_input == "5":
        print(exponent(num1, num2))

if __name__ == "__main__":
    if import_success:
        main_colorama()
    elif not import_success:
        main_no_colorama()


import time

def series_resistors():
    global resistance_eq
    print("." * 20)
    print("Series Resistors")
    print("." * 20)
    print('')
    s_resistors_n = int(input("How many resistors do you have in series?: "))
    s_resistances = []

    for i in range(1, s_resistors_n + 1):
        resistance = int(input(f"What is the resistance of resistor {i}? "))
        s_resistances.append(resistance)

    resistance_eq = sum(s_resistances)
    print(f"For your {s_resistors_n} resistors, the equivalent resistance is: {resistance_eq} ohms")


def parallel_resistors():
    global resistance_eq
    print("." * 20)
    print("Parallel Resistors")
    print("." * 20)
    print('')
    p_resistors_n = int(input("How many resistors do you have in parallel?: "))

    p_resistances = []
    for i in range(1, p_resistors_n + 1):
        resistance = int(input(f"What is the resistance of resistor {i}? "))
        p_resistances.append(resistance)

    resistance_eq = 1 / sum(1 / r for r in p_resistances)

    print(f"For your {p_resistors_n} resistors, the equivalent resistance is: {resistance_eq:.2f} ohms")

resistance_eq = 0
def main():

    def opening():
        print("." * 20)
        print("Resistors")
        print("." * 20)
        print('')
        print("1. Series Resistors")
        print("2. Parallel Resistors")
        print("3. Exit")
        print('')


    opening()
    user_choice = input("What would you like to do?: ")
    while user_choice not in ["1", "2", "3"]:
        print("Invalid input.")
        user_choice = input("What would you like to do?: ")


    while user_choice != "3":
        if user_choice == "1":
            series_resistors()
        elif user_choice == "2":
            parallel_resistors()
        opening()
        user_choice = input("What would you like to do?: ")

    success = False
    if resistance_eq != 0:
        try:
            with open('resistance_save.txt', 'w') as f:
                f.write(f"Most recent equivalent resistance:\n\n{resistance_eq:.2f} ohms")
            success = True
        except FileNotFoundError:
            print("save file not found. Creating one now...")
            print("maybe it was deleted!")
            print("If you don't see a file named resistance_save.txt, please create one with that exact name.")
            success = False

    elif resistance_eq == 0:
        print("No equivalent resistance found. None saved")
    print("")
    ## Save
    print("Saving")
    time.sleep(0.5)
    if success:
        print("Most recent equivalent resistance save in resistance_save.txt")
    elif not success:
        print("Not saved")

    time.sleep(0.5)
    print("Exiting...")



if __name__ == "__main__":
    main()



















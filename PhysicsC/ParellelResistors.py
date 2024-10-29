print("."*20)
print("Parallel Resistors")
print("."*20)

resistors_n = int(input("How many resistors do you have in parallel?(max = 6): "))
while resistors_n > 6 or resistors_n < 1:
    print("Invalid Input")
    resistors_n = int(input("How many resistors do you have in parallel?(max = 6): "))
if resistors_n == 1:
    resistance = int(input(f"What is the resistance of resistor 1?"))
    resistance_eq = resistance
elif resistors_n == 2:
    resistance = int(input(f"What is the resistance of resistor 1?"))
    resistance_1 = int(input(f"What is the resistance of resistor 2?"))
    resistance_eq = ((1/resistance) + (1/resistance_1))**-1
elif resistors_n == 3:
    resistance = int(input(f"What is the resistance of resistor 1?"))
    resistance_1 = int(input(f"What is the resistance of resistor 2?"))
    resistance_2 = int(input(f"What is the resistance of resistor 3?"))
    resistance_eq = ((1/resistance) + (1/resistance_1) + (1/resistance_2))**-1
elif resistors_n == 4:
    resistance = int(input(f"What is the resistance of resistor 1?"))
    resistance_1 = int(input(f"What is the resistance of resistor 2?"))
    resistance_2 = int(input(f"What is the resistance of resistor 3?"))
    resistance_3 = int(input(f"What is the resistance of resistor 4?"))
    resistance_eq = ((1/resistance) + (1/resistance_1) + (1/resistance_2) +
                     (1/resistance_3))**-1
elif resistors_n == 5:
    resistance = int(input(f"What is the resistance of resistor 1?"))
    resistance_1 = int(input(f"What is the resistance of resistor 2?"))
    resistance_2 = int(input(f"What is the resistance of resistor 3?"))
    resistance_3 = int(input(f"What is the resistance of resistor 4?"))
    resistance_4 = int(input(f"What is the resistance of resistor 5?"))
    resistance_eq = ((1/resistance) + (1/resistance_1) + (1/resistance_2) +
                     (1/resistance_3) + (1/resistance_4))**-1
elif resistors_n == 6:
    resistance = int(input(f"What is the resistance of resistor 1?"))
    resistance_1 = int(input(f"What is the resistance of resistor 2?"))
    resistance_2 = int(input(f"What is the resistance of resistor 3?"))
    resistance_3 = int(input(f"What is the resistance of resistor 4?"))
    resistance_4 = int(input(f"What is the resistance of resistor 5?"))
    resistance_5 = int(input(f"What is the resistance of resistor 6?"))
    resistance_eq = ((1/resistance) + (1/resistance_1) + (1/resistance_2) +
                     (1/resistance_3) + (1/resistance_4) + (1/resistance_5))**-1
print("")
print(f"For your {resistors_n} resistors, the equivalent resistance is: {resistance_eq:.2f} ohms")

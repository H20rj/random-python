print("."*20)
print("Parallel Resistors")
print("."*20)

resistors_n = int(input("How many resistors do you have in parallel? "))

resistances = []
for i in range(1, resistors_n + 1):
    resistance = int(input(f"What is the resistance of resistor {i}? "))
    resistances.append(resistance)

resistance_eq = 1 / sum(1/r for r in resistances)

print(f"For your {resistors_n} resistors, the equivalent resistance is: {resistance_eq:.2f} ohms")
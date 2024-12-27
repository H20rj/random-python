import math


def main():
    print("Welcome to the currency converter!")
    print("Please enter the currency you want to convert to from USD:")
    print("    1. British Pound")
    print("    2. Euro")
    print("    3. Indian Rupee")
    print("    4. Australian Dollar")
    print("    5. Swiss Franc")
    print("    6. Canadian Dollar")
    print("    7. Singapore Dollar")
    print("    8. Malaysian Ringgit")
    print("    9. Japanese Yen")
    print("    10. Chinese Yuan")
    user_choice = int(input("Enter your choice: "))

    while user_choice < 1 or user_choice > 10:
        print("Invalid choice. Please enter a valid choice.")
        user_choice = int(input("Enter your choice: "))

    if user_choice == 1:
        print("1 USD = 0.799 British Pounds")
        while True:
            user_amount = input("Input the amount of money you want to convert from USD:\n")
            try:
                user_amount = float(user_amount)
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        converted_amount = user_amount * 0.799
        print(f"${user_amount:.2f} USD is equal to £{converted_amount:.2f} British Pounds.")

    elif user_choice == 2:
        print("1 USD = 1.155 Euros")
        while True:
            user_amount = input("Input the amount of money you want to convert from USD:\n")
            try:
                user_amount = float(user_amount)
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        converted_amount = user_amount * 1.155
        print(f"${user_amount:.2f} USD is equal to €{converted_amount:.2f} Euros.")

    elif user_choice == 3:
        print("1 USD = 85.343 Indian Rupees")
        while True:
            user_amount = input("Input the amount of money you want to convert from USD:\n")
            try:
                user_amount = float(user_amount)
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        converted_amount = user_amount * 85.343
        print(f"${user_amount:.2f} USD is equal to ₹{converted_amount:.2f} Indian Rupees.")

    elif user_choice == 4:
        print("1 USD = 1.609 Australian Dollars")
        while True:
            user_amount = input("Input the amount of money you want to convert from USD:\n")
            try:
                user_amount = float(user_amount)
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        converted_amount = user_amount * 1.609
        print(f"${user_amount:.2f} USD is equal to A${converted_amount:.2f} Australian Dollars.")

    elif user_choice == 5:
        print("1 USD = 0.899 Swiss Franc")
        while True:
            user_amount = input("Input the amount of money you want to convert from USD:\n")
            try:
                user_amount = float(user_amount)
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        converted_amount = user_amount * 0.899
        print(f"${user_amount:.2f} USD is equal to {converted_amount:.2f} CHF Swiss Franc.")

    elif user_choice == 6:
        print("1 USD = 1.441 Canadian Dollars")
        while True:
            user_amount = input("Input the amount of money you want to convert from USD:\n")
            try:
                user_amount = float(user_amount)
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        converted_amount = user_amount * 1.441
        print(f"${user_amount:.2f} USD is equal to C${converted_amount:.2f} Canadian Dollars.")

    elif user_choice == 7:
        print("1 USD = 1.340 Singapore Dollars")
        while True:
            user_amount = input("Input the amount of money you want to convert from USD:\n")
            try:
                user_amount = float(user_amount)
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        converted_amount = user_amount * 1.34
        print(f"${user_amount:.2f} USD is equal to S${converted_amount:.2f} Singapore Dollars.")

    elif user_choice == 8:
        print("1 USD = 4.477 Malaysian Ringgit")
        while True:
            user_amount = input("Input the amount of money you want to convert from USD:\n")
            try:
                user_amount = float(user_amount)
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        converted_amount = user_amount * 4.477
        print(f"${user_amount:.2f} USD is equal to RM{converted_amount:.2f} Malaysian Ringgit.")

    elif user_choice == 9:
        print("1 USD = 157.663 Japanese Yen")
        while True:
            user_amount = input("Input the amount of money you want to convert from USD:\n")
            try:
                user_amount = float(user_amount)
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        converted_amount = user_amount * 157.663
        print(f"${user_amount:.2f} USD is equal to ¥{converted_amount:.2f} Japanese Yen.")

    elif user_choice == 10:
        print("1 USD = 7.297 Chinese Yuan")
        while True:
            user_amount = input("Input the amount of money you want to convert from USD:\n")
            try:
                user_amount = float(user_amount)
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        converted_amount = user_amount * 7.297
        print(f"${user_amount:.2f} USD is equal to CN¥{converted_amount:.2f} Chinese Yuan.")


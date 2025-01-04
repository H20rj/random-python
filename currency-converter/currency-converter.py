def main():
    print("Welcome to currency converter, please select a currency:")
    currency_data = {
        "British Pound": {"rate": 0.795, "symbol": "£"},
        "Euro": {"rate": 0.959, "symbol": "€"},
        "Indian Rupee": {"rate": 85.391, "symbol": "₹"},
        "Australian Dollar": {"rate": 1.609, "symbol": "A$"},
        "Canadian Dollar": {"rate": 1.441, "symbol": "C$"},
        "Singapore Dollar": {"rate": 1.340, "symbol": "S$"},
        "Swiss Franc": {"rate": 0.902, "symbol": "CHF"},
        "Malaysian Ringgit": {"rate": 4.472, "symbol": "RM"},
        "Japanese Yen": {"rate": 157.872, "symbol": "¥"},
        "Chinese Yuan": {"rate": 7.298, "symbol": "C¥"}
    }

    currencies = list(currency_data.keys())
    for index, currency in enumerate(currencies, start=1): # print possible currencies
        print(f"    {index}. {currency}")

    while True: ## get user choice
        try:
            user_choice = int(input("Enter your choice: "))
            if 1 <= user_choice <= len(currencies):
                target_currency = currencies[user_choice - 1]
                break
            else:
                print("Invalid choice. Please enter a valid choice.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    while True:
        direction = input(
            "Do you want to convert TO this currency or FROM this currency to USD? (T/F): ").strip().upper()
        if direction in ["T", "F"]:
            break
        else:
            print("Invalid input. Please enter either 'T' or 'F'.")

    currency_rate = currency_data[target_currency]["rate"]
    currency_symbol = currency_data[target_currency]["symbol"]

    while True:
        try:
            if direction == "T":
                user_amount = float(input(f"Enter the amount of money you want to convert to {target_currency} in USD: $"))
            else:
                user_amount = float(input(f"Enter the amount of money you want to convert from {target_currency} in USD: {currency_symbol}"))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    if direction == "T":
        converted_amount = user_amount * currency_rate
        print(f"${user_amount} is equal to {converted_amount:.2f} {currency_symbol}.")
    else:
        converted_amount = user_amount / currency_rate
        print(f"{user_amount} {currency_symbol} is equal to ${converted_amount:.2f}.")



if __name__ == "__main__":
    main()
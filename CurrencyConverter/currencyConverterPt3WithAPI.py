import requests
from dotenv import load_dotenv
import os

load_dotenv()

EXCHANGE_RATE_API_KEY = os.getenv("EXCHANGE_RATE_API_KEY")
def get_currency_data(base_currency="USD"):
    if not EXCHANGE_RATE_API_KEY:
        print("EXCHANGE_RATE_API_KEY not found in .env file.")
        return None

    url = f"https://v6.exchangerate-api.com/v6/{EXCHANGE_RATE_API_KEY}/latest/{base_currency}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        rates = data.get("conversion_rates", {})

        currency_symbols = {
            "GBP": "£",
            "EUR": "€",
            "INR": "₹",
            "AUD": "A$",
            "CHF": "CHF",
            "CAD": "C$",
            "SGD": "S$",
            "MYR": "RM",
            "JPY": "¥",
            "CNY": "CN¥",
            "USD": "$"
        }

        currency_data = {}

        for code, symbol in currency_symbols.items():
            if code in rates:
                currency_data[code] = {"rate": rates[code], "symbol": symbol}
        return currency_data

    except requests.exceptions.RequestException as e:
        print("Error fetching currency data:", e)
        return None

def main() -> None:
    print("Fetching currency data...")

    currency_data = get_currency_data(base_currency="USD")
    if not currency_data:
        print("Failed to fetch currency data.")
        return

    currency_names = {
        "GBP": "British Pound",
        "EUR": "Euro",
        "INR": "Indian Rupee",
        "AUD": "Australian Dollar",
        "CHF": "Swiss Franc",
        "CAD": "Canadian Dollar",
        "SGD": "Singapore Dollar",
        "MYR": "Malaysian Ringgit",
        "JPY": "Japanese Yen",
        "CNY": "Chinese Yuan",
        "USD": "United States Dollar"
    }

    print("Welcome to currency converter!")

    currencies = list(currency_names.keys())

    for index, code in enumerate(currencies, start=1):
        print(f"    {index}. {currency_names[code]}")

    while True:
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

        print("Invalid input. Please enter either 'T' or 'F'.")

    rate = currency_data[target_currency]["rate"]
    symbol = currency_data[target_currency]["symbol"]

    while True:
        try:
            amount = float(input(f"Enter the amount of money you want to convert:"))
            if amount > 0:
                break
            else:
                print("Invalid input. Please enter a positive number.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")

    if direction == "T":
        converted_amount = amount * rate
        print(f"{amount:.2f} USD is equal to {symbol}{converted_amount:.2f} {currency_names[target_currency]}.")

    else:
        converted_amount = amount / rate
        print(f"{symbol}{amount:.2f} {currency_names[target_currency]} is equal to {converted_amount:.2f} USD.")







if __name__ == "__main__":
    main()
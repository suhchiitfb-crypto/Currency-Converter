import requests

def get_rate(from_currency, to_currency):
    url = "https://api.frankfurter.app/latest"
    params = {
        "base": from_currency,
        "symbols": to_currency
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data["rates"][to_currency]

def convert(amount, from_currency, to_currency):
    rate = get_rate(from_currency, to_currency)
    converted = amount * rate
    return round(converted, 2)

def show_currencies():
    response = requests.get("https://api.frankfurter.app/currencies")
    currencies = response.json()
    for code in sorted(currencies):
        print(code + " - " + currencies[code])

def get_historical_rate(date, from_currency, to_currency):
    url = "https://api.frankfurter.app/" + date
    params = {
        "from": from_currency,
        "to": to_currency
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data["rates"][to_currency]

while True:
    print("\n--- CURRENCY CONVERTER ---")
    from_currency = input("Convert from (e.g. USD, 'list', or 'history' for past rates): ").upper()
    if from_currency == "LIST":
        show_currencies()
        continue
    if from_currency == "HISTORY":
        date = input("Enter date (YYYY-MM-DD): ")
        hist_from = input("Convert from (e.g. USD): ").upper()
        hist_to = input("Convert to (e.g. GBP): ").upper()
        try:
            hist_rate = get_historical_rate(date, hist_from, hist_to)
            print("On " + date + ", 1 " + hist_from + " = " + str(hist_rate) + " " + hist_to)
        except KeyError:
            print("Sorry, couldn't find that rate — check your currency codes or date.")
        continue
    to_currency = input("Convert to (e.g. GBP): ").upper()
    amount_input = input("Amount: ")

    if not amount_input.replace(".", "", 1).isdigit():
        print("Please enter a valid number.")
        continue

    amount = float(amount_input)

    try:
        result = convert(amount, from_currency, to_currency)
        print(str(amount) + " " + from_currency + " = " + str(result) + " " + to_currency)
    except KeyError:
        print("Sorry, one of those currency codes isn't supported.")

    again = input("\nConvert again? (y/n): ")
    if again.lower() != "y":
        print("Goodbye!")
        break 
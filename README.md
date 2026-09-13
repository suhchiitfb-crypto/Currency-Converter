# Currency Converter

A command-line currency converter built in Python, using live exchange rate data from the [Frankfurter API](https://www.frankfurter.app/).

## Features

- Convert between currencies using live, up-to-date exchange rates
- View a list of all supported currency codes at any time (`list`)
- Look up historical exchange rates for a specific past date (`history`)
- Input validation — handles invalid amounts and unsupported currency codes gracefully

## How to run

1. Clone this repository
2. Set up a virtual environment and install dependencies:
python3 -m venv venv
source venv/bin/activate
pip install requests

3. Run the app:

python3 currency.py


## Example

Convert from (e.g. USD, 'list', or 'history' for past rates): USD
Convert to (e.g. GBP): GBP
Amount: 100
100.0 USD = 74.03 GBP
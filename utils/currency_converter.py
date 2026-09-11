import requests


class CurrencyConverter:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.fastforex.io/convert"

    def convert(self, amount: float, from_currency: str, to_currency: str):
        """Convert the amount from one currency to another."""

        params = {
            "from": from_currency,
            "to": to_currency,
            "amount": amount,
            "api_key": self.api_key
        }

        response = requests.get(self.base_url, params=params)

        if response.status_code != 200:
            raise Exception(f"API call failed: {response.text}")

        data = response.json()

        return data["result"][to_currency]
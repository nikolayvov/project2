import os

import requests
from dotenv import load_dotenv

load_dotenv()


def convert_rub(operations: dict) -> float:
    """Функция, которая конвертирует сумму транзакции в рубли."""
    from_currency = operations["operationAmount"]["currency"]["code"]
    amount = operations["operationAmount"]["amount"]
    to_currency = "RUB"
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to_currency}&from={from_currency}&amount={amount}"
    headers = {"apikey": os.getenv("APILAYER_KEY")}
    response = requests.get(url, headers=headers)
    return response.json()["result"]


print(
    convert_rub(
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560",
        }
    )
)

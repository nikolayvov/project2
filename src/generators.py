from typing import Generator

transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {
            "amount": "79114.93",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188"
    },
    {
        "id": 142264269,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {
            "amount": "79115.93",
            "currency": {
                "name": "RUB",
                "code": "RUB"
            }
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258543",
        "to": "Счет 75651667383060284189"
    },
    {
        "id": 142264270,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {
            "amount": "79116.93",
            "currency": {
                "name": "EUR",
                "code": "EUR"
            }
        },
        "description": "Перевод с карты на карту",
        "from": "Счет 19708645243227258544",
        "to": "Счет 75651667383060284190"
    }
]


def filter_by_currency(transactions: list[dict], currency: str) -> Generator:
    """
        ФФункция, которая возвращает итератор, который
            поочередно выдает транзакции, где код валюты операции
            соответствует заданному
        """
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


def transaction_descriptions(transactions: list[dict]) -> Generator:
    """
            Функция, которая принимает список словарей с транзакциями
            и возвращает описание каждой операции по очереди
            """
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, end: int) -> Generator:
    """
                Функция генератор номеров банковских карт в формате XXXX XXXX XXXX XXXX
                """
    for i in range(start, end + 1):
        card_str = str(i).zfill(16)
        card_number = card_str[:4] + ' ' + card_str[4:8] + ' ' + card_str[8:12] + ' ' + card_str[12:]
        yield card_number


# t = filter_by_currency(transactions, "USD")
# for i in t:
#     print(i)

# d = transaction_descriptions(transactions)
# for i in d:
#     print(i)

# c = card_number_generator(1, 11)
# for i in c:
#     print(i)

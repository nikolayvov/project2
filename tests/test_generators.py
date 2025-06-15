import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


@pytest.mark.parametrize(
    "currency, expected",
    [
        (
            "USD",
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
                "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                "description": "Перевод организации",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702",
            },
        ),
        (
            "RUB",
            {
                "id": 142264269,
                "state": "EXECUTED",
                "date": "2019-04-04T23:20:05.206878",
                "operationAmount": {"amount": "79115.93", "currency": {"name": "RUB", "code": "RUB"}},
                "description": "Перевод со счета на счет",
                "from": "Счет 19708645243227258543",
                "to": "Счет 75651667383060284189",
            },
        ),
        (
            "EUR",
            {
                "id": 142264270,
                "state": "EXECUTED",
                "date": "2019-04-04T23:20:05.206878",
                "operationAmount": {"amount": "79116.93", "currency": {"name": "EUR", "code": "EUR"}},
                "description": "Перевод с карты на карту",
                "from": "Счет 19708645243227258544",
                "to": "Счет 75651667383060284190",
            },
        ),
    ],
)
def test_filter_by_currency(currency, expected, currency_code):
    """Тест с параметризацией"""
    _generator = filter_by_currency(currency_code, currency)
    assert next(_generator) == expected


def test_filter_by_currency_2(currency_code):
    _generator = filter_by_currency(currency_code, "USD")
    assert next(_generator) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    assert next(_generator) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }


def test_transaction_descriptions(currency_code):
    _generator = transaction_descriptions(currency_code)
    assert next(_generator) == "Перевод организации"
    assert next(_generator) == "Перевод со счета на счет"
    assert next(_generator) == "Перевод со счета на счет"
    assert next(_generator) == "Перевод с карты на карту"


def test_card_number_generator():
    _generator = card_number_generator(1, 3)
    assert next(_generator) == "0000 0000 0000 0001"
    assert next(_generator) == "0000 0000 0000 0002"
    assert next(_generator) == "0000 0000 0000 0003"

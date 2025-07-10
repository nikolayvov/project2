from src.filter import process_bank_search, process_bank_operations


def test_process_bank_search(currency_code):
    assert process_bank_search(currency_code, "организации") == [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        }
    ]


def test_process_bank_operations(currency_code):
    categories = ["Перевод организации", "Перевод со счета на счет", "Оплата услуг", "Перевод с карты на карту"]

    expected = {
        "Перевод организации": 1,
        "Перевод со счета на счет": 2,
        "Перевод с карты на карту": 1

    }
    result = process_bank_operations(currency_code, categories)
    assert result == expected

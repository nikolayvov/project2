import pytest


@pytest.fixture
def correct_c_number():
    """Данные для проверки функции get_mask_card_number"""
    return "1264 56** **** 4888"


@pytest.fixture
def correct_a_number():
    """Данные для проверки функции get_mask_account"""
    return "**3086"


@pytest.fixture
def correct_card():
    """Данные для проверки функции mask_account_card с данными карты"""
    return "Visa Platinum 7000 79** **** 6361"


@pytest.fixture
def correct_account():
    """Данные для проверки функции mask_account_card с данными счета"""
    return "Счет **4305"


@pytest.fixture
def correct_date():
    """Данные для проверки функции get_date"""
    return "11.03.2024"


@pytest.fixture
def correct_state():
    """Данные для проверки функции filter_by_state"""
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def correct_date_sort():
    """Данные для проверки функции sort_by_date"""
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def currency_code():
    """Данные для проверки функции filter_by_currency"""
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 142264269,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79115.93", "currency": {"name": "RUB", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258543",
            "to": "Счет 75651667383060284189",
        },
        {
            "id": 142264270,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79116.93", "currency": {"name": "EUR", "code": "EUR"}},
            "description": "Перевод с карты на карту",
            "from": "Счет 19708645243227258544",
            "to": "Счет 75651667383060284190",
        },
    ]

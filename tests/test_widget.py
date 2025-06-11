import pytest


from src.masks import get_mask_card_number, get_mask_account
from src.widget import mask_account_card, get_date


def test_mask_account_card(correct_card):
    assert mask_account_card("Visa Platinum 7000792289606361") == correct_card


def test_mask_account_card(correct_account):
    assert mask_account_card("Счет 73654108430135874305") == correct_account


def test_get_date(correct_date):
    assert get_date("2024-03-11T02:26:18.671407") == correct_date


@pytest.mark.parametrize(
    "date, expected",
    [
        ("", "Неверный формат входных данных"),
        ("20240311T02:26:18.671407", "Неверный формат входных данных"),
        ("2024-03-11T02:26:18.6714071234567890", "Неверный формат входных данных"),
        ("2024-01-01T00:00:00.000000", "01.01.2024"),
        ("2024-12-31T23:59:59.999999", "31.12.2024"),

    ])
def test_get_date_incorrect(date, expected):
    """Тест функции get_date с параметризацией значений date"""
    assert get_date(date) == expected
